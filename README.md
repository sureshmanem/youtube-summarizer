# YouTube Video Summarizer with LM Studio

This project summarizes YouTube videos locally using LM Studio and open-source LLMs. It extracts transcripts via captions or audio transcription (OpenAI Whisper) and generates concise summaries using LangChain prompt templates. Models are listed, loaded and unloaded from the app's sidebar via the LM Studio SDK.

## Setup & Usage

1. Install LM Studio ([https://lmstudio.ai](https://lmstudio.ai)) and make sure the `lms` CLI is on your PATH.
2. Install dependencies:
```
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Download a model (check the exact key with `lms ls`):
```
lms get <model-name>
```

4. Start the LM Studio server:
```
lms server start
```

5. Launch the app:
```
streamlit run app.py
```

Pick a model and context length in the sidebar. The model is loaded automatically when you summarize, or use **Load** / **Unload** to manage it yourself.

## Configuration

Optional environment variables:

| Variable | Default | Purpose |
|---|---|---|
| `LMSTUDIO_BASE_URL` | `http://localhost:1234/v1` | OpenAI-compatible endpoint used for summaries |
| `LMSTUDIO_HOST` | `localhost:1234` | Host used by the LM Studio SDK for model management |
| `LMSTUDIO_MODEL` | first loaded/downloaded model | Default model in the sidebar |
| `LMSTUDIO_CONTEXT_LENGTH` | `16384` | Context length used when loading a model |

Long videos need a larger context length; raise it if summaries look cut off.

`yt-dlp` and `ffmpeg` are needed for videos without captions (audio is transcribed with Whisper).

## Credits & License

This project is a fork of [youtube-summarizer-ollama](https://github.com/AusaafAhmad/youtube-summarizer-ollama) by Ausaaf Ahmad, migrated from Ollama to LM Studio (see `migrationplan.md`). See the Medium article for the original architecture:
[How I Built a YouTube Summarizer Using Ollama](https://medium.com/p/86bbb3194b6c).

Released under the MIT License; see `LICENSE`.
