
# Weather && Fashion Alert

The Weather Update Service is a simple Python script that provides regular weather updates for a specific city. It utilizes the OpenWeatherMap API to fetch weather data and sends notifications via email.

## Prerequisites

Before you begin, ensure you have the following:

- Python installed on your system.
- An OpenWeatherMap API key. You can obtain one by signing up on the [OpenWeatherMap website](https://openweathermap.org/api).

## Setup

1. **Clone the repository to your local machine:**

   ```bash
   git clone https://github.com/Anfaal25/Weather-Fashion-Alert.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Weather-Fashion-Alert
   ```

3. **Create a `.env` file in the project directory with the following content:**

   ```env
   api_key=YOUR_OPENWEATHERMAP_API_KEY
   from_email=YOUR_EMAIL@gmail.com
   from_email_password=YOUR_EMAIL_PASSWORD
   to_email=RECIPIENT_EMAIL@gmail.com
   ```

   Replace `YOUR_OPENWEATHERMAP_API_KEY` with your actual OpenWeatherMap API key, `YOUR_EMAIL@gmail.com` with your Gmail email address, `YOUR_EMAIL_PASSWORD` with your email password, and `RECIPIENT_EMAIL@gmail.com` with the recipient's email address.



## Usage

To use the Weather Update Service, run the `WeatherAlert.py` script:

```bash
python WeatherAlert.py
```



## Conclusion

The Weather Update Service provides a simple yet effective solution for staying informed about the weather conditions of a specific city. By utilizing the OpenWeatherMap API and email notifications, this service ensures that you receive regular updates without any hassle.

Feel free to explore the code, customize it according to your preferences, and integrate additional features to enhance its functionality. If you have any questions, suggestions, or feedback, please don't hesitate to reach out at [anfaalmahbub25@gmail.com](mailto:anfaalmahbub25@gmail.com).

Thank you for using the Weather && Fashion Alert ! Stay weather-ready!
