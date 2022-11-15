from characters.character import Character


class Wizard(Character):
    def __init__ (self, name:str, hp:int, weapon, armor, manapoint:int, spell):
        #Character.__init__(self, name:str, hp:int, weapon, armor)
        self.manapoint = manapoint
        self.spell = spell
        