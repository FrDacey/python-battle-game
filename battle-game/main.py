from gears.armor import Armor
from gears.weapon import Weapon
from characters.character import Character

#Armor
tunic = Armor('tunic',0)
leather = Armor('Leather',3)
chainmail = Armor('Chainmail',8)
ironarmor = Armor('IronArmor',13)



#Weapons
hand = Weapon('Hand',1)
dague = Weapon('Dague',2)
trainingsword = Weapon('TrainingSword',4)
ironsword = Weapon('IronSword',11)


#Characters
john = Character('John',100,ironsword,chainmail)
jane = Character('Jane',100,ironsword,chainmail)



#Test
while john.hp >= 0 or jane.hp >= 0:
    if john.hp >= 0:
        john.attack(jane)
        print("John Attack with : ",john.weapon.name)
        print("Results: ")
        print(john.name, john.hp, "HP")
        print(jane.name, jane.hp, "HP")
        input("------------------")
    else :
        print(jane.name,' Won the battle')
        break
    if jane.hp >= 0:
        jane.attack(john)
        print("Jane Attack with : ",john.weapon.name)
        print("Results: ")
        print(john.name, john.hp, "HP")
        print(jane.name, jane.hp, "HP")
        input("------------------")
        
    else :
        print(john.name,' Won the battle')
        break
