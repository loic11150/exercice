happynumbers = open("happynumbers.txt","r")
primenumbers = open("primenumbers.txt","r")

primenumbersLines = primenumbers.readlines()#ligne du txt
happynumberslines = happynumbers.readlines()#ligne du .txt
numberlist = []
#pour chaque ligne de happynumbers on regarde chaque ligne de prime numbers et on regarde si il y dedans
for happyLine in happynumberslines:
    happyLine = happyLine.replace("\n","")
    for primeline in primenumbersLines:
        primeline = primeline.replace("\n","")
        if happyLine == primeline:
            numberlist.append(primeline)
print("Les nombres en communs dans les deux listes sont les suivants :")
print(numberlist)