class Character:
    def __init__(self,name:str,hp:int,weapon,armor):
        self.name = name        
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
    
    def attack(self, other):
        if (self.weapon.damage - other.armor.defense) >0:
            other.hp = other.hp - (self.weapon.damage - other.armor.defense)
        else:
            other.hp = other.hp
