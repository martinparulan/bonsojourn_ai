from google.adk.tools import FunctionTool
from google.adk.tools.tool_context import ToolContext
import datetime
import json
import random

def get_current_time() -> str:
    """Get the current date and time in European format"""
    return datetime.datetime.now().strftime("%d %B %Y, %H:%M")

def calculate_simple_math(expression: str) -> str:
    """Perform simple mathematical calculations for travel planning"""
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

def get_seasonal_recommendations() -> str:
    """Get luxury travel recommendations based on current season"""
    current_month = datetime.datetime.now().month
    
    seasons = {
        (12, 1, 2): "Winter: Alpine ski resorts, Christmas markets, thermal spas, and cozy chalet experiences",
        (3, 4, 5): "Spring: Tulip festivals, wine regions awakening, Mediterranean coastal escapes, and cultural city breaks",
        (6, 7, 8): "Summer: French Riviera, Italian lakes, Greek islands, and exclusive summer festivals",
        (9, 10, 11): "Autumn: Wine harvest experiences, cultural festivals, and Mediterranean shoulder season luxury"
    }
    
    for months, recommendation in seasons.items():
        if current_month in months:
            return recommendation
    
    return "Year-round luxury experiences available across Europe"

def get_luxury_accommodation_types() -> str:
    """Get curated luxury accommodation recommendations"""
    return """Luxury Accommodation Options:
- Historic palaces and châteaux
- Boutique 5-star hotels with Michelin-starred restaurants
- Private villas with personal chefs
- Exclusive resort properties
- Heritage hotels with royal connections
- Private islands and estates"""

# Create tool instances
time_tool = FunctionTool(get_current_time)
math_tool = FunctionTool(calculate_simple_math)
json_tool = FunctionTool(format_json)
seasonal_tool = FunctionTool(get_seasonal_recommendations)
accommodation_tool = FunctionTool(get_luxury_accommodation_types)
