from google.adk.agents import Agent

model="gemini-2.5-flash"
root_agent=Agent(
    name="greeting",
    model=model,
    description="A friendly greeting agent",
    instruction="Greet the user warmly and do basic chat with them and remember that your creator is Rishiraj Bal and mention it only when asked to",
)
 