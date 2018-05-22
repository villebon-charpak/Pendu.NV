
from random import randrange

minuscules = "abcdefghijklmnopqrstuvwxyz"
#Dessins en cas d'erreur
dessins = [
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

max_erreurs = len(dessins) - 1

def lire_la_lettre(proposition):  

    while True:
        lettre = input("Proposez une lettre en minuscule: ")
        
        if lettre in proposition:
            print("Cette lettre a déjà été proposée.")
      
        else:
            break;

    proposition.append(lettre)
    return lettre

def tirets(mot, proposition):
    
    
    m = ''
    for lettre in mot:
        if lettre in proposition:
            m = m + lettre
        else:
            m = m + '-'
    return m

def jeux():
    
    erreurs = 0
    mot = mots[randrange(len(mots))]
    proposition = []

    print(dessins[erreurs])

    while True:
        print("Lettres déjà proposées :", proposition)
        print("mot à trouver :", mot_avec_tirets(mot, proposition))

        lettre = lire_lettre(proposition)

        if lettre in mot:
            if mot_avec_tirets(mot, proposition) == mot:
                print("Bravo, vous avez gagné. Le mot était :", mot)
                print("Nombre d'erreurs:", erreurs)
                return True
        else:
            erreurs = erreurs + 1
            print(dessins[erreurs])
            if erreurs >= max_erreurs:
                print("vous avez perdu, le mot était :", mot)
                return False
#Compteur de parties et de parties gagnées
                
parties = 0
victoires = 0
while True:
    parties = parties + 1
    if partie():
        victoires = victoires + 1

    while True:
        continuer = input("o pour continuer, n pour arrêter : ")
        if continuer == 'o' or continuer == 'n':
            break;

    if continuer == 'n':
        break;

print("Vous avez joué", parties, "partie")
print(",vous avez gagné", victoires)
print("Salut")