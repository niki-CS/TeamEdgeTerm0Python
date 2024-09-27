import random
active = True

class Superperson:
    def __init__(self, name, age, powers, nemesis):
        self.name = name
        self.age = age
        self.powers = powers
        self.nemesis = nemesis
        self.health_points = 100
    

    def attack(self, enemy):
        global active
        defense = input("The Reverse Flash is trying to attack! Do you want to try and defend yourself?: ")
        if defense == "defend":
            while self.health_points > 0 or enemy.health_points > 0:
                defend = random.randint(1,2)
                do_hit = random.randint(1,2)
                if do_hit == 1 and defend == 1:
                    print("You just got struck. You have lost 20 health points")
                    self.health_points += -20
                    print(self.health_points)
                elif do_hit == 1 and defend == 2:
                    print("You attacked successfully. The Reverse Flash has lost 20 health points")
                    enemy.health_points += -20
                    print(enemy.health_points)
                elif do_hit == 2 and defend == 1:
                    print("Your enemy failed to attack and you missed. No one losed health points")
                elif do_hit == 2 and defend == 2:
                    print("Your enemy failed to attack and you made your move! The Reverse Flash lost 20 health points")
                    enemy.health_points += -20
                    print(enemy.health_points)
                
                if self.health_points == 0:
                    print("The Reverse Flash wins..")
                    active = False
                    break
                elif enemy.health_points == 0:
                    print("The Flash wins..")
                    active = False
                    break
        if defense == "no":
            print("You died..")
            active = False 

flash = Superperson("Flash", 32, "Speed", "Reverse Flash")
reverse_flash = Superperson("Reverse Flash", 32, "Speed", "Flash")
print(f"Your name is {flash.name} and you are {flash.age} years old. My superpower is {flash.powers} and my nemesis is {flash.nemesis}. I have {flash.health_points} health points.")
print(f"Villian: My name is {reverse_flash.name} and I am {reverse_flash.age}. My powers are {reverse_flash.powers} and you, {reverse_flash.nemesis}, are my nemesis. I have {reverse_flash.health_points} health points.")
while active:
    flash.attack(reverse_flash)