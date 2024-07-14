import tkinter as tk
from tkinter import messagebox

class TriviaQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz")
        self.root.configure(bg="black")

        self.questions = [
            {
                "question": "What is the capital of India?",
                "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
                "answer": "Delhi"
            },
            {
                "question": "Which river is known as the 'Ganga' in India?",
                "options": ["Yamuna", "Brahmaputra", "Indus", "Ganges"],
                "answer": "Ganges"
            },
            {
                "question": "Which Indian state is known as the 'Land of the Gods'?",
                "options": ["Uttarakhand", "Himachal Pradesh", "Kerala", "Jammu and Kashmir"],
                "answer": "Uttarakhand"
            },
            {
                "question": "Who was the first Prime Minister of India?",
                "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Indira Gandhi"],
                "answer": "Jawaharlal Nehru"
            },
            {
                "question": "Which city hosts the annual Kumbh Mela festival?",
                "options": ["Haridwar", "Prayagraj", "Varanasi", "Ujjain"],
                "answer": "Prayagraj"
            },
            {
                "question": "Which Indian city is known as the 'Pink City'?",
                "options": ["Jaipur", "Udaipur", "Jodhpur", "Ajmer"],
                "answer": "Jaipur"
            },
            {
                "question": "Who wrote the Indian national anthem 'Jana Gana Mana'?",
                "options": ["Rabindranath Tagore", "Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose"],
                "answer": "Rabindranath Tagore"
            },
            {
                "question": "Which Indian state is famous for its backwaters?",
                "options": ["Kerala", "Goa", "Tamil Nadu", "West Bengal"],
                "answer": "Kerala"
            },
            {
                "question": "What is India's national animal?",
                "options": ["Tiger", "Elephant", "Lion", "Leopard"],
                "answer": "Tiger"
            },
            {
                "question": "Which Indian monument is considered one of the Seven Wonders of the World?",
                "options": ["Qutub Minar", "Red Fort", "Taj Mahal", "Gateway of India"],
                "answer": "Taj Mahal"
            },
            {
                "question": "In which city is the Indian Institute of Technology (IIT) located?",
                "options": ["Mumbai", "Kanpur", "Delhi", "Kharagpur"],
                "answer": "Kharagpur"
            },
            {
                "question": "Which Indian state has the largest coastline?",
                "options": ["Gujarat", "Maharashtra", "Odisha", "Andhra Pradesh"],
                "answer": "Gujarat"
            },
            {
                "question": "Who was known as the 'Iron Man of India'?",
                "options": ["Sardar Vallabhbhai Patel", "Jawaharlal Nehru", "Subhas Chandra Bose", "B.R. Ambedkar"],
                "answer": "Sardar Vallabhbhai Patel"
            },
            {
                "question": "Which Indian city is called the 'City of Lakes'?",
                "options": ["Udaipur", "Jodhpur", "Bhopal", "Indore"],
                "answer": "Udaipur"
            },
            {
                "question": "Which Indian festival is known as the 'Festival of Lights'?",
                "options": ["Diwali", "Holi", "Navratri", "Dussehra"],
                "answer": "Diwali"
            },
            {
                "question": "Who is known as the 'Father of the Indian Constitution'?",
                "options": ["B.R. Ambedkar", "Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel"],
                "answer": "B.R. Ambedkar"
            },
            {
                "question": "Which state in India has the highest literacy rate?",
                "options": ["Kerala", "Goa", "Mizoram", "Tripura"],
                "answer": "Kerala"
            },
            {
                "question": "Which Indian cricketer has scored the highest number of centuries in Test cricket?",
                "options": ["Sachin Tendulkar", "Virat Kohli", "Rahul Dravid", "Sunil Gavaskar"],
                "answer": "Sachin Tendulkar"
            },
            {
                "question": "Which Indian dance form originated in Kerala?",
                "options": ["Bharatanatyam", "Kuchipudi", "Kathakali", "Odissi"],
                "answer": "Kathakali"
            },
            {
                "question": "Who was the first Indian woman to win an Olympic medal?",
                "options": ["Saina Nehwal", "P.V. Sindhu", "Sakshi Malik", "Karnam Malleswari"],
                "answer": "Karnam Malleswari"
            },
            {
                "question": "Which Indian scientist won the Nobel Prize in Physics in 1930?",
                "options": ["C.V. Raman", "Meghnad Saha", "Satyendra Nath Bose", "Homi J. Bhabha"],
                "answer": "C.V. Raman"
            }
        ]

        self.score = 0
        self.current_question = 0

        self.label_question = tk.Label(root, text="", wraplength=580, justify="center", font=("Times New Roman", 14, "bold"),
                                       bg="light blue", fg="black")
        self.label_question.pack(pady=20)

        self.option_var = tk.StringVar()
        self.option_var.set("")

        self.radio_options_frame = tk.Frame(root, bg="black")
        self.radio_options_frame.pack(pady=10)

        self.radio_options = []
        for i in range(4):
            radio = tk.Radiobutton(self.radio_options_frame, text="", variable=self.option_var, value="", font=("Times New Roman", 12, "bold"),
                                   bg="light pink", fg="black", anchor="w")
            radio.grid(row=0, column=i, padx=10, pady=5, sticky="w")
            self.radio_options.append(radio)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer,
                                       font=("Times New Roman", 12, "bold"), bg="white", fg="black")
        self.submit_button.pack(pady=10, ipadx=20)

        self.label_score = tk.Label(root, text="Score: 0", font=("Times New Roman", 12, "bold"), bg="black", fg="white")
        self.label_score.pack()

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.label_question.config(text=question_data["question"])

            options = question_data["options"]
            max_option_length = max(len(option) for option in options)
            option_width = max(12, max_option_length + 5)  # Adjust minimum width based on longest option

            for i in range(4):
                self.radio_options[i].config(text=options[i], value=options[i], width=option_width)

            self.option_var.set("")
        else:
            messagebox.showinfo("Trivia Quiz", f"Quiz ended! Your final score is: {self.score}")

    def check_answer(self):
        selected_answer = self.option_var.get()
        correct_answer = self.questions[self.current_question]["answer"]
        
        if selected_answer == correct_answer:
            self.score += 1
        
        self.label_score.config(text=f"Score: {self.score}")
        self.current_question += 1
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaQuiz(root)
    root.mainloop()
