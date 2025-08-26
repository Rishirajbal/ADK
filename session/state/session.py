#Example usage of sessions
import asyncio
from google.adk.sessions import InMemorySessionService, Session

async def main():
    temp = InMemorySessionService()
    session = await temp.create_session(
        app_name="my_app",
        user_id="1234",
        state={"initial_key": "initial_value"},
    )

    print("Examining session values")
    print(f"session.app_name: {session.app_name}")
    print(f"session.user_id: {session.user_id}")
    print(f"session.state: {session.state}")
    print(f"events: {session.events}")
    print(f"session.last_update_time: {session.last_update_time}")

if __name__ == "__main__":
    asyncio.run(main())
