import random

print()
nom_j1 = str(input("nom du joueur 1 : "))
nom_j2 = str(input("nom du joueur 2 : "))
print()

symbol = "X" 

def premierJoueur(prenom1, prenom2):
    joueurs = [prenom1,prenom2]
    joueur_actuel = random.choice(joueurs)
    print("après tirage aléatoire, c'est", joueur_actuel, "qui commence !")
    return joueur_actuel

joueur_actuel = premierJoueur(nom_j1, nom_j2)

def changeJoueur(dernierJoueur, symbol):

    if symbol == "X":
        symbol = "O"
    else:
        symbol = "X"

    if dernierJoueur == nom_j1:
        return nom_j2, symbol
    else:
        return nom_j1, symbol   
    

grille = [["-","-","-"], 
          ["-","-","-"],
          ["-","-","-"]]

def afficheGrille():
    for i in grille: #i la liste
        print()
        for j in i: #j les éléments de la liste
            print(j, end=" ")

def action(grille, joueur_actuel):
    ligne = int(input("ligne : "))
    while (ligne < 0 or ligne >= 3):
        ligne = int(input("ligne : "))
    colonne = int(input("colonne : "))
    while (colonne >= 3 or colonne < 0):
        colonne = int(input("colonne : "))
    if grille[ligne][colonne] != "-":
        print("place déjà prise")
        action(grille, joueur_actuel)
    else:
        grille[ligne][colonne] = symbol

def gagne_perdu(grille):
    print()
    if (grille[0][0] == grille[0][1] == grille[0][2] == "X") or (grille[0][0] == grille[0][1] == grille[0][2] == "O") : # premiere ligne
        print(joueur_actuel, "a gagné !")
        return False
    elif (grille[1][0] == grille[1][1] == grille[1][2] == "X") or (grille[1][0] == grille[1][1] == grille[1][2] == "O"): # deuxieme ligne
        print(joueur_actuel, "a gagné !")
        return False
    elif (grille[2][0] == grille[2][1] == grille[2][2] == "X") or (grille[2][0] == grille[2][1] == grille[2][2] == "O"): # troisieme ligne
        print(joueur_actuel, "a gagné !")
        return False
    elif (grille[0][0] == grille[1][0] == grille[2][0] == "X") or (grille[0][0] == grille[1][0] == grille[2][0] == "O"): # premiere colonne
        print(joueur_actuel, "a gagné !")
        return False
    elif (grille[0][1] == grille[1][1] == grille[2][1] == "X") or (grille[0][1] == grille[1][1] == grille[2][1] == "O"): # deuxieme colonne
        print(joueur_actuel, "a gagné !")
        return False
    elif (grille[0][2] == grille[1][2] == grille[2][2] == "X") or (grille[0][2] == grille[1][2] == grille[2][2] == "O"): # troisieme colonne
        print(joueur_actuel, "a gagné !")
        return False
    elif (grille[0][0] == grille[1][1] == grille[2][2] == "X") or (grille[0][0] == grille[1][1] == grille[2][2] == "O"): # diagonale /
        print(joueur_actuel, "a gagné !")
        return False
    elif (grille[0][2] == grille[1][1] == grille[2][0] == "X") or (grille[0][2] == grille[1][1] == grille[2][0] == "O"): # diagonale \
        print(joueur_actuel, "a gagné !")
        return False
    else:
        return True

while True:
    print()
    print("Au tour de", joueur_actuel)
    action(grille, joueur_actuel)
    afficheGrille()
    if gagne_perdu(grille) == False: break
    joueur_actuel, symbol = changeJoueur(joueur_actuel, symbol)
    print()