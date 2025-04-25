from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from google.adk.tools.langchain_tool import LangchainTool
from google.adk.agents import Agent
from crewai_tools import ScrapeWebsiteTool
from google.adk.tools.crewai_tool import CrewaiTool
from google.adk.agents import LlmAgent, BaseAgent
from crewai_tools import BraveSearchTool
import yfinance as yf
# Initialize the tool for internet searching capabilities



# Create the Wikipedia tool properly

y_tool = YahooFinanceNewsTool()
wrapped_Y_tool = LangchainTool(tool=y_tool)
b_ytool = BraveSearchTool()
wrapped_b_tool = CrewaiTool(
    name="search_for_content",          # ✅ valid
    description="Searches the internet and returns links.",
    tool=b_ytool
)

s_tool = ScrapeWebsiteTool()
scrape_tool = CrewaiTool(
    name="Scrape_any_website",
    description="scrape the given links",
    tool=s_tool
)

def get_stock_price(symbol: str):
    """
    Retrieves the current stock price for a given symbol.

    Args:
        symbol (str): The stock symbol (e.g., "AAPL", "GOOG").

    Returns:
        float: The current stock price, or None if an error occurs.
    """
    try:
        stock = yf.Ticker(symbol)
        historical_data = stock.history(period="1d")
        if not historical_data.empty:
            current_price = historical_data['Close'].iloc[-1]
            return current_price
        else:
            return None
    except Exception as e:
        print(f"Error retrieving stock price for {symbol}: {e}")
        return None


stock_price_agent = Agent(
    model='gemini-2.0-flash',
    name='stock_agent',
    instruction= 'You are an agent who retrieves stock prices. If a ticker symbol is provided, fetch the current price. If only a company name is given, first perform a Google search to find the correct ticker symbol before retrieving the stock price. If the provided ticker symbol is invalid or data cannot be retrieved, inform the user that the stock price could not be found.',
    description='This agent specializes in retrieving real-time stock prices. Given a stock ticker symbol (e.g., AAPL, GOOG, MSFT) or the stock name, use the tools and reliable data sources to provide the most up-to-date price.',
    tools=[get_stock_price],
)

# Create the agent
yf_agent = Agent(
    name="langchain_tool_agent",
    model="gemini-2.0-flash",
    description="Agent to get information from yahoo finance",
    instruction="I can answer your questions related to finance using yahoo finance",
    tools=[wrapped_Y_tool]
)
g_agent = Agent(
    name="basic_search_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions using brave Search. get the links",
    instruction="I can answer your questions by searching the internet. and provide just the links",
    # google_search is a pre-built tool which allows the agent to perform Google searches.
    tools=[wrapped_b_tool]
)
s_agent= Agent(
     name="scrape_tool_agent",
    model="gemini-2.0-flash",
    description="Agent to scrape data from given links",
    instruction="I can scrape data from given links",
    tools=[scrape_tool]
)
root_agent = LlmAgent(
    name="Coordinator",
    model="gemini-2.0-flash",
    description="I coordinate search,yahoo finace news,scrape  agent.",
    sub_agents=[ # Assign sub_agents here
        yf_agent,
        g_agent,
        s_agent,
        stock_price_agent
    ]
)