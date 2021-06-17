class ArmourPiece:

    def __init__(self, armour_type, skills, slots, defence, name):
        self.armour_type = armour_type
        self.skills = skills
        self.slots = slots
        self.defence = defence
        self.name = name
        self.create_possible_skill_list(skills, slots)

    def create_possible_skill_list(self, skills, slots):
        self.possible_skill_list = []
        


    
