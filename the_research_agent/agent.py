import wikipedia
from google.adk.agents.llm_agent import Agent

def wikipedia_tool(query: str) -> str:
    """
    Search Wikipedia for the given query and return a summary of top results.
    
    Args:        
        query (str): The search query to look up on Wikipedia.
    """
    
    try:
        # the summary method automatically finds the best-matching page
        # and returns a summary of it.
        summary = wikipedia.summary(query)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # handle cases where a query is ambiguous (e.g., "Mercury")
        return f"The query '{query}' is ambiguous. Please be more specific. Possible options include: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        # handle cases where the page does not exist
        return f"Sorry, I could not find a Wikipedia page for '{query}'."
    except Exception as e:
        return f"An unexpected error occurred while searching Wikipedia: {str(e)}"


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
