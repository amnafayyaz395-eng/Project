# utils.py - Shared utilities between apps
import json
import re
from typing import Dict, List, Any

def format_nutrition_response(response: str) -> str:
    """Format the AI response for better readability in nutrition context."""
    
    # Add emojis based on content
    if any(word in response.lower() for word in ['recipe', 'ingredients', 'cook']):
        response = "🍳 " + response
    elif any(word in response.lower() for word in ['exercise', 'workout', 'fitness']):
        response = "💪 " + response
    elif any(word in response.lower() for word in ['vitamin', 'mineral', 'nutrient']):
        response = "🔬 " + response
    
    # Format lists with bullet points
    lines = response.split('\n')
    formatted_lines = []
    for line in lines:
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            formatted_lines.append(f"• {line.strip()[2:]}")
        else:
            formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

def extract_keywords(query: str) -> List[str]:
    """Extract nutrition-related keywords from query."""
    nutrition_keywords = [
        'calorie', 'protein', 'carb', 'fat', 'vitamin', 'mineral',
        'meal', 'diet', 'recipe', 'healthy', 'weight', 'fitness',
        'vegetarian', 'vegan', 'gluten', 'sugar', 'fiber'
    ]
    
    found_keywords = []
    for keyword in nutrition_keywords:
        if keyword in query.lower():
            found_keywords.append(keyword)
    
    return found_keywords

def save_chat_history(messages: List[Dict], filename: str = "chat_history.json"):
    """Save chat history to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(messages, f, indent=2)
    except Exception as e:
        print(f"Error saving chat history: {e}")

def load_chat_history(filename: str = "chat_history.json") -> List[Dict]:
    """Load chat history from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []