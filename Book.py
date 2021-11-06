import random

class Wizard:
    Character = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Albus Dumbledore", "Lord Voldemort"]
    n = random.randint(0, len(Character) - 1)
    default_name = Character[n]    
    
    def __init__(self, name = default_name):
        self.name = name
        
class Wizarding_world:
    Count = 0
    
    def __init__(self, world):
        self.world = world
        self.wizards = []

    def add_wizard(self, wizard):
        # condition not working?????
        if wizard.name not in self.wizards:
            self.wizards.append(wizard)
            Wizarding_world.Count += 1
            print(f"Hi {wizard.name}, Welcome to the Wizarding world!\n")

    def greeting():
        print(f"{Wizarding_world.Count} wizards have now entered the Hogwarts School of Witchcraft and Wizardry!\n")        
        

class House_of_Hogwarts:
    House = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    n = random.randint(0, len(House) - 1)
    default_house = House[n]    

    def __init__(self, name, house=default_house):
        self.name = name
        self.house = house
        #print(f"{self.name} belongs to {self.house}!")


class Wizards(House_of_Hogwarts):  
    def __init__(self, name, damage=100, hp=1000):
        super().__init__(name)
        self.damage = damage
        self.hp = hp

    def attack(self, opponent):
        opponent.hp -= self.damage
        if opponent.hp <= 0:
            print(f"Yay! {self.name} from {self.house} caused fatal damage to {opponent.name} from {opponent.house}")
        else:
            self.hp -= opponent.damage
            if self.hp <= 0:
                self.hp = 0
                print(f"Oh no, {self.name} is killed by {opponent.name}")

    def battle(w1, w2):
        print(f"###Epic Wizard Duels: {w1.name} vs {w2.name}###\n")
        n = 1
        while w1.hp > 0 and w2.hp > 0:
            w1.attack(w2)
            n += 1
        print(f"after {n} rounds of battle.")


def the_wizarding_world_of_harry_potter():
    w1 = Wizard("Harry Potter")
    w2 = Wizard("Lord Voldemort")
    
    wizarding_world = Wizarding_world("Hogwarts")
    wizarding_world.add_wizard(w1)
    wizarding_world.add_wizard(w2)

    Wizarding_world.greeting()
    
    Harry_Potter = Wizards("Harry Potter", 100, 1000)
    Lord_Voldemort = Wizards("Lord Voldemort", 1000, 1000)
    Wizards.battle(Harry_Potter,Lord_Voldemort)
    
if __name__ == '__main__':
    pass