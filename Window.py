from tkinter import *
from tkinter.ttk import *

class Window:
    def __init__(self, database):
        self.root = Tk()
        self.combo_skill_v = StringVar()
        self.combo_skill_v.set(database.skill_list[0])
        self.combo_skill = Combobox(self.root, textvariable = self.combo_skill_v, values = database.skill_list, width = 30, state = "readonly")
        self.combo_skill.grid(row=0, column=0, padx=5, pady=5)

