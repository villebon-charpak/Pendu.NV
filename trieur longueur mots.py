from random import randrange
liste=["ss","kkk","haricot","bvkebibhebfiaebhfuhaggedgfukzgfukgzyf","champignondepeid","pêche"]
liste.sort(key=lambda item:len(item))
print(liste)
mot = liste[randrange(len(liste))]
print(mot)
n=len(mot)

