from dice import *

ancestry_data = {
    (1, 4): "Human",
    (5, 6): "Elf",
    (7, 8): "Dwarf",
    (9, 10): "Halfling",
    (11, 11): "Half-orc",
    (12, 12): "Goblin"
}

class_data = {
    1: "Fighter",
    2: "Priest",
    3: "Thief",
    4: "Wizard",
    5: "Ranger",
    6: "Bard"
}

class Character:
    def __init__(self):
        self.ancestry_roll = roll_d12()
        self.ancestry = self.generate_ancestry()
        self.class_roll = roll_d6()
        self.char_class = self.generate_class()

    def generate_ancestry(self):
        for range_, ancestry_name in ancestry_data.items():
            if range_[0] <= self.ancestry_roll <= range_[1]:
                return ancestry_name
        raise ValueError("Invalid ancestry value.")
    
    def generate_class(self):
        return class_data.get(self.class_roll, "Invalid Class")
