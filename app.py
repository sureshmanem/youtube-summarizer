import streamlit as st
import Transcript
import lmstudio_models
from model import summarize
from config import LMSTUDIO_MODEL, LMSTUDIO_CONTEXT_LENGTH


st.header("Youtube Video Summmarizer")

if not lmstudio_models.server_available():
    st.error("LM Studio server not running. Start it with `lms server start`.")
    st.stop()

with st.sidebar:
    st.header("Model (LM Studio)")
    models = lmstudio_models.list_models()
    if not models:
        st.warning("No models downloaded. Download one with `lms get <model>`.")
        st.stop()

    loaded = lmstudio_models.loaded_models()
    default = LMSTUDIO_MODEL if LMSTUDIO_MODEL in models else next((m for m in models if m in loaded), models[0])
    selected = st.selectbox("Model", models, index=models.index(default))
    context_length = st.number_input("Context length", min_value=2048, max_value=262144,
                                     value=LMSTUDIO_CONTEXT_LENGTH, step=2048)

    col1, col2 = st.columns(2)
    if col1.button("Load", use_container_width=True):
        with st.spinner(f"Loading {selected}..."):
            lmstudio_models.ensure_loaded(selected, int(context_length))
        st.rerun()
    if col2.button("Unload", use_container_width=True, disabled=selected not in loaded):
        lmstudio_models.unload(selected)
        st.rerun()

    st.caption("Loaded models")
    if loaded:
        for identifier, ctx in loaded.items():
            st.markdown(f"- `{identifier}` (context {ctx})")
    else:
        st.markdown("_None_")

    st.divider()
    st.header("About This App")
    st.markdown("""

        Made by Suresh Manem
        """)

with st.form("root"):
    link = st.text_input("Paste Youtube Video Link Here")
    submitted = st.form_submit_button()



if submitted and link:
    transcript = Transcript.get_transcript(link)
    with st.spinner(f"Summarizing with {selected}..."):
        model_id = lmstudio_models.ensure_loaded(selected, int(context_length))
        summary = summarize(transcript, model_id)
    st.header("Summary")
    st.write(summary)
    st.header("Transcript")
    st.write(transcript)
