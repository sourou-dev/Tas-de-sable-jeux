import tkinter as tk
from tkinter import messagebox
import random


from mesgrilles import *

TAILLE_CASE = 30
COULEUR_GRAIN = "#1E3A8A"

nbl = 20
nbcol =20


memoire = []

fen = tk.Tk()
fen.title("Tas de sable")

can = tk.Canvas(fen, width=nbcol*TAILLE_CASE, height=nbl*TAILLE_CASE, bg="white")
can.grid(row=0, column=0, columnspan=5)




#dessiner la grille :
#affiche les cases et met la couleur à celles qui contiennent un grain


def dessiner_grille():
    can.delete("all")

    for i in range(nbl):
        for j in range(nbcol):

            x0 = j*TAILLE_CASE
            y0 = i*TAILLE_CASE
            x1 = x0 + TAILLE_CASE
            y1 = y0 + TAILLE_CASE

            can.create_rectangle(x0,y0,x1,y1,outline="black")

            if grille[i][j] == 1:
                can.create_rectangle(x0+5,y0+5,x1-5,y1-5,fill=COULEUR_GRAIN)

                

#pour jouer une étape :
                
#trouve les falaises
#choisit une colonne au hasard
#déplace un grain
#met à jour l'affichage

def une_etape():

    global grille

    falaises = trouver_falaises(grille)

    if falaises !=[]:

        memoire.append(deepcopy(grille))

        col = random.choice(falaises)

        jouer_falaise(grille,col)

        dessiner_grille()

    else:
        messagebox.showinfo("Info","Tas stable")


        

# lance une démonstration automatique :
# répète des étapes jusqu'à ce que le tas soit stable

def demo_auto():

    if not est_stable(grille):

        une_etape()

        can.after(300,demo_auto)

    else:

        messagebox.showinfo("Info","Démo terminée")

        

# modde joueur
# permet de cliquer sur une colonne pour jouer si c'est une falaise

def mode_joueur(event):

    global grille

    col = event.x // TAILLE_CASE #pour récupererla colonne cliquer avec la souris
 

    falaises = trouver_falaises(grille) 

    if col in falaises:    

        memoire.append(deepcopy(grille))

        jouer_falaise(grille,col)

        dessiner_grille()

        if est_stable(grille):

            messagebox.showinfo("Info","Le tas est stable")

can.bind("<Button-1>", mode_joueur)

# mode rretour en arrière: pour revenir à l'etape précédente de la grille

def oups():

    global grille

    if memoire !=[]:

        grille = memoire.pop() #supprimer la dernière mémoire enregistrer

        dessiner_grille()

    else:

        messagebox.showinfo("Info","Pas d'étape précédente")

        

#pour lancer une nouvelle partie:
 #créeation d' une nouvelle grille aléatoire et vide la memoire
def nouvelle_partie():

    global grille
    global memoire

    grille = tas_aleatoire(nbl,nbcol)

    memoire = []

    dessiner_grille()


# initialisation:
#pour crere une grille aléatoire au démarrage et l'affiche

grille = tas_aleatoire(nbl,nbcol)

dessiner_grille()

# les boutons
tk.Button(fen,text="Démo",command=demo_auto).grid(row=1,column=0)
tk.Button(fen,text="1 étape",command=une_etape).grid(row=1,column=1)
tk.Button(fen,text="Oups",command=oups).grid(row=1,column=2)
tk.Button(fen,text="Nouvelle partie",command=nouvelle_partie).grid(row=1,column=3)
tk.Button(fen,text="Quitter",command=fen.destroy).grid(row=1,column=4)

fen.mainloop()
