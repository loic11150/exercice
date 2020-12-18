#chr()
#charcode chiffre : 48 - 57
#charcode lettre 65 - 90
import random
i = 0
mdp = "" 
while i < 12:
    letterOrInt = random.randint(0,1)#aléatoire pour savoir si je créer un int ou un char
    if letterOrInt == 1 :
        charcode = random.randint(65,90)
        char = chr(charcode)
        majOrMin = random.randint(0,1)#aléatoire pour savoir si je met en minuscule ou pas
        if majOrMin == 1 :
            char = char.lower()
    else : 
        charcode = random.randint(48,57)
        char = chr(charcode)
    mdp = mdp + char
    i = i+1

print("Mon MDP généré aléatoirement :")
print(mdp)