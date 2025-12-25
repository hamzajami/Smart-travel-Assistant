# ✈️ Smart Travel Assistant

An intelligent travel planning application that combines real-time weather data with AI-powered recommendations to help you plan the perfect trip.

## 🎥 Demo

https://github.com/yourusername/smart-travel-assistant/assets/recording-2025-12-21-225634_EPeAhjnL.mp4

## ✨ Features

- 🌤️ **Real-Time Weather Data** - Get current weather conditions for any city worldwide
- 🤖 **AI-Powered Recommendations** - Personalized travel suggestions using Google Gemini AI
- 🏛️ **Tourist Attractions** - Discover 3-5 famous places to visit in your destination
- 💰 **Cost Estimation** - Detailed breakdown of daily expenses (accommodation, food, transport, tickets)
- 📅 **One-Day Itinerary** - Smart travel plans based on current weather conditions
- 📥 **Export Functionality** - Download your travel plan as a text file
- 🎨 **Modern UI** - Clean and intuitive interface built with Streamlit

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenWeather API Key ([Get it here](https://openweathermap.org/api))
- Google Gemini API Key ([Get it here](https://aistudio.google.com/app/apikey))

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/smart-travel-assistant.git
cd smart-travel-assistant
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. (Optional) Set up environment variables
```bash
export GEMINI_API_KEY="your_gemini_api_key"
export WEATHER_API_KEY="your_openweather_api_key"
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 📦 Dependencies

```
streamlit==1.40.2
requests==2.32.3
google-genai==1.0.1
```

## 🔧 Usage

1. **Enter API Keys** - Provide your Gemini and OpenWeather API keys in the sidebar
2. **Select Destination** - Enter the country and city you want to visit
3. **Get Travel Plan** - Click the "Get Travel Plan" button
4. **View Results** - See weather data, tourist attractions, cost estimates, and itinerary
5. **Download** - Export your travel plan for offline reference

## 📸 Screenshots

### Main Interface
The app features a clean, user-friendly interface with weather metrics and AI-generated travel recommendations.

### Weather Display
Real-time weather information including temperature, conditions, humidity, and wind speed.

### Travel Recommendations
Personalized suggestions for tourist attractions, daily expenses, and travel itineraries.

## 🛠️ Technical Details

- **Frontend**: Streamlit
- **Weather API**: OpenWeatherMap
- **AI Model**: Google Gemini 2.5 Flash
- **Language**: Python 3.8+

## 🌟 Features Breakdown

### Weather Integration
- Real-time weather data from OpenWeatherMap
- Temperature, humidity, wind speed, and conditions
- Metric system (Celsius, km/h)

### AI Recommendations
- Context-aware suggestions based on weather
- Famous tourist attractions with descriptions
- Budget and mid-range accommodation options
- Local transport and food cost estimates
- Currency conversion (local + USD)

### User Experience
- Responsive design
- Color-coded information boxes
- Download functionality
- Error handling and validation
- Loading indicators

## 📝 API Keys Setup

### OpenWeather API
1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Generate an API key
4. Free tier: 60 calls/minute

### Google Gemini API
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Free tier available

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [OpenWeatherMap](https://openweathermap.org/) for weather data
- [Google Gemini](https://deepmind.google/technologies/gemini/) for AI capabilities

## 📧 Contact

Your Name - [Hamza Jami](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/smart-travel-assistant](https://github.com/yourusername/smart-travel-assistant)

---

Made with ❤️ using Streamlit & Google Gemini
