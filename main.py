import requests
from datetime import datetime

API_ID = "a763257c"
API_KEY = "77381a56bd74e3fd20384516273c6aec"
url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    'Content-Type': 'application/json',
    'x-app-id': API_ID,
    'x-app-key': API_KEY
}
query = input("What workout you've done?: ")
data = {
    "query": query
}

response = requests.post(url, json=data, headers=headers)
exercise_name = response.json()["exercises"][0]["name"].title()
duration_time = int(response.json()["exercises"][0]["duration_min"])
duration = str(duration_time) + " min"
calories = int(response.json()["exercises"][0]["nf_calories"])
today = datetime.today()
formatted_date = today.strftime("%d/%m/%Y")
now = datetime.now().time()
formatted_time = now.strftime("%H:%M:%S")

url_sheet = "https://api.sheety.co/3e90a8cc7ec2fa46ed0c819b872e83f7/daniyalWorkouts/workouts"
MY_TOKEN = "daniyal2005"

bearer_headers = {
    "Authorization": f"Bearer {MY_TOKEN}"
}
body = {
    "workout": {
        "date": formatted_date,
        "time": formatted_time,
        "exercise": exercise_name,
        "duration": duration,
        "calories": calories
    }
}
response_sheet = requests.post(url_sheet, json=body, headers=bearer_headers)
if response_sheet.status_code != 200:
    print("Something went wrong.")
else:
    print("Done.")
