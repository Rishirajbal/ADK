from datetime import datetime
from google.adk.agents.callback_context import CallbackContext
from google.adk.agents import LlmAgent
from typing import Optional
from google.genai import types


def before(callback_context: CallbackContext) -> Optional[types.Content]:
    """This callback is used to logs when the agent starts a request"""
    state=callback_context.state
    timestamp=datetime.now()

    if "agent_name" not in state:
        state["agent_name"]="BrahmNET"

    if "request_counter" not in state:
        state["request_counter"]=1
    else:
        state["request_counter"]+=1

    state["request_start_time"]=timestamp

    print(f"Agent {state['agent_name']} started request {state['request_counter']} at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    return None

def after(callback_context: CallbackContext) -> Optional[types.Content]:
    """This callback is used to logs when the agent finishes a request"""
    state=callback_context.state
    timestamp=datetime.now()

    agent_name=state.get("agent_name", "Unknown")
    request_counter=state.get("request_counter", "Unknown")

    seconds_str="Unknown"
    if "request_start_time" in state and state["request_start_time"] is not None:
        duration=timestamp - state["request_start_time"]
        seconds_str=f"{duration.total_seconds():.2f}"

    print(
        f"Agent {agent_name} finished request {request_counter} in {seconds_str} seconds at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
    )

    return None


root_agent=LlmAgent(
    model="gemini-2.5-flash",
    name="before_after_agent",
    description="This agent is used to log the start and end of a request",
    instruction="You are a helpful assistant that logs the start and end of a request",
    before_agent_callback=before,
    after_agent_callback=after,)