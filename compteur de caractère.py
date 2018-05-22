
from random import randrange
fichier=open("dico.txt")
contenu = fichier.readlines()

mot = contenu[randrange(len(contenu))]

n=len(mot)
print("le nombre de caractères dans test est : " + str(n))
print(mot)
