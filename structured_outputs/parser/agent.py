from pydantic import BaseModel,Field
class email(BaseModel):
    subject: str = Field(..., description="Subject of the email")
    body: str = Field(..., description="Body of the email")

from google.adk.agents import LlmAgent
model="gemini-2.5-flash"

root_agent=LlmAgent(
    model=model,
    name="parser",
    description="An agent which generates email responses.",
    instruction="""write an email as per user's requests.
    **IMPORTANT**->your response must be valid JSON matching this structure:
    {
        "subject": "Email Subject",
        "body": "Email Body"
    }""",
    input_schema=email,
    output_schema=email,
    output_key="email",

)