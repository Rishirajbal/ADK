from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import Agent
import os
from dotenv import load_dotenv
import litellm


load_dotenv(dotenv_path=r"path")
api_key = os.getenv("HUGGINGFACE_API_KEY")

if not api_key:
    raise ValueError("HUGGINGFACE_API_KEY not found. Please check your .env file.")

#just a conceptual code ADK does not work with open-source models as of now for that use langchain
model = LiteLlm(
    model="openai/gpt-oss-120b:groq",
    api_key=api_key,
    api_base="https://router.huggingface.co/v1"
)

root_agent = Agent(
    model=model,
    name="llm",
    description="A chat assistant",
    instruction="Answer the user's questions to the best of your ability.",
)
