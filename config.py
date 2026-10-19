import os

# OpenAI-compatible endpoint used for inference
LMSTUDIO_BASE_URL = os.getenv("LMSTUDIO_BASE_URL", "http://localhost:1234/v1")
# Host used by the lmstudio SDK for model management
LMSTUDIO_HOST = os.getenv("LMSTUDIO_HOST", "localhost:1234")
# Default model key; empty means pick the first loaded/downloaded model
LMSTUDIO_MODEL = os.getenv("LMSTUDIO_MODEL", "")
# Context length used when loading a model (transcripts can be long)
LMSTUDIO_CONTEXT_LENGTH = int(os.getenv("LMSTUDIO_CONTEXT_LENGTH", "16384"))
