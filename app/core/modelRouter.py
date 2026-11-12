from dotenv import load_dotenv

from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
from agno.models.anthropic import Claude
from agno.models.ollama import Ollama
from agno.models.deepseek import DeepSeek
from agno.knowledge.embedder.openai import OpenAIEmbedder

load_dotenv()


class ModelRouter:
    """Resolves 'provider:modelname' strings into Agno models / embedders."""

    MODELS = {
        "openai": OpenAIChat,
        "google": Gemini,
        "anthropic": Claude,
        "ollama": Ollama,
        "deepseek": DeepSeek,
    }

    EMBEDDERS = {
        "openai": OpenAIEmbedder,
    }

    @staticmethod
    def _parse(provider_model: str, registry: dict) -> tuple[str, str]:
        if ":" not in (provider_model or ""):
            raise ValueError(f"Invalid format '{provider_model}'. Expected 'provider:modelname'.")
        provider, name = provider_model.split(":", 1)
        provider, name = provider.strip().lower(), name.strip()
        if provider not in registry:
            raise ValueError(f"Unsupported provider '{provider}'. Choose from {list(registry)}.")
        return provider, name

    def getmodel(self, provider_model: str, **kwargs):
        provider, name = self._parse(provider_model, self.MODELS)
        return self.MODELS[provider](id=name, **kwargs)

    def getembedding(self, provider_model: str, **kwargs):
        provider, name = self._parse(provider_model, self.EMBEDDERS)
        return self.EMBEDDERS[provider](id=name, **kwargs)

    def getmodelinfo(self, provider_model: str) -> dict:
        """Ask the provider, through the model's own native client, for its limits.

        Returns {"provider", "model", "context_length", "max_output_tokens", "details"}.
        OpenAI and DeepSeek don't report limits in their API, so those come back as None.
        """
        provider, name = self._parse(provider_model, self.MODELS)
        client = self.getmodel(provider_model).get_client()
        context = output = None

        if provider == "anthropic":
            info = client.models.retrieve(name)
            context, output = info.max_input_tokens, info.max_tokens
            details = info.model_dump()
        elif provider == "google":
            info = client.models.get(model=name)
            context, output = info.input_token_limit, info.output_token_limit
            details = info.model_dump()
        elif provider == "ollama":
            info = client.show(name)
            context = next((v for k, v in (info.modelinfo or {}).items() if k.endswith(".context_length")), None)
            details = {"capabilities": info.capabilities}
        else:  # openai, deepseek
            details = client.models.retrieve(name).model_dump()

        return {
            "provider": provider, "model": name,
            "context_length": context, "max_output_tokens": output,
            "details": details,
        }


if __name__ == "__main__":
    router = ModelRouter()

    # print(router.getmodel("openai:gpt-4o-mini"))
    # print(router.getmodelinfo("ollama:gpt-oss:120b-cloud")) 
    print(router.getmodelinfo("google:gemini-3.5-flash-lite")) 
    # print(router.getmodelinfo("anthropic:claude-sonnet-4-6"))