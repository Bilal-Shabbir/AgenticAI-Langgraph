import requests
from fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("LocalToolServer")

@mcp.tool()
def add_numbers(a: float, b: float) -> dict:
    """Adds two numbers together."""
    return {"operation": "addition", "a": a, "b": b, "result": a + b}

@mcp.tool()
def subtract_numbers(a: float, b: float) -> dict:
    """Subtracts the second number (b) from the first number (a)."""
    return {"operation": "subtraction", "a": a, "b": b, "result": a - b}

@mcp.tool()
def multiply_numbers(a: float, b: float) -> dict:
    """Multiplies two numbers."""
    return {"operation": "multiplication", "a": a, "b": b, "result": a * b}

@mcp.tool()
def divide_numbers(a: float, b: float) -> dict:
    """Divides the first number (a) by the second number (b)."""
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"operation": "division", "a": a, "b": b, "result": a / b}

@mcp.tool()
def get_stock_price(symbol: str) -> dict:
    """
    Fetch latest stock price for a given symbol (e.g. 'AAPL', 'TSLA')
    Using Alpha Vantage.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=F5GC4D602BKWMO8B"
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": f"Failed to fetch stock data: {str(e)}"}

if __name__ == "__main__":
    mcp.run()