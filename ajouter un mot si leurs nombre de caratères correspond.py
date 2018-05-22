from random import randrange
fichier = open("dico.txt")
contenu = fichier.readlines()
mot = contenu[randrange(len(contenu))]
question = ("azertyuiopq")
i=len(question)
n=len(mot)
print(n)
li=[]
if n==i:
    li.append(mot)
    print(li)