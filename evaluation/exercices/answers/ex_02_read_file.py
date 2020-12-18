file = open("nameslist.txt","r")
lines = file.readlines()#lignes du ficher txt

name = {}#dictionnaire
#onparcours les lignes 
for line in lines :
    line = line.replace("\n","")# ça me sortait darth/n luke/n etc... du coup je vire le /n car c'est moche
    if line in name : # si le prénom est dans ma liste on incrémente la value de la key de 1
        name[line] = name[line] + 1
    else :
        name[line] = 1 # si le prénnom n'était pas dans la liste 
file.close
#affichage
for key in name:
    name[key] = str(name[key])
    print(key +" apparaît "+ name[key]+ " fois dans le fichier")
