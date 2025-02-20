import os
import requests
from config import settings
from datetime import datetime
import google.generativeai as genai

# Configure Gemini API with the provided API key.
genai.configure(api_key=settings.GEMINI_API_KEY)

def analyze_compliance_data(data: dict) -> str:
    """
    Use Google Gemini AI to analyze supplier compliance data.
    """
    prompt = f"Analyze this compliance data and provide insights: {data}"
    
    try:
        model = genai.GenerativeModel("gemini-pro")  # Using Gemini-Pro
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error during Gemini AI analysis: {e}"

def fetch_weather_impact(latitude: float, longitude: float, delivery_date: str) -> str:
    """
    Fetch weather data from OpenWeatherMap to determine if adverse weather impacted delivery.
    Returns a status string.
    """
    url = (
        f"https://api.openweathermap.org/data/2.5/onecall/timemachine?"
        f"lat={latitude}&lon={longitude}&dt={delivery_date}&appid={settings.OPENWEATHER_API_KEY}"
    )
    try:
        response = requests.get(url)
        data = response.json()
        weather_conditions = [weather["main"].lower() for weather in data.get("current", {}).get("weather", [])]
        if "rain" in weather_conditions or "snow" in weather_conditions:
            return "Excused - Weather Delay"
        return "No Weather Impact"
    except Exception as e:
        return f"Error fetching weather data: {e}"
