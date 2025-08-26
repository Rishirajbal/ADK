import uuid
import asyncio
from dotenv import load_dotenv
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from question_answering_agent import question_answering_agent


load_dotenv(dotenv_path=r"C:\Users\KIIT\OneDrive\Desktop\adk\session\state\.env")

# Session service
session_service_stateful = InMemorySessionService()

# Initial state
initial_state = {
    "user_name": "Rishiraj Bal",
    "user_preferences": "I like to play CODM and listen to music, I am a GenAI developer",
}

# App + session info
app_name = "BrahmNET"
user_id = "1234"
session_id = str(uuid.uuid4())

# ✅ Run async create_session synchronously
session = asyncio.run(session_service_stateful.create_session(
    app_name=app_name,
    user_id=user_id,
    session_id=session_id,
    state=initial_state,
))

print(f"Created new session: {session_id}")

# Runner
runner = Runner(
    agent=question_answering_agent,
    app_name=app_name,
    session_service=session_service_stateful,
)

# New user message
new_message = types.Content(
    role="user",
    parts=[types.Part(text="What is my name?")]
)

# Runner.run is sync → normal for loop
for event in runner.run(
    user_id=user_id,
    session_id=session_id,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final response received: {event.content.parts[0].text}")
