from google.adk.agents.llm_agent import Agent

def greeting_tool()-> str:
    """Returns a warm friendly welcome message"""
    return "Hello from your specialized greeting tool! Welcome."

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='You are a friendly agent. When the user greets you, you MUST use the greeting_tool to respond. ',
    tools=[greeting_tool]
)

