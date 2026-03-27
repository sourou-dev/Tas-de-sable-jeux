from copy import deepcopy
import random

# Création d'une grille remplir de 0
def creer_grille(nbligne, nbcolonne):
    grille=[]
    for i in range(nbligne):
        ligne=[]
        for j in range(nbcolonne):
            ligne.append(0)
        grille.append(ligne)
    return grille



#copie une grille
def copier_grille(grille):
    return deepcopy(grille) #pour copier ma grille créer

# fonction pour compter  le nombre de grains dans chaque colonne
#envoie une liste du nombre grain à chaque indice de colonne 

def grain_colonnes(grille):
    nbligne = len(grille)
    nbcolonne = len(grille[0])
    colonnes = []

    for j in range(nbcolonne):
        c = 0
        for i in range(nbligne):
            if grille[i][j] == 1:
                c += 1
        colonnes.append(c)

    return colonnes



#fonction pour trouver les falaises :
#parcourt les colonnes et compare chaque valeur à la suivante
#s'il y a au moins 2 grains de différence, alors c'est une falaise



def trouver_falaises(grille):
    colonnes = grain_colonnes(grille)
    falaises = []

    for i in range(len(colonnes) - 1):
        if colonnes[i] > colonnes[i+1] + 2: #si la le nombre de grain dans la colonne i est superieure à celui dans la colonne i+1
                                                        #et que la diffrece est superieure à 2   
            falaises.append(i)

    return falaises



#jouer une falaise: retire le grain sur une falaise
#et l'ajoute à la colonne la suivant

def jouer_falaise(grille, col):
    nbl = len(grille)

    #retirer le grain le plus haut
    for i in range(nbl):
        if grille[i][col] == 1:
            grille[i][col] = 0
            break

    #ajouter un grain dans la colonne suivante
    for i in range(nbl-1, -1, -1):
        if grille[i][col+1] == 0:
            grille[i][col+1] = 1
            break

#quand le tas est stable: informe si y'a de falaise ou pas

def est_stable(grille):
    if trouver_falaises(grille)==[]:
        return True
    return False



#creer un tas aleatoire : remplir aleatoirement la grille creer

def tas_aleatoire(nbligne, nbcol):
    grille = creer_grille(nbligne, nbcol)

    for colonne in range(nbcol):
        nombre_grains = random.randint(0, nbligne - 1)

        for grain in range(nombre_grains):
            ligne = nbligne - 1 - grain
            grille[ligne][colonne] = 1

    return grille
