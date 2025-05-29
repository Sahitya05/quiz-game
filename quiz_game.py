import tkinter as tk
from tkinter import messagebox

# Define your questions, options, correct answers, and explanations
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris",
        "explanation": "Paris is the capital and most populous city of France."
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "HTML", "C++"],
        "answer": "HTML",
        "explanation": "HTML is the standard markup language for creating web pages."
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Power Unit"],
        "answer": "Central Processing Unit",
        "explanation": "CPU stands for Central Processing Unit. It is the brain of the computer."
    },
    {
        "question": "Who developed Python?",
        "options": ["Dennis Ritchie", "Bjarne Stroustrup", "Guido van Rossum", "James Gosling"],
        "answer": "Guido van Rossum",
        "explanation": "Python was developed by Guido van Rossum and released in 1991."
    },
    {
        "question": "Which of these is not a programming language?",
        "options": ["Python", "Java", "HTML", "Ruby"],
        "answer": "HTML",
        "explanation": "HTML is a markup language, not a programming language."
    }
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")

        self.score = 0
        self.question_index = 0
        self.total_questions = len(questions)
        self.timer_seconds = 15

        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=500, justify="center")
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 14), width=30, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.timer_label = tk.Label(root, text="Time left: 15s", font=("Arial", 14))
        self.timer_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack()

        self.next_question()

    def next_question(self):
        if self.question_index < self.total_questions:
            self.current_question = questions[self.question_index]
            self.question_label.config(text=self.current_question["question"])

            for i, option in enumerate(self.current_question["options"]):
                self.buttons[i].config(text=option, state="normal")

            self.remaining_time = self.timer_seconds
            self.update_timer()
        else:
            self.end_game()

    def update_timer(self):
        if self.remaining_time > 0:
            self.timer_label.config(text=f"Time left: {self.remaining_time}s")
            self.remaining_time -= 1
            self.timer = self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's up!", f"The correct answer was: {self.current_question['answer']}\nExplanation: {self.current_question['explanation']}")
            self.question_index += 1
            self.next_question()

    def check_answer(self, idx):
        self.root.after_cancel(self.timer)
        selected = self.current_question["options"][idx]
        if selected == self.current_question["answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", f"Well done!\nExplanation: {self.current_question['explanation']}")
        else:
            messagebox.showerror("Incorrect!", f"The correct answer was: {self.current_question['answer']}\nExplanation: {self.current_question['explanation']}")
        self.score_label.config(text=f"Score: {self.score}")
        self.question_index += 1
        self.next_question()

    def end_game(self):
        percent = (self.score / self.total_questions) * 100
        result = f"You scored {self.score} out of {self.total_questions} ({percent:.2f}%)"
        messagebox.showinfo("Quiz Finished", result)
        self.show_restart_button()

    def show_restart_button(self):
        for btn in self.buttons:
            btn.pack_forget()
        self.question_label.config(text="Quiz Completed!")
        self.timer_label.pack_forget()

        self.restart_btn = tk.Button(self.root, text="Restart Quiz", font=("Arial", 16), command=self.restart_quiz)
        self.restart_btn.pack(pady=20)

    def restart_quiz(self):
        self.restart_btn.pack_forget()
        self.score = 0
        self.question_index = 0
        self.score_label.config(text="Score: 0")
        for btn in self.buttons:
            btn.pack()
        self.timer_label.pack()
        self.next_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
