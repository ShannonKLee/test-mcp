from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Test MCP")

@mcp.tool()
def concat_str(str1: str, str2: str) -> str:
    return str1 + str2

@mcp.tool()
def hello_person(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool()
def hello_world():
    return "Hello World!"

def main():
    """Main entry point for the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
