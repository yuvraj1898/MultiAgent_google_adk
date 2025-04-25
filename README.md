# 🧠 Multi-Agent Financial Assistant

A modular, AI-powered assistant designed to retrieve and process real-time financial data, news, and web content. Built using **Google Agent Development Kit (ADK)**, **LangChain**, **CrewAI**, and **Gemini models**, this assistant seamlessly integrates tools for search, scraping, and stock analytics.

---

## 🚀 Features

- 📈 Real-time stock price retrieval using Yahoo Finance via `yfinance`
- 📰 Finance news retrieval using `YahooFinanceNewsTool`
- 🔍 Web search using Brave Search
- 🕸️ Web scraping using `ScrapeWebsiteTool`
- 🤖 Agent orchestration using Google ADK and CrewAI
- 🧠 Coordinator agent that intelligently routes tasks to specialized sub-agents

---

## 📦 Tech Stack

- Python
- [LangChain](https://github.com/langchain-ai/langchain)
- [CrewAI](https://github.com/joaomdmoura/crewai)
- [Google Agent Development Kit (ADK)](https://github.com/google/agentic-development-kit)
- [yfinance](https://github.com/ranaroussi/yfinance)
- Brave Search API
- Gemini-2.0-flash (LLM)

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/multi-agent-financial-assistant.git
cd multi-agent-financial-assistant
```
### 2. Create & Activate Virtual Environment (Recommended)
```bash
python -m venv .venv
# Activate (each new terminal)
# macOS/Linux: source .venv/bin/activate
# Windows CMD: .venv\Scripts\activate.bat
# Windows PowerShell: .venv\Scripts\Activate.ps1
```
### 3. Install Dependencies

```bash
pip install langchain yfinance crewai_tools google-adk
```
### 4. Set Up Environment Variables
Create a .env file in the root directory and add your API keys:

```bash
GOOGLE_API_KEY=your_google_api_key
BRAVE_API_KEY=your_brave_api_key
```
### 5. Example Usage
Run the Assistant via Terminal
```bash
adk run multi_tool_agent
```
Run the Assistant via Web Interface

```bash
adk web
```

Open your browser at http://localhost:8000

Select multi_tool_agent from the dropdown in the top-left corner

Sample Query

User: What's the latest news on Tesla and its current stock price?
Coordinator Workflow:

Uses yf_agent to fetch Tesla news.

Uses stock_price_agent to get Tesla's current stock price.

Combines and presents both results.

📚 Project Structure

multi-agent-financial-assistant/
├── multi_tool_agent/
│   ├── __init__.py
│   └── agent.py
├── .env
├── requirements.txt
└── README.md
💡 Use Cases
LLM-powered financial dashboards

Automated research assistants

Slack/Notion finance bots

Portfolio monitoring & news alerts



