from __future__ import annotations
 
import json
import logging
import logging.handlers
import os
import sys
import time
from typing import Optional
 
 
# --------------------------------------------------------------------------- #
# ANSI Color Codes
# --------------------------------------------------------------------------- #
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
 
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GREY = "\033[90m"
 
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
 
    BG_RED = "\033[41m"
    BG_YELLOW = "\033[43m"
 
 
_LEVEL_COLOR_RAW = {
    logging.DEBUG: Colors.CYAN,
    logging.INFO: Colors.GREEN,
    logging.WARNING: Colors.YELLOW,
    logging.ERROR: Colors.RED,
    logging.CRITICAL: Colors.BOLD + Colors.BG_RED + Colors.WHITE,
}
 
# Cache of "<color><padded_levelname><RESET>" strings, built lazily the
# first time each (levelno, text) pair is seen instead of on every call.
_COLORED_LEVELNAME_CACHE: dict[int, dict[str, str]] = {
    lvl: {} for lvl in _LEVEL_COLOR_RAW
}
 
 
def _colored_levelname(levelno: int, padded_text: str) -> str:
    """Return a cached colorized levelname string, building it once per pair."""
    bucket = _COLORED_LEVELNAME_CACHE.get(levelno)
    if bucket is None:
        return padded_text
    cached = bucket.get(padded_text)
    if cached is None:
        cached = f"{_LEVEL_COLOR_RAW[levelno]}{padded_text}{Colors.RESET}"
        bucket[padded_text] = cached
    return cached
 
 
def _supports_color(stream) -> bool:
    """Detect whether the target stream supports ANSI color codes."""
    if os.environ.get("NO_COLOR") is not None:
        return False
    if os.environ.get("FORCE_COLOR") is not None:
        return True
    if not hasattr(stream, "isatty"):
        return False
    try:
        return stream.isatty()
    except Exception:
        return False
 
 
# --------------------------------------------------------------------------- #
# Formatters
# --------------------------------------------------------------------------- #
class ColorFormatter(logging.Formatter):
    """
    Formatter that adds ANSI colors to console output based on log level.
 
    Mutates record.levelname in place for the duration of the format() call
    and restores it afterward — avoids cloning the whole LogRecord (which
    logging.makeLogRecord does via a dict copy) on every log line. Safe for
    shared records across multiple handlers because the original value is
    always restored before format() returns, even on exception.
    """
 
    DEFAULT_FMT = (
        "%(asctime)s | %(levelname)s | %(name)s | "
        "%(filename)s:%(lineno)d | %(message)s"
    )
 
    def __init__(
        self,
        fmt: Optional[str] = None,
        datefmt: str = "%Y-%m-%d %H:%M:%S",
        use_color: bool = True,
    ):
        super().__init__(fmt or self.DEFAULT_FMT, datefmt=datefmt)
        self.use_color = use_color
 
    def format(self, record: logging.LogRecord) -> str:
        if not self.use_color:
            return super().format(record)
 
        original_levelname = record.levelname
        # Pad to width 8 ourselves (mirrors old %(levelname)-8s) before
        # coloring, so the ANSI escape bytes aren't counted by % padding.
        padded = f"{original_levelname:<8}"
        record.levelname = _colored_levelname(record.levelno, padded)
        try:
            return super().format(record)
        finally:
            record.levelname = original_levelname
 
 
class PlainFormatter(logging.Formatter):
    """Plain formatter used for file output (no ANSI codes)."""
 
    DEFAULT_FMT = (
        "%(asctime)s | %(levelname)-8s | %(name)s | "
        "%(filename)s:%(lineno)d | %(message)s"
    )
 
    def __init__(self, fmt: Optional[str] = None, datefmt: str = "%Y-%m-%d %H:%M:%S"):
        super().__init__(fmt or self.DEFAULT_FMT, datefmt=datefmt)
 
 
class JsonFormatter(logging.Formatter):
    """
    Formatter that emits log records as single-line JSON objects.
 
    Avoids constructing a datetime object per record (datetime.fromtimestamp
    is comparatively slow); uses time.strftime + msecs directly instead.
    """
 
    _TIME_FMT = "%Y-%m-%dT%H:%M:%S"
 
    def format(self, record: logging.LogRecord) -> str:
        ct = time.localtime(record.created)
        timestamp = f"{time.strftime(self._TIME_FMT, ct)}.{int(record.msecs):03d}"
 
        payload = {
            "timestamp": timestamp,
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False)
 
 
# --------------------------------------------------------------------------- #
# Logger factory / manager
# --------------------------------------------------------------------------- #
_CONFIGURED_LOGGERS: dict[str, logging.Logger] = {}
 
_LEVEL_MAP = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "WARN": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
    "FATAL": logging.CRITICAL,
}
 
 
def _resolve_level(level) -> int:
    if isinstance(level, int):
        return level
    return _LEVEL_MAP.get(str(level).upper(), logging.INFO)
 
 
