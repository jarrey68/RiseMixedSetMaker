from Database import Database
from ArmourPiece import ArmourPiece
from ArmourSet import ArmourSet
from Window import Window

def get_armour_pieces():
    file = open("ArmourPieces.csv", "r")
    raw_armour_pieces = file.read()
    file.close()
    armour_pieces_list = raw_armour_pieces.split("\n")
    armour_pieces_list.pop(0)
    for i in range(len(armour_pieces_list)):
        armour_pieces_list[i] = armour_pieces_list[i].split(",")
        armour_pieces_list[i] = ArmourPiece(armour_pieces_list[i][1], armour_pieces_list[i][10::], armour_pieces_list[i][9].split("-"), int(armour_pieces_list[i][3]), armour_pieces_list[i][0])
    return armour_pieces_list

def get_charms():
    file = open("Charms.csv", "r")
    raw_charms = file.read()
    file.close()
    charms_list = raw_charms.split("\n")
    charms_list.pop(0)
    for i in range(len(charms_list)):
        charms_list[i] = charms_list[i].split(",")
        charms_list[i] = ArmourPiece("Charm", charms_list[i][2::], charms_list[i][1].split("-"), 0, "")
    return charms_list

def get_skills_slots():
    file = open("SkillsSlots.csv", "r")
    raw_skills_slots = file.read()
    file.close()
    skills_slots_list = raw_skills_slots.split("\n")
    for i in range(len(skills_slots_list)):
        skills_slots_list[i] = skills_slots_list[i].split(",")
    return skills_slots_list

def main():

    main_database = Database(get_armour_pieces(), get_skills_slots(), get_charms())

    window = Window(main_database)
    window.root.mainloop()

    

main()