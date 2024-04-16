import sys
from random import randint

nombre_mystère = randint(0 , 100)
saisie = ""
essais = 10

print ("*** Le jeu du nombre mystère ***")
while essais != 0:
    print(f"Il te reste {essais} essais \n")

    saisie = input("Devine le nombre entre 0 et 100 \n👉 ")
    while not saisie.isdigit() or int(saisie) > 100 or int(saisie) <0:
        print("Veuillez entrer un nombre entre 0 et 100. \n")
        saisie = input("Devine le nombre entre 0 et 100 \n👉 ")
    saisie = int(saisie)

    if saisie == nombre_mystère:
        print(f"Bravo ! Le nombre mystère était bien {nombre_mystère}")
        print (f"Tu as trouvé le nombre mystère en {11 - essais} essais")
        print("Fin du jeu")
        sys.exit()
    elif saisie > nombre_mystère:
        if essais !=0 :
            print(f"Le nombre mystère est plus petit que {saisie}")
            essais -= 1
    elif saisie < nombre_mystère:
        if essais !=0 :
            print(f"Le nombre mystère est plus grand que {saisie}")
            essais -= 1
        
print(f"\nDommage ! Le nombre mystère était {nombre_mystère}")
print("Fin du jeu")
sys.exit()