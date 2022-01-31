import csv
import random as rand
import time
import tkinter
from tkinter import *
import datetime as dt

THEME_COLOR = "#252A34"
FONT = ("Arial", 20, "italic")

# ---------------------------------------------Setting up the UI--------------------------------------------- #
class TypeTest:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.config(padx=50, pady=20, bg=THEME_COLOR)
        self.window.bind('<Return>', self.check_scores)

        self.canvas = Canvas(height=450, width=800, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=3, pady=30)

        self.text = tkinter.StringVar()
        self.text_label = Label(self.window, borderwidth=2, textvariable=self.text, font=FONT, background="white", justify=LEFT, wraplength=800)
        self.text.set("Hello\n"
                      "Welcome to the Typing Test App!\n\n"
                      "Please type in the difficulty you would like to try.\n"
                      "Then click the 'Select Difficulty' button:\n\n"
                      "Easy\n"
                      "Normal\n"
                      "Hard")
        self.text_label.grid(pady=30, column=0, row=1, columnspan=3, sticky=NW)

        self.user_text = Text(self.window, width=72, height=5, font=("Arial", 15))
        self.user_text.grid(column=0, row=3, columnspan=3, pady=5, sticky=W)

        self.difficulty_button = Button(width=15, text="Select Difficulty", font=("Arial", 15), command=self.difficulty)
        self.difficulty_button.grid(column=0, row=5, columnspan=2, pady=5, sticky= W)

        self.start_button = Button(width=15, text="Start", font=("Arial", 15), command=self.start)
        self.start_button.grid(column=1, row=5, pady=5, sticky=E)

        self.quit_button = Button(width=15, text="Quit", command=self.finish, font=("Arial", 15))
        self.quit_button.grid(column=2, row=5, sticky=E)

        self.complete_text = tkinter.StringVar()
        self.complete_text.set(" ")
        self.complete_label = tkinter.Label(self.window, textvariable=self.complete_text, background=THEME_COLOR, font="Ariel", fg="white")
        self.complete_label.grid(column=1, row=4)

        self.begin = False

        self.window.mainloop()

    def start(self):
        if self.begin is False:
            pass
        else:
            time.sleep(2)
            self.text.set(self.prompt)
            self.start_time = dt.datetime.now()
            self.user_text.focus()

    def difficulty(self):
        user_input = (self.user_text.get("1.0", "end - 1 chars")).upper()
        if user_input == "EASY" or user_input == "NORMAL" or user_input == "HARD":
            self.text.set("Get ready to start typing!\n\n"
                          "Press the 'Start' button when you're ready!")
            self.user_text.delete("1.0", 'end')
            self.prepare(mode=user_input)
        else:
            self.text.set("That was an invalid input.\n\n"
                          "Please type in the difficulty you would like to try and then click the 'Select Difficulty' button:\n"
                          "'Easy'\n"
                          "'Normal'\n"
                          "'Hard'")
            self.user_text.delete("1.0", 'end')

    def prepare(self, mode):
        self.begin = True
        with open(file="words.csv", encoding="utf-8-sig") as file:
            words = []
            data = csv.reader(file)
            for row in data:
                words.append(''.join(row))
        file.close()
        self.mode = mode
        if mode == "EASY":
            prompt_list = []
            self.word_amount = rand.randint(5, 20)
            for x in range(self.word_amount):
                word = rand.choice(words)
                prompt_list.append(word)
                words.remove(word)
            self.prompt = " ".join(prompt_list)
        elif mode == "NORMAL":
            prompt_list = []
            self.word_amount = rand.randint(20, 45)
            for x in range(self.word_amount):
                word = rand.choice(words)
                prompt_list.append(word)
                words.remove(word)
            self.prompt = " ".join(prompt_list)
        elif mode == "HARD":
            prompt_list = []
            self.word_amount = rand.randint(45, 80)
            for x in range(self.word_amount):
                word = rand.choice(words)
                prompt_list.append(word)
                words.remove(word)
            self.prompt = " ".join(prompt_list)

    def check_scores(self, event=None):
        if self.begin is False:
            pass
        else:
            user_input = list(self.user_text.get("1.0", "end - 1 chars"))[:-1]
            prompt = list(self.prompt)
            print(user_input)
            print(prompt)
            total = len(prompt)
            print(total)
            if len(user_input) != total:
                pass
            else:
                correct = 0
                for x in range(total):
                    if user_input[x] == prompt[x]:
                        correct += 1
                    else:
                        pass
                print(correct)
                self.accuracy = correct/total * 100
                self.end_time = dt.datetime.now()
                difference = self.end_time - self.start_time
                self.minutes = divmod(difference.total_seconds(), 60)
                for_wpm = self.minutes[0] + float('{:.2f}'.format((self.minutes[1])/60))
                self.wpm = round(self.word_amount/for_wpm)
                self.text.set(f"You finished in {self.minutes[0]} minutes and {'{:.2f}'.format(self.minutes[1])} seconds\n"
                              f"with an accuracy of {'{:.2f}'.format(self.accuracy)}% and wpm of {self.wpm}!\n\n"
                              f"To play again type in the difficulty you would like to try and then click the 'Select Difficulty' button:\n"
                              "'Easy'\n"
                              "'Normal'\n"
                              "'Hard'")
                self.user_text.delete("1.0", 'end')
                self.add_score()
        user_input = (self.user_text.get("1.0", "end - 1 chars")).upper()
        if user_input == "SCORES":
            with open(file="score.csv", encoding="utf-8-sig") as file:
                scores = []
                data = csv.reader(file)
                for row in data:
                    scores.append(''.join(row))
            print(scores)
            self.text.set("Top 10:\n"
                          ""
                          "If you would like to play,"
                          "please type in the difficulty you would like to try and then click the 'Select Difficulty' button:\n"
                          "'Easy'\n"
                          "'Normal'\n"
                          "'Hard'")

    def add_score(self):
        with open("score.csv", mode="w") as file:
            file.write(f"Difficulty: {self.mode} WPM: {self.wpm} Time: {self.minutes[0]} minutes {'{:.2f}'.format(self.minutes[1])} seconds")
        file.close()

    def check_highscores(self):
        with open("score.csv") as file:
            self.high_score = int(file.read())
        file.close()
        pass

    def finish(self):
        self.window.destroy()
