from mcp.server.fastmcp import FastMCP
import io
import contextlib
import traceback

# Initialize MCP server
mcp = FastMCP("Python Execution MCP")


@mcp.tool()
async def execute_python(code: str) -> str:
    """
    Execute Python code and return the output.

    The code should be valid Python.
    Any printed output will be returned.
    """

    output_buffer = io.StringIO()

    try:
        # Capture print output
        with contextlib.redirect_stdout(output_buffer):
            exec(code, {})

        output = output_buffer.getvalue()

        if output.strip() == "":
            return "Code executed successfully (no output)"

        return output

    except Exception as e:
        return f"Error executing code:\n{traceback.format_exc()}"


if __name__ == "__main__":
    mcp.run()