import wikipedia
import arxiv
from google.adk.agents import LlmAgent
from google.adk.tools.google_search_tool import GoogleSearchTool

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


def report_writer_tool(content: str, filename: str) -> str:
    """
    Writes the given content to a local file. Appends if the file already exists. 

    Args:
        content (str): The text content to write to the file.
        filename (str): The name of the file to save the content in (e.g., 'report.txt').
    """
    try:
        # use 'a' for append mode. This will create the file if it does not exist,
        # or add to the end of it if it does exist.
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(content + "\n")
        return f"Successfully appended content to {filename}."
    except Exception as e:
        return f"An error occurred while writing to the file: {str(e)}"

instruction = """
You are a helpful and diligent research assistant. Your goal is to produce a brief research report on a given topic.

You MUST follow these steps in order:
1. First, gather background information on the topic using the wikipedia_tool.
2. Next, find relevant academic papers using the arxiv_tool.
3. Then, find supplementary web articles using the google_search tool.
4. Finally, synthesize all the information you have gathered from all sources into a coherent report
    and use the report_writer_tool to save this complete report to a file named 'report.txt'.
"""
root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='research_assistant',
    description='A research assistant that gathers information from Wikipedia, arXiv and Google Search to create a summary report on a given topic.',
    instruction=instruction,
    tools=[
        wikipedia_tool,
        arxiv_tool,
        GoogleSearchTool(bypass_multi_tools_limit=True),
        report_writer_tool
    ]
)
