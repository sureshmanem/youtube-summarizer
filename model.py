from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from config import LMSTUDIO_BASE_URL

template = """
You are an AI Assistant. Summarize the following youtube video transcript in the following format:
- Name of Channel: (only if it's directly mentioned like this is <name>, I'm <name> etc)
- A short title of the summary
- Main Summary in keypoints (bold important points)
- Final conclusion of the video: (if any)

{transcript}
"""

prompt = ChatPromptTemplate.from_template(template)


def strip_reasoning(text: str) -> str:
    # Reasoning models (e.g. deepseek-r1, qwen3) may emit <think>...</think> before the answer
    return text.split("</think>")[-1].strip()


def summarize(transcript: str, model: str) -> str:
    # LM Studio ignores the API key, but the OpenAI client requires one
    llm = ChatOpenAI(base_url=LMSTUDIO_BASE_URL, api_key="lm-studio", model=model, temperature=0.3)
    chain = prompt | llm | StrOutputParser()
    return strip_reasoning(chain.invoke({"transcript": transcript}))
