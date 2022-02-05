import csv
import random as rand
import time
import tkinter
from tkinter import *
import datetime as dt
from threading import Thread
THEME_COLOR = "#252A34"
FONT = ("Arial", 20, "italic")

# ---------------------------------------------Setting up the UI--------------------------------------------- #
class Typer:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=50, pady=20, bg=THEME_COLOR)
        self.window.bind("<KeyRelease>", self.check)

        self.text = tkinter.StringVar()
        self.text_label = Label(self.window, borderwidth=2, textvariable=self.text, font=FONT, background="white", justify=LEFT, wraplength=800)
        self.text.set("Hello\n"
                      "Welcome to the Disappearing Text App!\n\n"
                      "You can generate a random prompt to type or you can just type freely for 5 minutes\n"
                      "If you stop typing for at least 5 seconds, everything will get cleared"
                      )
        self.text_label.grid(pady=30, padx=30, column=0, row=1, columnspan=3, sticky=NW)

        self.user_text = Text(self.window, width=70, height=12, font=("Arial", 15))
        self.user_text.grid(column=0, row=2, columnspan=3, pady=5, padx=30, sticky=W)
        self.user_text.config(state='disabled')

        self.start_noprompt_button = Button(width=20, text="Start without prompt", font=("Arial", 15), command=lambda:Thread(target=self.start).start())
        self.start_noprompt_button.grid(column=0, row=3, pady=15, sticky=E)

        self.prompt_button = Button(width=20, text="Generate random prompt", font=("Arial", 15), command=lambda:Thread(target=self.random_prompt).start())
        self.prompt_button.grid(column=1, row=3, pady=15, sticky=N)

        self.quit_button = Button(width=20, text="Quit", command=self.finish, font=("Arial", 15))
        self.quit_button.grid(column=2, row=3, sticky=W, pady=15)

        self.complete_text = tkinter.StringVar()
        self.complete_text.set(" ")
        self.complete_label = tkinter.Label(self.window, textvariable=self.complete_text, background=THEME_COLOR, font="Ariel", fg="white")
        self.complete_label.grid(column=1, row=4)
        self.begin = False
        self.countdown = None

        self.window.mainloop()

    def start(self):
        self.begin = True
        self.user_text.delete('1.0', END)
        self.text.set("Start typing away!\n"
                      "Type whatever you want!\n"
                      )
        self.user_text.config(state='normal')
        self.user_text.focus()
        time.sleep(1)
        self.start_time = time.time()
        self.highest_count = 0
        self.long_timer = time.time()
        self.stop_timer = None
        while self.long_timer < self.start_time + 300:
            if self.stop_timer == None:
                if self.current_count > self.highest_count:
                    self.highest_count = self.current_count
                elif self.highest_count == self.current_count or self.highest_count > self.current_count:
                    self.stop_timer = time.time()

            else:
                if self.current_count > self.highest_count:
                    self.highest_count = self.current_count
                    self.stop_timer = None
                elif time.time() >= self.stop_timer + 5:
                    self.user_text.delete('1.0', END)
                    self.long_timer = self.start_time + 301
        print("stopped")
        self.text.set("Time is up!\n"
                      "Click one of the buttons to try again or click 'Quit' to exit the program")
        self.user_text.config(state='disabled')

    def check(self, event=None):
        self.current_count = len(self.user_text.get("1.0", "end - 1 chars"))

    def prepare(self):
        # Currently this will just produce a random string of words instead of a proper prompt
        with open(file="words.csv", encoding="utf-8-sig") as file:
            words = []
            data = csv.reader(file)
            for row in data:
                words.append(''.join(row))
        file.close()
        prompt_list = []
        self.word_amount = rand.randint(5, 50)
        for x in range(self.word_amount):
            word = rand.choice(words)
            prompt_list.append(word)
            words.remove(word)
        self.prompt = " ".join(prompt_list)

    def random_prompt(self):
        self.begin = True
        self.user_text.config(state='normal')
        self.user_text.delete('1.0', END)
        self.prepare()
        self.text.set("Start typing away!\n"
                      "Type whatever you want!\n"
                      )
        self.user_text.focus()
        self.user_text.insert(1.0, self.prompt)
        time.sleep(1)
        self.start_time = time.time()
        self.highest_count = 0
        self.long_timer = time.time()
        self.stop_timer = None
        while self.long_timer < self.start_time + 300:
            if self.stop_timer == None:
                if self.current_count > self.highest_count:
                    self.highest_count = self.current_count
                elif self.highest_count == self.current_count or self.highest_count > self.current_count:
                    self.stop_timer = time.time()

            else:
                if self.current_count > self.highest_count:
                    self.highest_count = self.current_count
                    self.stop_timer = None
                elif time.time() >= self.stop_timer + 5:
                    self.user_text.delete('1.0', END)
                    self.long_timer = self.start_time + 301
        self.text.set("Time is up!\n"
                      "Click one of the buttons to try again or click 'Quit' to exit the program")
        self.user_text.config(state='disabled')

    def finish(self):
        self.window.destroy()
