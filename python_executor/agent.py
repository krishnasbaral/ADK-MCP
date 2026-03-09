import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters

# 1. Locate your server file dynamically
current_dir = os.path.dirname(__file__)
server_path = os.path.join(current_dir, "mcp_server.py")

# 2. Setup the toolset to run your script as a subprocess
python_toolset = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="python",
            args=[server_path],
            env=dict(os.environ),
        )
    )
)

# 3. Define the agent for ADK-Web to use
root_agent = Agent(
    model='gemini-2.0-flash',
    name='PythonExecutorAgent',
    instruction="You are a code assistant. Use 'execute_python' for math/logic.",
    tools=[python_toolset]
)