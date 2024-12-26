import requests

parameters = {
    "amount": 50,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
questions_data = response.json()
#print(questions_data["results"])

question_data = questions_data["results"]

