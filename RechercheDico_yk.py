###
##Recherche dichotomique
####

def recherche_dt(tab,element):
    """Recherche si tab contient element à partir de l'indice début."""
    debut=0
    fin = len(tab) - 1
    milieu = (debut + fin) // 2
    while debut <= fin:
        if element == tab[milieu]:  # on a trouvé l'élément
            return milieu
        elif element < tab[milieu]:
            fin = milieu - 1  # on considère la partie gauche du tableau
        else:
            debut = milieu + 1  # on considère la partie droite du tableau
        milieu = (debut + fin) // 2
    return -1


####
## Teste recherche dicothomique
####
print("\n************************************\n")
print("Test de la recherche dichotomique")
liste_test = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(recherche_dt(liste_test, 23))  # Doit afficher 5 (indice de 23)
print(recherche_dt(liste_test, 50))  # Doit afficher -1 (non trouvé)


###
## Recherche sequentielle
###

def recherche_seq(tab, element):
    """Retourne l'indice de la première occurence de element dans tab et 
       -1 si element n'est pas dans tab."""
    i = 0
    while i < len(tab) and tab[i] != element:
        i += 1
    if i == len(tab):
        return -1  # en cas d'échec de la recherche
    else:
        return i

###
## Dans cette partie je vais realiser une comparaison entre recherche sequentielle et recherche dichotomique
###

from matplotlib.pyplot import plot, figure, legend, xlabel, ylabel
from time import time
from random import randint
from random import random


###
## Fonction qui genere aleatoirement un tableau
###

def cree_tab(n):
    """genere un tableau aleatoire d'une taille donnee en parametre"""
    tab = []
    i = 0
    while i < n:
        tab.append(randint(1,n))
        i += 1
    return tab

###
## Fonction qui mesure le temps
###

def mesure_temps_recherche(n, nb_mesures):
    """Retourne le temps moyen (sur nb_mesures) d'une recherche d'un élément 
    dans un tableau trié. Le tableau retourné contient le temps pour une 
    recherche séquentielle (indice 0) puis dichotomique (indice1)."""
    tps = [0., 0.]
    tableau = cree_tab(n)
    tableau.sort()
    #print(tableau)
    
    i = 0
    while i < nb_mesures:
        element = n

        # le temps pour la Recherche séquentielle
        tic = time()
        res = recherche_seq(tableau, element)
        tps[0] += time() - tic

        # Le temps pour la Recherche dichotomique
        tic = time()
        res = recherche_dt(tableau, element)
        tps[1] += time() - tic

        i += 1

    tps[0] = round(1000 * tps[0] / nb_mesures, 6)
    tps[1] = round(1000 * tps[1] / nb_mesures, 6)
    return tps

# Mesures des temps :
# - temps_seq[i] contient le temps moyen de recherche séquentielle pour un tableau de taille tailles[i]
# - temps_dt[i] contient le temps moyen de recherche dichotomique pour un tableau de taille tailles[i]
nb_mesures = 20
tailles = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
temps_seq = []
temps_dt = []
i = 0
while i < len(tailles):
    n=randint(1,tailles[i])
    tps = mesure_temps_recherche(n, nb_mesures)
    temps_seq.append(tps[0])
    temps_dt.append(tps[1])
    i += 1


#
# Affichage des temps d'execution moyen par taille
#
print("\n**************************************\n")
print("Temps moyen de recherche :")
print("\n***************************************\n")
i = 0
while i < len(tailles):
    # Affichage de la taille actuelle du tableau
    print("Pour un tableau de taille ", tailles[i], ":")
    
    # Affichage du temps de recherche pour la méthode séquentielle
    print("\t", temps_seq[i], "ms pour la recherche séquentielle")
    
    # Affichage du temps de recherche pour la méthode dichotomique
    print("\t", temps_dt[i], "ms pour la recherche dichotomique")
    
    # Calcul et affichage du facteur d'accélération de la recherche dichotomique 
    #print(f"****La recherche dichotomique est {temps_dt[i]/temps_seq[i]:.3f}x plus rapide")

    i += 1


#
# Affichage graphique de la comparaison , j'ai affiché les 2 courbes 
#

import matplotlib.pyplot as plt  # Importation de la bibliothèque Matplotlib pour tracer des graphiques

# Tracé des courbes de temps d'exécution en fonction de la taille
plt.plot(tailles, temps_seq, label="séquentiel")  # Courbe pour la méthode séquentielle
plt.plot(tailles, temps_dt, label="dichotomie")  # Courbe pour la méthode de dichotomie

# Ajout des labels pour les axes
plt.xlabel("taille")  # Label pour l'axe des abscisses
plt.ylabel("temps (ms)")  # Label pour l'axe des ordonnées

# Ajout d'une légende pour distinguer les courbes
plt.legend()

# Affichage du graphique
plt.show()



