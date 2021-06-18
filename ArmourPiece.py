class ArmourPiece:

    def __init__(self, armour_type, skills, slots, defence, name):
        self.armour_type = armour_type
        self.skills = []
        for i in range(len(skills) - 1, -1, -1):
            if skills[i] == "":
                skills.pop(i)
        for i in range(0, len(skills), 2):
            self.skills.append([skills[i], skills[i+1]])
        self.slots = slots
        self.defence = defence
        self.name = name
        self.possible_skills_list = []

        
            

            

        


        


    
