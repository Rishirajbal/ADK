from google.adk.agents import Agent

model = "gemini-2.5-flash"

question_answering_agent = Agent(
    name="question_answering_agent",
    model=model,
    description="A friendly question answering agent",
    instruction="""Answer the user's questions accurately and remember that your creator is Rishiraj Bal and mention it only when asked to
    some info regarding user_name:{user_name} , user_preferences:{user_preferences}""",
)

