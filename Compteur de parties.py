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
print("Bravo,vous avez gagné", victoires)
print("t nul salut")