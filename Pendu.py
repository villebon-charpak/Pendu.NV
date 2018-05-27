from random import randrange
niveau_de_pendaison = [
"""
   ,==========Y===
   ||  /      |
   || /       |
   ||/        
   ||        
   ||        
   ||
  /||
 //||
============
"""
,
"""
   ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        
   ||        
   ||
  /||
 //||
============
"""
,
"""
 ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||         +
   ||        
   ||
  /||
 //||
============
"""
,
"""
 ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||         +
   ||         +
   ||
  /||
 //||
============
"""
,
"""
 ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||       /-+
   ||         +
   ||
  /||
 //||
============
"""
,
"""
 ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||       /-+-/
   ||         +
   ||
  /||
 //||
============
"""
,
 """
,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||       /-+-/
   ||         +
   ||        |
  /||
 //||
============ 
"""
,
"""
,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||       /-+-/
   ||         +
   ||        | |
  /||
 //||
============

 """
 ]

max_erreurs = len(niveau_de_pendaison) - 1

def lire_lettre(proposition):  

    while True:
        lettre_proposee = input("Proposez une lettre en minuscule: ")
        
        if lettre_proposee in proposition:
            print("Cette lettre a déjà été proposée.")
      
        else:
            break;

    proposition.append(lettre_proposee)
    return lettre_proposee

def affiche_lettres(positions,mot_a_trouver):
    mot_a_afficher=" "
    postion_de_base=0
    for lettre_mot in mot_a_trouver:
        if postion_de_base in propositions:
            mot_a_afficher= mot_a_afficher+lettre_mot
        else:
            mot_a_afficher= mot_a_afficher+"*"
      
        return mot_a_afficher

def partie():
    
    erreurs = 0
    fichier=open("dico.txt")
    contenu = fichier.readlines()

    mot = contenu[randrange(len(contenu))]

    n=len(mot)
    print("le nombre de caractères dans test est : " + str(n))
    print(mot)
    proposition = []

    print(niveau_de_pendaison[erreurs])

    while True:
        print("Lettres déjà proposées :", proposition)
        print("mot à trouver :", mot_avec_tirets(mot, proposition))

        lettre_proposee = lire_lettre(proposition)

        if lettre_proposee in mot:
            if mot_avec_tirets(mot, proposition) == mot:
                print("Bravo, vous avez gagné. Le mot était :", mot)
                print("Nombre d'erreurs:", erreurs)
                return True
        else:
            erreurs = erreurs + 1
            print(niveau_de_pendaison[erreurs])
            if erreurs >= max_erreurs:
                print("vous avez perdu, le mot était :", mot)
                return False

nbr_parties = 0
nbr_victoires = 0
while True:
    nbr_parties = nbr_parties + 1
    if partie():
        nbr_victoires = nbr_victoires + 1

    while True:
        continuer = input("mot commençant par un c pour continuer, mot commençant par un a pour arrêter : ")
        if continuer[0] == 'c' or continuer[0] == 'a' :
             break;
        else:
                print("lisez bien les instructions svp!")
           

    if continuer[0] == 'a':
        break;

print("Vous avez joué", nbr_parties, "partie")
print("vous avez gagnés", nbr_victoires)
