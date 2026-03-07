from google.adk.agents.llm_agent import Agent
from google.genai import types
from pydantic import BaseModel, Field

# def greeting_tool()-> str:
#     """Returns a warm friendly welcome message"""
#     return "Hello from your specialized greeting tool! Welcome."

class GreetingRequest(BaseModel):
    """Input schema for specifying the language of the greeting."""
    language: str = Field(description="The language to greet the user in.")

class GreetingResponse(BaseModel):
    """Output schema for the greeting message."""
    greeting_message: str = Field(description="The final, formatted greeting message.")
    

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='You are a friendly agent. Greet the user in their specified language. ',
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=250,
        # input_schema=GreetingRequest,
        # output_schema=GreetingResponse,
        # output_key="final_greeting",
        # include_contents = 'none', # It will be a fresh conversation. History will not be included in the input.
        safety_settings=[types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        )]
    )
)

