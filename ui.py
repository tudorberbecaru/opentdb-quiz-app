from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        # Initialize GUI components and set up the main window
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="Score: 0", font=("Arial", 12, "bold"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas for Question Text
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 15, "italic"),
                                                     width=280)
        self.get_next_question()
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True Button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # False Button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # Run the main loop
        self.window.mainloop()

    def get_next_question(self):

        # Display the next question on the canvas if there are more questions
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # Display final message when the quiz is completed
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"Congratulations!\nYou've finished the quiz with a score"
                                                            f" of {self.quiz.score}/10.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):

        # Handle user input for True and provide feedback
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):

        # Handle user input for False and provide feedback
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):

        # Display feedback on the canvas based on correctness and update the UI
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # After 1 second, move to the next question
        self.window.after(1000, func=self.get_next_question)
