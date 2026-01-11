def moy(x: list) -> float :
    """ calcul de la moyenne arithmétique """
    y = len(x)
    somme_element = 0
    for i in range(y): 
        somme_element += int(x[i])
    return somme_element / y

def med(x:list) -> float :
    """ calcul de la médiane"""
    y = len(x)
    if y % 2 == 0 :
        milieu = y // 2
        return (x[milieu] + x[milieu - 1] ) / 2
    else:
        return x[y // 2]

print("Etude d'une série statistique")
valeurs = sorted([float(x) for x in input("Entrez les termes de la série statistique (séparés par un espace) : ").split()])
print("\nsérie ordonnée: ", valeurs)
print("effectif total: ", len(valeurs))
print("étendue: ", valeurs[-1]-valeurs[0])
print("moyenne: ", moy(valeurs))
print("médiane: ", med(valeurs))
