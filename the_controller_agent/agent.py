import wikipedia
import arxiv
from google.adk.agents import LlmAgent
from google.adk.tools.google_search_tool import GoogleSearchTool


#-----------------------     Wikipedia Agent     -----------------------
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

wikipedia_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='wikipedia_researcher',
    description='An expert at finding and summarizing information from Wikipedia.',
    instruction='You are a specialized agent and your only task is to accept a research query and use the wikipedia_tool to find relevant information about the query.',
    tools=[wikipedia_tool]
)

#-----------------------     arXiv Agent     -----------------------
def arxiv_tool(query: str) -> str:
    """
    Search arXiv repository for academic papers matching a query.

    Args:
        query (str): The topic to search for academic papers on arXiv.
    """
    try:
        # create a client to interact with the arXiv API
        client = arxiv.Client()

        # define the search parameters
        search = arxiv.Search(
            query=query,
            max_results=3,
            sort_by=arxiv.SortCriterion.Relevance
        )

        results = []
        for result in client.results(search):
            results.append(f"Title: {result.title}\nSummary: {result.summary}\nURL: {result.entry_id}")
        
        if not results:
            return f"No papers found on arXiv for the query '{query}'."
        
        return "\n-------\n".join(results)
    
    except Exception as e:
        return f"An error occurred while searching arXiv: {str(e)}"


arxiv_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='arxiv_researcher',
    description='An expert at finding and summarizing academic papers from arXiv.',
    instruction='You are a specialized agent and your only task is to accept a research query and use the arxiv_tool to find relevant academic papers.',
    tools=[arxiv_tool]
)

#-----------------------     Web Agent     -----------------------

web_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='web_researcher',
    description='An expert at finding and summarizing information from the web.',
    instruction='You are a specialized agent and your only task is to accept a research query and use the google_search_tool to find relevant information from the web.',
    tools=[GoogleSearchTool()]
)
