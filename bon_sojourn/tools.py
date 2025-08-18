from google.adk.tools import FunctionTool
from google.adk.tools.tool_context import ToolContext
import datetime
import json

def get_current_time() -> str:
    """Get the current date and time"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_simple_math(expression: str) -> str:
    """Perform simple mathematical calculations"""
    try:
        # Basic safety - only allow simple math operations
        allowed_chars = set('0123456789+-*/(). ')
        if not all(c in allowed_chars for c in expression):
            return "Error: Only basic math operations (+, -, *, /, parentheses) are allowed"
        
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error calculating: {str(e)}"

def format_json(data: str) -> str:
    """Format JSON data for better readability"""
    try:
        parsed = json.loads(data)
        return json.dumps(parsed, indent=2)
    except Exception as e:
        return f"Error formatting JSON: {str(e)}"

# Create tool instances
time_tool = FunctionTool(get_current_time)
math_tool = FunctionTool(calculate_simple_math)
json_tool = FunctionTool(format_json)
