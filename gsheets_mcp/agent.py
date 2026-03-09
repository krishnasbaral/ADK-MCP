from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
import os

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful SQL database assistant',
    instruction='Help users query and explore their SQL Server database',
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='mssql-mcp',
                    args=["--stdio"],
                    env={
                        "MSSQL_SERVER": os.environ.get("MSSQL_SERVER", ""),
                        "MSSQL_DATABASE": os.environ.get("MSSQL_DATABASE", ""),
                        "MSSQL_USER": os.environ.get("MSSQL_USER", ""),
                        "MSSQL_PASSWORD": os.environ.get("MSSQL_PASSWORD", ""),
                        "MSSQL_ENCRYPT": "true",
                        "MSSQL_ACCESS_MODE": "readonly",
                        "PATH": os.environ.get("PATH", ""),
                        "APPDATA": os.environ.get("APPDATA", ""),
                        "USERPROFILE": os.environ.get("USERPROFILE", ""),
                    }
                ),
            ),
        )
    ],
)