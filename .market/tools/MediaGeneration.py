"""
MediaGeneration.py
==================
Media Generation (Image / Video / Audio) tools from Agno, each as an
independent @tool.

pip install agno openai fal-client replicate elevenlabs moviepy opencv-python
"""

import os
from agno.tools import tool


@tool
def dalle_generate_image(prompt: str) -> str:
    """Generate an image from a text prompt using DALL-E.

    Args:
        prompt (str): Description of the image to generate.
    """
    os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
    from agno.tools.dalle import DalleTools
    return DalleTools().create_image(prompt)


@tool
def fal_generate_image(prompt: str) -> str:
    """Generate an image from a text prompt using Fal.

    Args:
        prompt (str): Description of the image to generate.
    """
    os.environ["FAL_KEY"] = "YOUR_FAL_KEY"
    from agno.tools.fal import FalTools
    return FalTools().generate_image(prompt)


@tool
def replicate_generate_image(prompt: str, model: str = "stability-ai/sdxl") -> str:
    """Generate an image using a model hosted on Replicate.

    Args:
        prompt (str): Description of the image to generate.
        model (str): Replicate model identifier. Defaults to "stability-ai/sdxl".
    """
    os.environ["REPLICATE_API_TOKEN"] = "YOUR_REPLICATE_API_TOKEN"
    from agno.tools.replicate import ReplicateTools
    return ReplicateTools(model=model).generate_image(prompt)


@tool
def gemini_generate_image(prompt: str) -> str:
    """Generate an image using Gemini's image generation (Nano Banana).

    Args:
        prompt (str): Description of the image to generate.
    """
    os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY"
    from agno.tools.models_labs import ModelsLabTools
    return ModelsLabTools().generate_image(prompt)


@tool
def lumalabs_generate_video(prompt: str) -> str:
    """Generate a short video from a text prompt using Luma Labs.

    Args:
        prompt (str): Description of the video to generate.
    """
    os.environ["LUMAAI_API_KEY"] = "YOUR_LUMAAI_API_KEY"
    from agno.tools.lumalab import LumaLabTools
    return LumaLabTools().generate_video(prompt)


@tool
def modelslab_generate_video(prompt: str) -> str:
    """Generate a short video from a text prompt using ModelsLab.

    Args:
        prompt (str): Description of the video to generate.
    """
    os.environ["MODELS_LAB_API_KEY"] = "YOUR_MODELS_LAB_API_KEY"
    from agno.tools.models_labs import ModelsLabTools
    return ModelsLabTools().generate_video(prompt)


@tool
def elevenlabs_text_to_speech(text: str, voice: str = "Rachel") -> str:
    """Convert text to spoken audio using ElevenLabs.

    Args:
        text (str): The text to convert to speech.
        voice (str): Voice name to use. Defaults to "Rachel".
    """
    os.environ["ELEVEN_LABS_API_KEY"] = "YOUR_ELEVENLABS_API_KEY"
    from agno.tools.eleven_labs import ElevenLabsTools
    return ElevenLabsTools(voice_id=voice).generate_speech(text)


@tool
def cartesia_text_to_speech(text: str) -> str:
    """Convert text to spoken audio using Cartesia.

    Args:
        text (str): The text to convert to speech.
    """
    os.environ["CARTESIA_API_KEY"] = "YOUR_CARTESIA_API_KEY"
    from agno.tools.cartesia import CartesiaTools
    return CartesiaTools().generate_speech(text)


@tool
def desi_vocal_text_to_speech(text: str) -> str:
    """Convert text to spoken audio using Desi Vocal TTS.

    Args:
        text (str): The text to convert to speech.
    """
    os.environ["DESI_VOCAL_API_KEY"] = "YOUR_DESI_VOCAL_API_KEY"
    from agno.tools.desi_vocal import DesiVocalTools
    return DesiVocalTools().generate_speech(text)


@tool
def mlx_transcribe_audio(audio_path: str) -> str:
    """Transcribe an audio file to text using MLX Transcribe.

    Args:
        audio_path (str): Path to the audio file.
    """
    from agno.tools.mlx_transcribe import MLXTranscribeTools
    return MLXTranscribeTools().transcribe(audio_path)


@tool
def moviepy_extract_clip(video_path: str, start_seconds: float, end_seconds: float) -> str:
    """Extract a clip from a video file using MoviePy.

    Args:
        video_path (str): Path to the source video file.
        start_seconds (float): Clip start time in seconds.
        end_seconds (float): Clip end time in seconds.
    """
    from agno.tools.moviepy_video import MoviePyVideoTools
    return MoviePyVideoTools().extract_clip(video_path, start_seconds, end_seconds)


@tool
def unsplash_search_photos(query: str) -> str:
    """Search stock photos on Unsplash.

    Args:
        query (str): The search query, e.g. "mountains at sunset".
    """
    os.environ["UNSPLASH_ACCESS_KEY"] = "YOUR_UNSPLASH_ACCESS_KEY"
    from agno.tools.unsplash import UnsplashTools
    return UnsplashTools().search_photos(query)


@tool
def opencv_detect_faces(image_path: str) -> str:
    """Detect faces in an image using OpenCV.

    Args:
        image_path (str): Path to the image file.
    """
    from agno.tools.opencv import OpenCVTools
    return OpenCVTools().detect_faces(image_path)


@tool
def giphy_search_gif(query: str) -> str:
    """Search for a GIF on Giphy.

    Args:
        query (str): The search query, e.g. "excited cat".
    """
    os.environ["GIPHY_API_KEY"] = "YOUR_GIPHY_API_KEY"
    from agno.tools.giphy import GiphyTools
    return GiphyTools().search_gifs(query)
