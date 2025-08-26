from google.adk.agents import Agent
from google.adk.tools import google_search

model="gemini-2.5-flash"

root_agent=Agent(
    model=model,
    name="websearch",
    description="A web search agent that can perform searches and return results.",
    instruction="""You are a web search agent. When asked a question you will answer it ,and if asked to search the web you will perform a Google search and return the top result. If the user asks for more details, you will provide a summary of the information found.
    """,
    tools=[google_search],
    
)