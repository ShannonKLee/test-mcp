from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Test MCP")

@mcp.tool()
def hello_world():
    return "Hello World!"

def main():
    """Main entry point for the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
