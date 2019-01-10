import random
import time

def displayIntro():
    print('''Tu te trouves sur des terres peuplées par de nombreux dragons.
Quelques mettres plus loin, tu aperçois l'entrée de deux grottes.
Dans une de ces grottes se trouve un sympathique dragon qui t\'apportera de grandes richesses.
Dans l'autre se trouve un terrible dragon affamé qui ne fera qu'une bouchée de toi !''')
    print()

def chooseCave():
    cave = ''
    while cave !='1' and cave !='2':
        print('Dans quelle grotte veux-tu aller ?(1 ou 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print("Tu t'approches de la grotte...")
    time.sleep(2)
    print("Il fait froid, il fait sombre, tu es effrayé...")
    time.sleep(2)
    print("Un énorme dragon surgit devant toi ! Il ouvre grand sa gueule, et...")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("T'annonce qu'il t'offre son trésor !")
    else:
        print("Te dévore en une misérable bouchée")

playAgain = "oui"
while playAgain == "oui" or playAgain == "o" or playAgain == "yes" or playAgain == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Veux-tu rejouer ? (oui ou non)")
    playAgain = input()
