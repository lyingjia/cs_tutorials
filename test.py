import random

class House_of_Hogwarts():
    House = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    Adjective = ["daring and brave", "just and loyal", "wise and witty","cunning and ambitious"]
    n = random.randint(0, 3)
    default_h = House[n]
    default_a = Adjective[n]

    def __init__(self, name, house=default_h, adjective=default_a):
        self.name = name
        self.house = house
        self.adjective = adjective
        
    def sorting_hat(self):
        print(f"{self.name} is placed at {self.house} for being {self.adjective}.\n")

class Wizards(House_of_Hogwarts):  
    def __init__(self, name, damage=100, hp=1000):
        super().__init__(name)
        self.damage = damage
        self.hp = hp

    def attack(self, opponent):
        opponent.hp -= self.damage
        if opponent.hp <= 0:
            print(f"Yay! {self.adjective} {self.name} from {self.house} caused fatal damage to {opponent.adjective} {opponent.name} from {opponent.house}")
        else:
            self.hp -= opponent.damage
            if self.hp <= 0:
                self.hp = 0
                print(f"Oh no, {self.adjective} {self.name} from {self.house} is killed by {opponent.adjective} {opponent.name} from {opponent.house}")

    def battle(w1, w2):
        print("#"*50)
        print(f"Chapter 4: Epic Wizard Duels: {w1.name} vs {w2.name} \n")
        n = 1
        while w1.hp > 0 and w2.hp > 0:
            w1.attack(w2)
            n += 1
        print(f"after {n} round of battle.\n") if n == 1 else print(f"after {n} rounds of battles.\n") 
        print("#"*50,"\n")
            
def main():
    # Chapter 1: characters enters Wizarding world
    user = input("What's your name?\n")
    print(f"Hi {user}, Welcome to the Wizarding world!\n")
    
    Character = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Albus Dumbledore", "Lord Voldemort"]
    while True:
        n = input("Pick a character:1) Harry Potter 2)Hermione Granger 3)Ron Weasley 4)Albus Dumbledore 5)Lord Voldemort\n")
        if n.isnumeric():
            n = min(max(int(n),1),5)
            break
        else:
            print("You typed something wrong!")
    name2 = Character[n-1]
    print("#"*50)
    print(f"Chapter 1: {name2} and {user} have now entered the Hogwarts School of Witchcraft and Wizardry!\n")  
        
    # Chapter 2: The sorting hat 
    print("#"*50)
    print(f"Chapter 2: Sorting hat and the house of Hogwarts\n")  
    w1 = House_of_Hogwarts(user)
    w1.sorting_hat()
    w2 = House_of_Hogwarts(name2)
    w2.sorting_hat()

    # Chapter 3: Defence Against the Dark Margic 
    
    # Chapter 4: Epic Wizard Duels
    w1 = Wizards(user, 100, 1000)
    w2 = Wizards(name2, 1000, 1000)
    Wizards.battle(w1,w2)

main()
    
    