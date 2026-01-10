##############################################################
# Gauthier Lestimé   09/01/2026    Statistiques              #
##############################################################                                                

a = "0"
val_final = [] 
effectif_total = 0
print("Etude d'une serie statistique")

def choix():
    print("\n1: entrer des valeurs\n2: calculer la moyenne\n3: calculer la mediane\n4: arreter le programme\n")
    a = input()
    return a

def moy(x, y): # x = liste , y = effectif total
    somme_element = 0
    n = 0
    for i in range(y): 
        somme_element += int(x[n])
        n += 1
    return somme_element / y

def med(x, y):
    
    if y % 2 == 0:
        milieu = y // 2
        milieu2 = milieu - 1
        return (x[milieu] + x[milieu2]) / 2
    else:
        return x[y // 2]   

while a != "4":
    a = choix() 

    if a == "1":
        val_save = input()
        val_sep = val_save.split()
        val_sep.sort()
        val_final = val_sep 
        effectif_total = len(val_final)
        print("valeurs triées :", val_final)
        print("effectif_total :", effectif_total)

    if a == "2":
        moyenne = moy(val_final, effectif_total)  
        print("moyenne :", moyenne)

    if a == "3":
        mediane = med(val_final, effectif_total)
        print("mediane :", mediane)
        

    if a == "4":
        break