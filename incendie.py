#######################################################################################################
# Groupe BI TD4
# Antony MONCLER
# Michel ALAND
# Claude LOUEMBET
# Samy
# Ruben 
https://github.com/uvsq22007891/PROJET_groupe5
#######################################################################################################

import tkinter as tk
import random as rd 

HEIGHT = 500
WIDTH = 500
largeur_case = WIDTH // 10
hauteur_case = HEIGHT // 10
#######################################################################################################
"""Cette fonction permet de charger une suavegarde de lasimulation des parcelles"""

def charge (event):
    pass

# Ruben AMOYAL
#######################################################################################################

def random_parcelle(event):
    """ me les parcelles aléatoirement sur le terrain """
    canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
    canvas.grid()
    for i in range(10):
        for j in range(10):
            couleur=rd.randint(0,6)
            if couleur == 0:
                color="blue"
            if couleur == 1:
                color="green"
            if couleur == 2:
                color="red"
            if couleur == 3:
                color="yellow"
            if couleur == 4:
                color="grey"
            if couleur == 5:
                color="black"
            canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)
#######################################################################################################
def sauvegarde(save):
    """ permet d'enregistrer les données de la partie actuelle """
    fichier = open("fichier.txt","w")

    with open("fichier.txt", 'wb') as save:
        pickle.dump(fichier,save)



    

def charge(save):
    """ permet de chargerles données de la partie précédente """
    with open('fichier.txt','rb') as save:
        chargement= pickle.load(save)


racine = tk.Tk() # Création de la fenêtre racine

racine.mainloop() # Lancement de la boucle principale