from google.adk.agents.llm_agent import Agent
from google.genai import types
from pydantic import BaseModel, Field

# def greeting_tool()-> str:
#     """Returns a warm friendly welcome message"""
#     return "Hello from your specialized greeting tool! Welcome."

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='You are a friendly agent. Greet the user in their specified language. ',
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=250,
        safety_settings=[types.SafetySetting(
            category=types.SafetySetting.Category.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        )]
    )
)

