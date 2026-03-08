from google.adk.agents.llm_agent import Agent
from google.adk.planners import BuiltInPlanner, PlanReActPlanner
from google.genai import types
from pydantic import BaseModel, Field

# def greeting_tool()-> str:
#     """Returns a warm friendly welcome message"""
#     return "Hello from your specialized greeting tool! Welcome."

# class GreetingRequest(BaseModel):
#     """Input schema for specifying the language of the greeting."""
#     language: str = Field(description="The language to greet the user in.")

# class GreetingResponse(BaseModel):
#     """Output schema for the greeting message."""
#     greeting_message: str = Field(description="The final, formatted greeting message.")

def create_greeting(name: str, language: str = "English") -> str:
    """Creates a personalized greeting for a user in a specified language.

    Args:
        name (str): The name of the person to greet.
        language (str): The language for the greeting. Defaults to English.
    """
    if language.lower() == "spanish":
        return f"Hola, {name}! Cómo estás?"
    else:
        return f"Hello, {name}! How are you?"
    

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='You are a friendly agent. When the user asks for a greeting, use the 'create_greeting' tool to generate it.',
    tools=[create_greeting, google_search],
    # generate_content_config=types.GenerateContentConfig(
    #     temperature=0.2,
    #     max_output_tokens=250,
    #     input_schema=GreetingRequest,
    #     output_schema=GreetingResponse,
    #     output_key="final_greeting",
    #     include_contents = 'none', # It will be a fresh conversation. History will not be included in the input.
    #     planner=BuiltInPlanner(
    #         thinking_config=types.ThinkingConfig(
    #             include_thoughts=True,
    #             thinking_budget=1024
    #         )
    #     ),
    #     safety_settings=[types.SafetySetting(
    #         category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
    #         threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    #     )]
    # )
)