def _safe_filename(name: str) -> str:
    return "".join(c if c.isalnum() or c in "-_." else "_" for c in name) or "app"
 
 
def get_logger(
    name: str = "app",
    *,
    log_dir: str = "logs",
    level="DEBUG",
    console: bool = True,
    file_output: bool = True,
    error_file_output: bool = True,
    json_format: bool = False,
    rotation: str = "size",          # "size" | "time" | "none"
    max_bytes: int = 10 * 1024 * 1024,
    backup_count: int = 5,
    when: str = "midnight",          # for time-based rotation
    color: Optional[bool] = None,    # None = auto-detect
    propagate: bool = False,
) -> logging.Logger:
    """
    Create (or return an already-configured) logger with console + file handlers.
 
    Repeated calls with the same `name` return the cached instance immediately
    via a dict lookup, without re-touching the filesystem or rebuilding handlers.
 
    Args:
        name: Logger name (usually __name__).
        log_dir: Directory where log files are written.
        level: Minimum log level (e.g. "DEBUG", "INFO", logging.DEBUG).
        console: Enable colored console handler.
        file_output: Enable general rotating file handler.
        error_file_output: Enable a dedicated file for ERROR+ records.
        json_format: Use JSON formatting for file handlers instead of plain text.
        rotation: "size" (RotatingFileHandler), "time" (TimedRotatingFileHandler), or "none".
        max_bytes: Max file size before rotating (size-based rotation).
        backup_count: Number of rotated backups to keep.
        when: Rotation interval unit for time-based rotation.
        color: Force-enable/disable console color. None = auto-detect TTY.
        propagate: Whether the logger should propagate to the root logger.
 
    Returns:
        Configured logging.Logger instance.
    """
    cached = _CONFIGURED_LOGGERS.get(name)
    if cached is not None:
        return cached
 
    logger = logging.getLogger(name)
    resolved_level = _resolve_level(level)
    logger.setLevel(resolved_level)
    logger.propagate = propagate
 
    if logger.handlers:
        _CONFIGURED_LOGGERS[name] = logger
        return logger
 
    if console:
        use_color = _supports_color(sys.stdout) if color is None else color
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(resolved_level)
        console_handler.setFormatter(ColorFormatter(use_color=use_color))
        logger.addHandler(console_handler)
 
    if file_output or error_file_output:
        os.makedirs(log_dir, exist_ok=True)
 
    file_formatter = JsonFormatter() if json_format else PlainFormatter()
 
    def _make_rotating_handler(filepath: str) -> logging.Handler:
        if rotation == "size":
            return logging.handlers.RotatingFileHandler(
                filepath, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
            )
        elif rotation == "time":
            return logging.handlers.TimedRotatingFileHandler(
                filepath, when=when, backupCount=backup_count, encoding="utf-8"
            )
        return logging.FileHandler(filepath, encoding="utf-8")
 
    if file_output:
        general_path = os.path.join(log_dir, f"{_safe_filename(name)}.log")
        file_handler = _make_rotating_handler(general_path)
        file_handler.setLevel(resolved_level)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
 
    if error_file_output:
        error_path = os.path.join(log_dir, f"{_safe_filename(name)}.error.log")
        error_handler = _make_rotating_handler(error_path)
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(file_formatter)
        logger.addHandler(error_handler)
 
    _CONFIGURED_LOGGERS[name] = logger
    return logger
 
 
def set_level(name: str, level) -> None:
    """Change the log level of an already-configured logger (and its handlers)."""
    logger = _CONFIGURED_LOGGERS.get(name) or logging.getLogger(name)
    resolved = _resolve_level(level)
    logger.setLevel(resolved)
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler) and handler.level == logging.ERROR:
            continue  # keep the dedicated error-file handler at ERROR
        handler.setLevel(resolved)
 
 
def shutdown_logger(name: str) -> None:
    """Remove and close all handlers for a logger, then forget it."""
    logger = _CONFIGURED_LOGGERS.pop(name, None) or logging.getLogger(name)
    for handler in list(logger.handlers):
        handler.close()
        logger.removeHandler(handler)
 
 
def reset_all() -> None:
    """Shut down every logger created through get_logger. Mostly useful for tests."""
    for name in list(_CONFIGURED_LOGGERS.keys()):
        shutdown_logger(name)
 
 
# --------------------------------------------------------------------------- #
# Demo / self-test when run directly
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    log = get_logger("demo", log_dir="logs", level="DEBUG", json_format=False)
 
    log.debug("This is a DEBUG message — cyan")
    log.info("This is an INFO message — green")
    log.warning("This is a WARNING message — yellow")
    log.error("This is an ERROR message — red")
    log.critical("This is a CRITICAL message — bold red background")
 
    try:
        1 / 0
    except ZeroDivisionError:
        log.exception("Caught an exception with traceback logging")
 
    print("\nCheck the ./logs directory for demo.log and demo.error.log")
 