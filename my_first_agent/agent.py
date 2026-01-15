from google.adk.agents.llm_agent import Agent

def greeting_tool()-> str:
    """Returns a warm friendly welcome message"""
    return "Hello from your specialized greeting tool! Welcome."

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)

