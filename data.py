import requests

URL = "https://opentdb.com/api.php"

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

question_data = response.json()["results"]
