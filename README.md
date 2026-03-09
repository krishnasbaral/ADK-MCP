# ADK-MCP

A collection of **MCP (Model Context Protocol) servers and AI agents** built using **ADK** to extend AI capabilities with external tools such as Google Search, Google Maps, Google Sheets, and Python execution.

This repository demonstrates how MCP servers can be used to connect LLM agents with real-world tools and services.

---

# 📂 Repository Structure

```
ADK-MCP
│
├── adk_mcp_gmaps       # MCP server for Google Maps integration
├── first_agent         # Google Search AI Agent
├── gsheets_mcp         # MCP server for Google Sheets operations
├── python_executor     # MCP server to execute Python code
└── workspace_mcp       # MCP server for workspace/file operations
```

Each folder contains an MCP server or agent that can be connected to an LLM application.

---

# 🤖 Agents

## 1️⃣ Google Search Agent (`first_agent`)

This agent allows an LLM to **perform Google searches and retrieve information from the internet**.

### Features

- Perform real-time Google searches
- Retrieve relevant search results
- Assist AI systems with up-to-date information
- Useful for **RAG pipelines and knowledge retrieval**

### Example Use Case

User Query:

```
What is the capital of France?
```

Agent Flow:

```
User Query → Google Search Agent → Google Search → Results returned to LLM
```

---

# 🧩 MCP Servers

## 📍 Google Maps MCP (`adk_mcp_gmaps`)

Provides access to **Google Maps functionality**.

Capabilities may include:

- Place search
- Location lookup
- Map-based queries

---

## 📊 Google Sheets MCP (`gsheets_mcp`)

Enables interaction with **Google Sheets**.

Possible operations:

- Read sheet data
- Write data
- Update records
- Automate spreadsheet workflows

---

## 🐍 Python Executor MCP (`python_executor`)

Allows an AI agent to **execute Python code dynamically**.

Features:

- Run Python scripts
- Perform calculations
- Process data
- Execute custom logic

---

## 🏢 Google Workspace MCP (`workspace_mcp`)

This module connects the agent with **Google Workspace services** using the `workspace-mcp` server.

### Supported Services

- Google Drive
- Google Sheets
- Gmail
- Google Calendar
- Google Docs

### Example Capabilities

The AI agent can:

- Send or read Gmail messages
- Manage Google Drive files
- Read or update Google Sheets
- Create calendar events
- Access Google Docs

### Agent Configuration Example

```python
root_agent = Agent(
    name="workspace_agent",
    model="gemini-2.5-flash",
    instruction="Use Google Workspace tools to manage Drive, Sheets, Gmail, Calendar and Docs.",
)

# ⚙️ Requirements

- Python 3.9+
- ADK
- MCP compatible environment

Install dependencies:

```bash
pip install -r requirements.txt
```

---


# 🔗 How MCP Works

MCP allows AI agents to interact with external tools.

```
User Query
     │
     ▼
LLM Agent
     │
     ▼
MCP Tool
     │
     ▼
External Service
(Google Search / Maps / Sheets / Python)
```

The response is then returned back to the agent.

---

# 💡 Example Applications

This repository can be used to build:

- AI research assistants
- AI copilots with tool access
- RAG systems with live internet search
- Data automation agents
- Developer AI assistants

---


# 👨‍💻 Author

Krushna S. Baral

---

# 📄 License

This project is open-source and available under the MIT License.
