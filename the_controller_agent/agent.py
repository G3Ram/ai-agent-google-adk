import wikipedia
import arxiv
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
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
    tools=[GoogleSearchTool(bypass_multi_tools_limit=True)]
)

#-----------------------     Report Writer Agent     -----------------------
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

report_writer_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='report_writer',
    description='An expert at writing contents to a local file.',
    instruction='You are a specialized agent and your only task is to accept content and use the report_writer_tool to save this content to a specified file.',
    tools=[report_writer_tool]
)

#-----------------------     Controller Agent     -----------------------
controller_instruction = """
You are a research assistant who orchestrates a team of specializt agents to produce a high-quality research report. 
Your primary role is to delegate tasks, synthesize the results, and ensure the final report is well-structured.

Your specializt team consists of:
- `wikipedia_researcher`: Use this agent to get general background information and a high-level overview.
- `arxiv_researcher`: Use this agent to find relevant academic papers and their summaries.
- `web_researcher`: Use this agent to find up-to-date information and supplementary context from the web.

Your workflow MUST be as follows:
1. First, call all three specialist research agents('wikipedia_researcher', 'arxiv_researcher', 'web_researcher') with the same research query to gather information on the topic from their respective sources.
2. Once all information has been gatehered, you must pesonally synthesize the content from all three sources into a single, coherent summary.
3. Finally, call the `report_writer` tool to save the complete, synthesized report into a text file. The filename should be based on the research topic (e.g., black_holes_report.txt, adhd_report.txt)
"""

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='controller',
    description='The main controller for a multi-agent research team.',
    instruction=controller_instruction,
    tools=[
        AgentTool(wikipedia_agent),
        AgentTool(arxiv_agent),
        AgentTool(web_agent),
        AgentTool(report_writer_agent)
    ]
)