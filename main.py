import requests, json
from datetime import datetime

nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_headers = {
    "x-app-id" : "2fdab177",
    "x-app-key" : "96948f7adb5195cdf8fe55b667a16d96",
    "Content-Type" : "application/json"
}

query = input("Tell me which exercise you did: ")

exercise_body = {
    "query":query,
    "gender":"female",
    "weight_kg":52.5,
    "height_cm":160,
    "age":29
}

response = requests.post(url=nutritionix_exercise_endpoint, json=exercise_body, headers=exercise_headers).json()

today = datetime.now()
date = today.date()
time = today.strftime("%H:%M")

sheety_endpoint = "https://api.sheety.co/702e719946a64ffd027aa649d5887a1c/workoutTracker/workouts"


for user_input in response["exercises"]:
    sheety_body = {

        "workout": {
        "date": str(date),
        "time": time,
        "exercise": user_input["name"],
        "duration": user_input["duration_min"],
        "calories": user_input["nf_calories"]
        }
    }
    response = requests.post(url=sheety_endpoint, json=sheety_body)
    response.text


