import random
import string
import os


Character = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Albus Dumbledore", "Lord Voldemort"]
House = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
Adjective = ["daring and brave", "just and loyal", "wise and witty","cunning and ambitious"]
Spell = ["Stupefy","Riddikulus","Expecto Patronum", "Avada Kedavra"]    
WIDTH = 100
DEFAULT_DAMAGE, DAMAGE_VARIANCE = 100, 50
DEFAULT_HP, HP_VARIANCE = 1000, 100

def cap_first_letter(string):
    lst = [word[0].upper() + word[1:] for word in string.split()]
    return " ".join(lst)

class House_of_Hogwarts():
    def __init__(self, name, house=None, adjective=None):
        if house==None and adjective==None:
            n = random.randint(0, len(House)-1)
            house = House[n]
            adjective = Adjective[n]
            
        self.name = name
        self.house = house
        self.adjective = adjective
        
    def sorting_hat(self):
        print(f"{self.name} is placed at {self.house} for being {self.adjective}.\n", file=f)

class Wizards(House_of_Hogwarts):  
    def __init__(self, name, spell=None,damage=DEFAULT_DAMAGE, hp=DEFAULT_HP):
        if spell==None:
            spell = Spell[random.randint(0, len(Spell)-1)]
        super().__init__(name)
        self.spell = spell
        self.damage = (damage, 1000)[spell=="Avada Kedavra"] + random.randint(DAMAGE_VARIANCE*(-1),DAMAGE_VARIANCE)
        self.hp = hp + random.randint(HP_VARIANCE*(-1),HP_VARIANCE) 

    def get_spell(self):
        adjective = cap_first_letter(self.adjective)
        print(f"Yay! {adjective} {self.name} has aquired new skills!\n", file=f)
        print(f"{self.name}: \"{self.spell}!\"\n", file=f)
        print(f"{self.name}'s damage at {self.damage} and hp at {self.hp} \n", file=f)

    def attack(self, opponent):
        opponent.hp -= self.damage
        if opponent.hp <= 0:
            return True
        else:
            self.hp -= opponent.damage
            if self.hp <= 0:
                self.hp = 0
                return False
            
    def battle(self, opponent):
        print("#"*WIDTH, file=f)
        head = f"Chapter 4: Epic Wizard Duels: {self.name} vs {opponent.name}"
        print(head + "#"*(WIDTH - len(head))+"\n" + "#"*WIDTH +"\n", file=f)
        print(f"This is your final test at the Hogwarts School of Witchcraft and Wizardry.\n", file=f)
        n = 1
        while self.hp > 0 and opponent.hp > 0:
            win = self.attack(opponent)
            n += 1
        print(f"After {n} round of battle...\n", file=f) if n == 1 else print(f"After {n} rounds of battles...\n", file=f) 
        if win == True:
            adjective = cap_first_letter(self.adjective)
            print(f"Yay! {adjective} {self.name} from {self.house} caused fatal damage to {opponent.adjective} {opponent.name} from {opponent.house}.\n", file=f)
            print("Congradulations! You have achieved an O.W.L! See you next time.\n", file=f)
        else:
            print(f"Oh no, {self.adjective} {self.name} from {self.house} is killed by {opponent.adjective} {opponent.name} from {opponent.house}.\n", file=f)
            print("Don't give up, try again next time.\n", file=f)

class Book():
    # Chapter 1: characters enters Wizarding world
    def chapter1():
        global self, opponent
        self = input("What's your name?\n").title()
        print("#"*WIDTH, file=f)
        title = "Exploring the Wonder of Wizarding World!"
        print("#"*int(WIDTH/2-len(title)/2) + title + "#"*int(WIDTH/2-len(title)/2), file=f)
        for _ in range(3):
            print("#"*WIDTH, file=f)
        
        head = "Chapter 1: This is where it all begins"
        print("\n" + "#"*WIDTH + head + "#"*(WIDTH - len(head))+"\n" + "#"*WIDTH +"\n", file=f)
        print(f"Hi {self}, Welcome to the Wizarding world!\n", file=f)
        opponent = Character[random.randint(0, 3)]
        print(f"{opponent}: \"Hi {self}, I am your companion for the advanture!\"\n", file=f)
        
        print(f"{opponent} and {self} have now entered the Hogwarts School of Witchcraft and Wizardry!\n", file=f)  
            
    # Chapter 2: The sorting hat 
    def chapter2():
        global w1, w2
        print("#"*WIDTH, file=f)
        head = "Chapter 2: Sorting hat and the house of Hogwarts"
        print(head + "#"*(WIDTH - len(head))+"\n" + "#"*WIDTH +"\n", file=f)
        
        w1 = Wizards(self)
        w2 = Wizards(opponent)  
        w1.sorting_hat()
        w2.sorting_hat()        
           
    # Chapter 3: Defence Against the Dark Margic 
    def chapter3():
        print("#"*WIDTH, file=f)
        head = "Chapter 3: Defence Against the Dark Margic"
        print(head + "#"*(WIDTH - len(head))+"\n" + "#"*WIDTH +"\n", file=f)
        Wizards.get_spell(w1)
        Wizards.get_spell(w2)
        
    # Chapter 4: Epic Wizard Duels
    def chapter4():
        Wizards.battle(w1,w2)
        print("#"*WIDTH, file=f)
        print("#"*int(WIDTH/2-3) + "THE END" + "#"*int(WIDTH/2-4), file=f)
        for _ in range(3):
            print("#"*WIDTH, file=f)
    
def main():
    global f
    with open("Book.txt", "w") as f:
        Book.chapter1()
        Book.chapter2()
        Book.chapter3()
        Book.chapter4()
           
    os.startfile("Book.txt")
    
if __name__ == '__main__':
    main()

    
    