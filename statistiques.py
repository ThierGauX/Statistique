a = input("1: entrer des valeurs\n2: calculer la moyenne\n3: calculer la mediane\n4: arreter le programme\n")

def moy(x, y): #x = liste , y = effectif total
    somme_element = 0
    n = 0
    for i in range(1, effectif_total+1):
        somme_element += int(val[n])
        n+=1
    return somme_element/y



def med(x, y):
    if y % 2 == 0:
        milieu = y // 2
        milieu2 = milieu - 1
        return (x[milieu] + x[milieu2]) / 2
    else:
        return x[y // 2]


while a != "4":
    if a == "1":
        b = input()
        val = b.split()
        val.sort()
        effectif_total = len(val)
        pt = input("inprimer les valeurs\n")
        if pt == "y":
            print(val)
        pt = input("inprimer l'effectif\n")
        if pt == "y":
            print(effectif_total)
        a = input("1: entrer des valeurs\n2: calculer la moyenne\n3: calculer la mediane\n4: arreter le programme\n")
    



    if a == "2":
        moyenne = moy(val, effectif_total)
        pt = input("inprimer la moyenne\n")
        if pt == "y":
            print(moyenne)
        a = input("1: entrer des valeurs\n2: calculer la moyenne\n3: calculer la mediane\n4: arreter le programme\n")


    if a == "3":
        mediane = med(val, effectif_total)
        pt = input("inprimer la mediane\n")
        if pt == "y":
            print(mediane)
        a = input("1: entrer des valeurs\n2: calculer la moyenne\n3: calculer la mediane\n4: arreter le programme\n")


    if a == "4":
        break

        
        
        

