from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "682578b731ed0cdfcb26b93653a8dddc"  # your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }
        else:
            weather_data = {"error": "City not found."}
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
   app.run(debug=True)