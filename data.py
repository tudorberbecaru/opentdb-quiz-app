import requests

# Open Trivia DB API URL and parameters for fetching quiz questions
URL = "https://opentdb.com/api.php"
AMOUNT = 10  # Number of questions for the quiz
CATEGORY = 18  # Category ID for Science: Computers (Check https://opentdb.com/api_category.php)
DIFFICULTY = "medium"  # Difficulty level: 'easy', 'medium', or 'hard'

# API parameters
parameters = {
    "amount": AMOUNT,
    "category": CATEGORY,
    "difficulty": DIFFICULTY,
    "type": "boolean"  # Multiple-choice questions replaced with True/False for simplicity
}

# Make API request and parse JSON response
response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()

# Extract question data
question_data = data["results"]
