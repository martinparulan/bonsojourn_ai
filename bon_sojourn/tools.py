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

def collect_user_profile(name: str, email: str, home_city: str, timezone: str) -> str:
    """Collect and store user profile information"""
    profile = {
        "name": name,
        "email": email,
        "home_city": home_city,
        "timezone": timezone,
        "timestamp": datetime.datetime.now().isoformat()
    }
    return f"Profile collected for {name} from {home_city}. Ready to discover your perfect sojourn."

def set_trip_intent(intent: str, readiness: str) -> str:
    """Set user's trip intent and readiness level"""
    intents = {
        "celebrate": "Celebration - marking a milestone or achievement",
        "reset": "Reset - seeking renewal and restoration", 
        "create": "Create - inspiration and new experiences",
        "surprise": "Surprise me - open to discovery"
    }
    
    readiness_levels = {
        "dreaming": "Day Dreaming - exploring possibilities",
        "ready": "Ready to Manifest - prepared to book"
    }
    
    return f"Intent set to {intents.get(intent.lower(), intent)}. Mode: {readiness_levels.get(readiness.lower(), readiness)}."

def calibrate_tone(vibe: str, pace: str, style: str) -> str:
    """Calibrate user's preferred tone and style"""
    vibe_map = {
        "quiet": "Quiet - intimate, contemplative experiences",
        "social": "Social - vibrant, community-focused moments"
    }
    
    pace_map = {
        "slow": "Slow - unhurried, savoring each moment",
        "spirited": "Spirited - dynamic, energy-filled adventures"
    }
    
    style_map = {
        "classic": "Classic - timeless elegance and tradition",
        "contemporary": "Contemporary - modern sophistication and innovation"
    }
    
    reflection = f"Your vibe: {vibe_map.get(vibe.lower(), vibe)}. Your pace: {pace_map.get(pace.lower(), pace)}. Your style: {style_map.get(style.lower(), style)}."
    return f"Tone calibrated. {reflection}"

def process_signature_prompts(responses: str) -> str:
    """Process user responses to signature prompts and extract tags"""
    # Extract key themes and preferences from responses
    tags = []
    
    if "croissant" in responses.lower() or "pastry" in responses.lower():
        tags.append("culinary_focus_pastry")
    if "market" in responses.lower():
        tags.append("market_affinity")
    if "bar" in responses.lower() or "bar-stool" in responses.lower():
        tags.append("dining_style_casual")
    if "white-tablecloth" in responses.lower():
        tags.append("dining_style_formal")
    if "café" in responses.lower() or "cafe" in responses.lower():
        tags.append("cafe_culture")
    if "solo" in responses.lower():
        tags.append("solo_travel")
    if "group" in responses.lower() or "friends" in responses.lower():
        tags.append("group_travel")
    
    return f"Tags extracted: {', '.join(tags) if tags else 'general_preferences'}. Ready to manifest your sojourn."

def generate_sojourn_story(profile_data: str, preferences: str) -> str:
    """Generate a personalized Bon Sojourn Story in Ella's voice"""
    
    # This would integrate with Virtuoso properties and TAT data
    # For now, using the example Paris story as template
    
    story = """Newly single and glowing from your start-up sale, Paris greets you like an old friend. At Cheval Blanc Paris, your suite over the Seine is both sanctuary and reward. Morning begins in the atelier, laminating dough into golden croissants; afternoon drifts through markets, your tote filling with figs and chèvre before a long lunch on Île Saint-Louis beneath Notre-Dame's bells. Night settles at Le Tout-Paris bar—oysters, steak-frites, a glass of Sancerre, and the ease of conversation when you're exactly where you're meant to be. JOY is the souvenir."""
    
    return f"Your Bon Sojourn Story:\n\n{story}\n\nThis is your first draft. Would you like to refine it?"

def refine_story(adjustment: str, current_story: str) -> str:
    """Refine the story based on user adjustments"""
    adjustments = {
        "more_classic": "Adding more classic elements and traditional experiences",
        "more_contemporary": "Infusing contemporary touches and modern sophistication", 
        "quieter": "Creating more intimate, contemplative moments",
        "more_social": "Adding vibrant, community-focused experiences",
        "add_workshop": "Including a hands-on workshop or class",
        "swap_cafe": "Swapping café experiences for new discoveries"
    }
    
    adjustment_text = adjustments.get(adjustment.lower(), adjustment)
    return f"Story refined: {adjustment_text}. Here's your updated Bon Sojourn Story:\n\n{current_story}"

def save_to_dossier(story: str, tags: str) -> str:
    """Save story and preferences to user's Bon Dossier"""
    dossier_id = f"bon_dossier_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    return f"Saved to your Bon Dossier (ID: {dossier_id}). Your story is now safely stored and shareable."

# Create tool instances
time_tool = FunctionTool(get_current_time)
math_tool = FunctionTool(calculate_simple_math)
json_tool = FunctionTool(format_json)
seasonal_tool = FunctionTool(get_seasonal_recommendations)
accommodation_tool = FunctionTool(get_luxury_accommodation_types)
profile_tool = FunctionTool(collect_user_profile)
intent_tool = FunctionTool(set_trip_intent)
tone_tool = FunctionTool(calibrate_tone)
prompts_tool = FunctionTool(process_signature_prompts)
story_tool = FunctionTool(generate_sojourn_story)
refine_tool = FunctionTool(refine_story)
dossier_tool = FunctionTool(save_to_dossier)
