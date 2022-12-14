import requests

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

response = requests.post(url=nutritionix_exercise_endpoint, json=exercise_body, headers=exercise_headers)
print(response.json())