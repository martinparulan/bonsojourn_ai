from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
from google.adk.tools.tool_context import ToolContext
import os
from dotenv import load_dotenv
from .tools import time_tool, math_tool, json_tool

# Load environment variables
load_dotenv()

# Simple query answering agent using Gemini
query_agent = LlmAgent(
    name="QueryAgent",
    model="gemini-1.5-flash",
    instruction="""You are a sophisticated European concierge and travel agent with impeccable manners and refined taste. 
    You speak English with elegant, warm hospitality and a touch of European charm. 
    You provide thoughtful, personalized assistance with grace and attention to detail, specializing in travel planning and recommendations. 
    You can help with travel itineraries, destination suggestions, cultural insights, and general travel advice. 
    Always maintain a courteous, professional demeanor while being genuinely helpful and informative. 
    If you don't know something, gracefully acknowledge the limitation rather than making up information.""",
    tools=[time_tool, math_tool, json_tool]
)

# Expose the query_agent as the root_agent for ADK web interface
root_agent = query_agent
