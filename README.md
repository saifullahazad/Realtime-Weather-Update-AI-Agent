# WeatherGenie CLI

WeatherGenie CLI is a domain-specific command-line application that serves as your personalized weather advisor. It intelligently handles weather-related queries by deciding whether to fetch live weather data from an external API or to generate a generic weather advice message. Additionally, if a query is in Bangla, it responds in Bangla and prepends a time-based greeting (e.g., "শুভ সকাল" or "শুভ সন্ধ্যা").

## Overview

- **Domain-Specific:** Only handles weather-related queries.
- **Decision Making:** Uses an LLM to decide whether to fetch live data ("live") or to provide generic advice ("generic").
- **Live Weather Data:** Integrates with a live weather API (WeatherAPI) to fetch current weather conditions.
- **Multilingual Support:** Detects if the query is in Bangla and responds accordingly with a greeting.
- **Extensible:** Easily expandable to add more features or handle additional domains.

## Project Structure

```
Realtime-Weather-Update-AI-Agent/
├── .env                # Environment variables (e.g., API keys)
├── weather_api.py      # Module to call the live weather API
├── agent.py            # Contains decision making and final response composition
├── main.py             # CLI application entry point
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation (this file)
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Realtime-Weather-Update-AI-Agent.git
   cd Realtime-Weather-Update-AI-Agent
   ```

2. **Create and Activate a Virtual Environment:**

   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows:**
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies:**

   Ensure your `requirements.txt` file includes the following:
   ```plaintext
   openai
   langchain
   python-dotenv
   langchain-community
   langchain-openai
   requests
   pytz
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Configure Environment Variables

1. **Create a `.env` File** in the project root.
2. **Add Your API Keys:**  
   Example content for `.env`:
   ```ini
   OPENWEATHER_API_KEY=your_weather_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   Replace the placeholders with your actual API keys.

## Usage

Run the application from your terminal:
```bash
python main.py
```

You will see a prompt like:
```
Welcome to WeatherGenie CLI - Your Personalized Weather Advisor!
Ask WeatherGenie a question:
```

You can now enter weather-related queries. For example:
- **English Query:** "What's the weather like in Dhaka today?"
- **Bangla Query:** "তুমি কি আমাকে বাংলাদেশের আবহাওয়া বলতে পারো?"

## Examples

### In-Domain Query (Live Data)
- **Query:** "What's the weather like in Dhaka today?"
- **Expected Response:** A final message with weather details.

### In-Domain Query (Generic Advice)
- **Query:** "What is a good day for a picnic?"
- **Expected Response:** A friendly advice message without live data.

### Out-of-Domain Query
- **Query:** "What time is it?"
- **Expected Response:** "I'm sorry, but I only handle weather-related queries."

### Bangla Query Example
- **Query:** "তুমি কি আমাকে বাংলাদেশের আবহাওয়া বলতে পারো?"
- **Expected Response:** A final message in Bangla with a greeting and weather details.

## Future Enhancements

- **Improve Location Extraction:** Enhance the logic to extract locations more robustly from diverse query formats.
- **Enhanced Response Generation:** Refine prompt engineering to yield more detailed and context-aware responses.
- **Additional Features:** Add support for forecasts, weather alerts, or integration with other APIs.
- **Error Handling:** Implement better error handling for API failures and unexpected inputs.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions, collaborations, or suggestions, feel free to reach out:
- **Email:** [your.email@example.com](mailto:your.email@example.com)
- **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)

---

Enjoy using WeatherGenie CLI and feel free to explore, fork, and contribute to this project!
