from tkinter import *
from tkinter.ttk import *

class Window:
    
    def update_required_skill_list(self):
        self.lst_skills.delete(*self.lst_skills.get_children())
        for i in range(len(self.required_skill_list)):
            self.lst_skills.insert(parent="", index="end", iid = i, text = "", values = [self.required_skill_list[i][0], self.required_skill_list[i][1]])

    def add_to_list(self, event):
        required_skill_name = self.combo_skill_v.get()
        required_skill_level = self.combo_skill_level_v.get()
        condition = True
        for skill in self.required_skill_list:
            if required_skill_name == skill[0]:
                skill[1] = required_skill_level
                condition = False
        if condition:
            self.required_skill_list.append([required_skill_name, required_skill_level])
        self.update_required_skill_list()


    def remove_from_list(self, event):
        iid = self.lst_skills.focus()
        if not iid == "":
            self.required_skill_list.pop(int(iid))
            self.update_required_skill_list()
        
    def clear_list(self, event):
        self.required_skill_list = []
        self.update_required_skill_list()
    
    def __init__(self, database):
        self.required_skill_list = []
        self.root = Tk()
        self.root.title("Mixed Set Calculator for Monster Hunter Rise")
        self.root.iconbitmap("calc.ico")

        self.combo_skill_v = StringVar()
        self.combo_skill_v.set(database.skill_list[0])
        self.combo_skill = Combobox(self.root, textvariable = self.combo_skill_v, values = database.skill_list, width = 30, state = "readonly")
        self.combo_skill.grid(row=0, column=0, padx=5, pady=5)

        self.combo_skill_level_v = StringVar()
        self.combo_skill_level_v.set("1")
        self.combo_skill_level = Combobox(self.root, textvariable = self.combo_skill_level_v, values = ["1", "2", "3", "4", "5", "6", "7"], width = 1, state = "readonly")
        self.combo_skill_level.grid(row=0, column=1, padx=5, pady=5)

        self.frm_weapon_slots = Frame(self.root)
        self.frm_weapon_slots.grid(row=0, column=2, padx=5, pady=5)

        self.combo_weapon_slot_one_v = StringVar()
        self.combo_weapon_slot_one_v.set("-")
        self.combo_weapon_slot_one = Combobox(self.frm_weapon_slots, textvariable = self.combo_weapon_slot_one_v, values = ["-", "1", "2", "3"], width = 1, state = "readonly")
        self.combo_weapon_slot_one.pack(side=LEFT)

        self.combo_weapon_slot_two_v = StringVar()
        self.combo_weapon_slot_two_v.set("-")
        self.combo_weapon_slot_two = Combobox(self.frm_weapon_slots, textvariable = self.combo_weapon_slot_two_v, values = ["-", "1", "2", "3"], width = 1, state = "readonly")
        self.combo_weapon_slot_two.pack(side=LEFT)

        self.combo_weapon_slot_three_v = StringVar()
        self.combo_weapon_slot_three_v.set("-")
        self.combo_weapon_slot_three = Combobox(self.frm_weapon_slots, textvariable = self.combo_weapon_slot_three_v, values = ["-", "1", "2", "3"], width = 1, state = "readonly")
        self.combo_weapon_slot_three.pack(side=LEFT)

        self.frm_buttons = Frame(self.root)
        self.frm_buttons.grid(row=1, rowspan=3, column=2, sticky=N)

        self.btn_add = Button(self.frm_buttons, text = "Add")
        self.btn_add.bind("<ButtonRelease>", self.add_to_list)
        self.btn_add.pack(pady = 5)

        self.btn_remove = Button(self.frm_buttons, text = "Remove")
        self.btn_remove.bind("<ButtonRelease>", self.remove_from_list)
        self.btn_remove.pack(pady = 5)

        self.btn_clear = Button(self.frm_buttons, text = "Clear")
        self.btn_clear.bind("<ButtonRelease>", self.clear_list)
        self.btn_clear.pack(pady = 5)

        self.btn_generate = Button(self.frm_buttons, text = "Generate")
        #self.btn_generate.bind("<ButtonRelease>", self.generate_sets)
        self.btn_generate.pack(pady = 10)

        self.lst_skills = Treeview(self.root, height=25)
        self.lst_skills["columns"] = ("Name", "Level")
        self.lst_skills.column("#0", width = 0, stretch = NO)
        self.lst_skills.column("Name", width = 200, anchor = W, stretch = NO)
        self.lst_skills.column("Level", width = 50, anchor = W, stretch = NO)
        self.lst_skills.heading("Name", text = "Skill Name", anchor = W)
        self.lst_skills.heading("Level", text = "Level", anchor = W)
        self.lst_skills.grid(row = 1, rowspan=3, column = 0, columnspan = 2,  sticky = SW, padx = 10, pady = 10)

        self.lst_sets = Treeview(self.root, height=25)
        self.lst_sets["columns"] = ("Head", "Torso", "Arms", "Waist", "Leg", "Charm", "Decorations")
        self.lst_sets.column("#0", width = 0, stretch = NO)
        self.lst_sets.column("Head", width = 200, anchor = W, stretch = NO)
        self.lst_sets.column("Torso", width = 200, anchor = W, stretch = NO)
        self.lst_sets.column("Arms", width = 200, anchor = W, stretch = NO)
        self.lst_sets.column("Waist", width = 200, anchor = W, stretch = NO)
        self.lst_sets.column("Leg", width = 200, anchor = W, stretch = NO)
        self.lst_sets.column("Charm", width = 200, anchor = W, stretch = NO)
        self.lst_sets.column("Decorations", width = 200, anchor = W, stretch = NO)
        self.lst_sets.heading("Head", text = "Head", anchor = W)
        self.lst_sets.heading("Torso", text = "Torso", anchor = W)
        self.lst_sets.heading("Arms", text = "Arms", anchor = W)
        self.lst_sets.heading("Waist", text = "Waist", anchor = W)
        self.lst_sets.heading("Leg", text = "Leg", anchor = W)
        self.lst_sets.heading("Charm", text = "Charm", anchor = W)
        self.lst_sets.heading("Decorations", text = "Decorations", anchor = W)
        self.lst_sets.grid(row = 0, rowspan=100, column=3, padx = 10, pady = 10, sticky=SE)

    

