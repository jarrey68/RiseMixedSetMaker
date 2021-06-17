class Database:

    def __init__(self, armour_list, skills_slots_list):
        self.armour_list = armour_list
        self.head_list = []
        self.torso_list = []
        self.arms_list = []
        self.waist_list = []
        self.leg_list = []
        for i in range(len(self.armour_list)):
            if armour_list[i].armour_type == "Head":
                self.head_list.append(armour_list[i])
            elif armour_list[i].armour_type == "Torso":
                self.torso_list.append(armour_list[i])
            elif armour_list[i].armour_type == "Arms":
                self.arms_list.append(armour_list[i])
            elif armour_list[i].armour_type == "Waist":
                self.waist_list.append(armour_list[i])
            elif armour_list[i].armour_type == "Leg":
                self.leg_list.append(armour_list[i])
        
        self.charms_list = []

        self.skills_slots_list = skills_slots_list
        self.skill_list = []
        self.three_slot_list = []
        self.two_slot_list = []
        self.one_slot_list = []
        for i in range(len(skills_slots_list)):
            self.skill_list.append(skills_slots_list[i][0])
            if skills_slots_list[i][1] == "1":
                self.one_slot_list.append(skills_slots_list[i][0])
            elif skills_slots_list[i][1] == "2":
                self.two_slot_list.append(skills_slots_list[i][0])
            elif skills_slots_list[i][1] == "3":
                self.three_slot_list.append(skills_slots_list[i][0])

