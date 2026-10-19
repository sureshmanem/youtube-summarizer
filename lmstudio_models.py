import lmstudio as lms
from config import LMSTUDIO_HOST


def server_available() -> bool:
    return lms.Client.is_valid_api_host(LMSTUDIO_HOST)


def list_models() -> list[str]:
    with lms.Client(LMSTUDIO_HOST) as client:
        return sorted(m.model_key for m in client.llm.list_downloaded())


def loaded_models() -> dict[str, int]:
    """Loaded model identifiers mapped to their context length."""
    with lms.Client(LMSTUDIO_HOST) as client:
        return {m.identifier: m.get_context_length() for m in client.llm.list_loaded()}


def ensure_loaded(model_key: str, context_length: int) -> str:
    """Load model_key with the given context length (reloading if it differs). Returns its identifier."""
    with lms.Client(LMSTUDIO_HOST) as client:
        for m in client.llm.list_loaded():
            if m.identifier == model_key:
                if m.get_context_length() == context_length:
                    return m.identifier
                m.unload()
        model = client.llm.load_new_instance(model_key, config={"contextLength": context_length})
        return model.identifier


def unload(identifier: str) -> None:
    with lms.Client(LMSTUDIO_HOST) as client:
        client.llm.unload(identifier)
