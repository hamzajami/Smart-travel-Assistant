import streamlit as st
import os
import requests
from google import genai

# Page configuration
st.set_page_config(
    page_title="Smart Travel Assistant",
    page_icon="✈️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .weather-box {
        background-color: #E3F2FD;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .expense-box {
        background-color: #FFF3E0;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'response' not in st.session_state:
    st.session_state.response = None

def get_weather_data(city, api_key):
    """Fetch weather data from OpenWeatherMap API"""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        return {
            'temperature': round(data['main']['temp'], 1),
            'condition': data['weather'][0]['description'].title(),
            'humidity': data['main']['humidity'],
            'wind_speed': round(data['wind']['speed'] * 3.6, 1)  # Convert m/s to km/h
        }
    except Exception as e:
        st.error(f"Error fetching weather data: {str(e)}")
        return None

def get_travel_recommendations(country, city, weather_data, gemini_api_key):
    """Get travel recommendations from Gemini API"""
    try:
        client = genai.Client(api_key=gemini_api_key)
        
        system_prompt = """You are an intelligent and friendly travel assistant.
Your job is to help users plan trips by combining weather information with travel recommendations.
You will be given a country, a city, and current weather data.

Your responsibilities:
- Explain the current weather in simple words and say if it is suitable for travel.
- Suggest 3–5 famous tourist places in the given city.
- Briefly explain why each place is popular.
- Estimate daily travel expenses, including accommodation, food, local transport, and entry tickets.
- Show costs in both local currency and USD.
- Suggest a simple one-day travel plan based on the weather conditions.

Guidelines:
- Keep responses clear, practical, and easy to understand.
- Use bullet points where helpful.
- Do not mention APIs, data sources, or system details.
- Do not ask follow-up questions unless necessary.
- Maintain a friendly and helpful tone.

Output format:
- Weather Summary
- Famous Places
- Estimated Expenses
- One-Day Travel Plan"""

        user_prompt = f"""
Country: {country}
City: {city}

Current Weather Information:
- Temperature: {weather_data['temperature']} °C
- Weather Condition: {weather_data['condition']}
- Humidity: {weather_data['humidity']}%
- Wind Speed: {weather_data['wind_speed']} km/h

Tasks:
1. Briefly explain the current weather and whether it is suitable for travel.
2. List 3 to 5 famous tourist places in the given city.
3. Explain why each place is popular.
4. Estimate the daily travel expenses in local currency and USD, including:
   - Accommodation (budget and mid-range)
   - Food
   - Local transport
   - Entry tickets
5. Suggest a simple 1-day travel plan based on the weather.
6. Keep the explanation simple, friendly, and easy to understand.

Rules:
- Do not mention APIs or sources.
- Keep the response concise and practical.
- Use bullet points where helpful.
"""

        # Combine system prompt with user prompt for Gemini
        combined_prompt = f"""{system_prompt}

---

{user_prompt}"""

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=combined_prompt
        )
        
        return response.text
    except Exception as e:
        st.error(f"Error getting travel recommendations: {str(e)}")
        return None

# Main UI
st.markdown('<h1 class="main-header">✈️ Smart Travel Assistant</h1>', unsafe_allow_html=True)
st.markdown("### Plan your perfect trip with real-time weather insights and AI-powered recommendations!")

# Sidebar for API keys
with st.sidebar:
    st.header("⚙️ Configuration")
    gemini_api_key = st.text_input("Gemini API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
    weather_api_key = st.text_input("Weather API Key", type="password", value=os.getenv("WEATHER_API_KEY", ""))
    
    st.markdown("---")
    st.markdown("### 📝 How to use:")
    st.markdown("""
    1. Enter your API keys above
    2. Select a country and city
    3. Click 'Get Travel Plan'
    4. View personalized recommendations!
    """)
    
    st.markdown("---")
    st.markdown("### 🔑 Get API Keys:")
    st.markdown("[OpenWeather API](https://openweathermap.org/api)")
    st.markdown("[Google Gemini API](https://aistudio.google.com/app/apikey)")

# Main form
col1, col2 = st.columns(2)

with col1:
    country = st.text_input("🌍 Country", placeholder="e.g., France, Japan, USA")

with col2:
    city = st.text_input("🏙️ City", placeholder="e.g., Paris, Tokyo, New York")

# Center the button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    submit_button = st.button("🚀 Get Travel Plan", use_container_width=True)

# Process request
if submit_button:
    if not gemini_api_key or not weather_api_key:
        st.error("⚠️ Please provide both API keys in the sidebar!")
    elif not country or not city:
        st.error("⚠️ Please enter both country and city!")
    else:
        with st.spinner("🔍 Fetching weather data and generating travel plan..."):
            # Get weather data
            weather_data = get_weather_data(city, weather_api_key)
            
            if weather_data:
                # Display weather info
                st.markdown('<div class="weather-box">', unsafe_allow_html=True)
                st.subheader(f"🌤️ Current Weather in {city}, {country}")
                
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Temperature", f"{weather_data['temperature']}°C")
                col2.metric("Condition", weather_data['condition'])
                col3.metric("Humidity", f"{weather_data['humidity']}%")
                col4.metric("Wind Speed", f"{weather_data['wind_speed']} km/h")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Get travel recommendations
                recommendations = get_travel_recommendations(country, city, weather_data, gemini_api_key)
                
                if recommendations:
                    st.markdown("---")
                    st.subheader("📍 Your Personalized Travel Plan")
                    st.markdown(recommendations)
                    st.session_state.response = recommendations
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Travel Plan",
                        data=f"Travel Plan for {city}, {country}\n\n{recommendations}",
                        file_name=f"{city}_travel_plan.txt",
                        mime="text/plain"
                    )

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666;'>Made with ❤️ using Streamlit & Google Gemini</p>",
    unsafe_allow_html=True
)