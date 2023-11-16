# Quiz App with Open Trivia DB

This Quiz App fetches questions from the Open Trivia Database API, allowing users to test their knowledge on various topics. The app has a graphical user interface (GUI) and supports True/False questions.

## Screenshots

![screenshot1](https://github.com/tudorberbecaru/opentdb-quiz-app/blob/master/.github/Screenshot1.png)
![screenshot2](https://github.com/tudorberbecaru/opentdb-quiz-app/blob/master/.github/Screenshot2.png)

## Installation

### Prerequisites

- Python 3.x
- Tkinter library (usually included with Python)
- Requests

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/tudorberbecaru/opentdb-quiz-app.git
   cd opentdb-quiz-app
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   
## Usage

Run the following command to start the Quiz App:
   ```bash
   python main.py
   ```
Follow the on-screen instructions to answer questions, and view your final score at the end of the quiz.

## Customizing Your Quiz

Open the `data.py` file to customize your quiz settings. You can adjust the number of questions, category, difficulty level, and question type.
   ```python
   # data.py

   AMOUNT = 10            # Number of questions
   CATEGORY = 18          # Category ID (Check https://opentdb.com/api_category.php)
   DIFFICULTY = "medium"  # Difficulty level: 'easy', 'medium', or 'hard'
   ```

## Project Structure

- `data.py`: Fetches questions from the Open Trivia DB API.
- `main.py`: Initializes the QuizBrain and QuizInterface, handles user interaction.
- `question_model.py`: Defines the Question class.
- `quiz_brain.py`: Manages the quiz logic.
- `ui.py`: Implements the graphical user interface using Tkinter.

## License

This project is licensed under the **MIT** License - see the LICENSE file for details.

## Contribution

Feel free to modify any part of the code according to your preferences.

## Acknowledgments

- **Open Trivia Database** for providing quiz questions.
- **Tkinter** for GUI implementation.
