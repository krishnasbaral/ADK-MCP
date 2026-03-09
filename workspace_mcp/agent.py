from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
import os

root_agent = Agent(
    name="workspace_agent",
    model="gemini-2.5-flash",
    instruction="Use Google Workspace tools to manage Drive, Sheets, Gmail, Calendar and Docs.",
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="workspace-mcp",   # <-- this is what you installed
                    args=[],                  # no args needed
                    env={
                        "GOOGLE_OAUTH_CLIENT_ID": os.environ["GOOGLE_OAUTH_CLIENT_ID"],
                        "GOOGLE_OAUTH_CLIENT_SECRET": os.environ["GOOGLE_OAUTH_CLIENT_SECRET"],
                        "OAUTHLIB_INSECURE_TRANSPORT": "1"
                    }
                )
            )
        )
    ]
)