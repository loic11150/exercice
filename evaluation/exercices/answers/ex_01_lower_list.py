a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = input("Entrez un nombre : ")
i = 0
newlist = []
number = int(number)
for i in a :
    if i < number :
        newlist.append(i)
print("Les nombres plus petits que le votre dans la liste a : ")
print(newlist)