from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from google.adk.tools.langchain_tool import LangchainTool
from google.adk.agents import Agent

# Create the Wikipedia tool properly
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_wrapper)

# Wrap the tool for ADK
wiki_tool = LangchainTool(tool=wikipedia_tool)

# Create the agent
root_agent = Agent(
    name="langchain_tool_agent",
    model="gemini-2.0-flash",
    description="Agent to get information from Wikipedia",
    instruction="I can answer your questions using Wikipedia as a knowledge source",
    tools=[wiki_tool]
)