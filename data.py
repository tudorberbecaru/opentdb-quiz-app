import requests

URL = "https://opentdb.com/api.php"
AMOUNT = 10  # Amount of questions you want in your quiz
CATEGORY = 18  # Complete list of Open Trivia DB categories and their IDs: https://opentdb.com/api_category.php
DIFFICULTY = "medium"  # 'easy', 'medium' or 'hard'

parameters = {
    "amount": AMOUNT,
    "category": CATEGORY,
    "difficulty": DIFFICULTY,
    "type": "boolean"
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]
