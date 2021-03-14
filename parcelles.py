import tkinter as tk
import random as rd 

HEIGHT = 500
WIDTH = 500
largeur_case = WIDTH // 10
hauteur_case = HEIGHT // 10

class parcelles:

    def __init__(self,coordoneex,coordoneey):
        self.coordoneex = coordoneex
        self.coordoneey = coordoneey

    def get_coordonnee():
        return self.coordoneex,self.coordoneey

class eau(parcelles):

     def __init__(self,coordoneex,coordoneey):
        super().__init__(coordoneex,coordoneey)
        self.color = "blue"
    
    def get_color(self):
        return self.color


    
def random_parcelle():
    """ me les parcelles aléatoirement sur le terrain """
    canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
    canvas.grid()
    for i in range(10):
        for j in range(10):
            couleur=rd.randint(0,6)
            canvas = canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case))
                
            if couleur == 0:
                eau = eau( i , j  )
                canvas.config(fill=eau.get_color())


racine = tk.Tk() # Création de la fenêtre racine
random_parcelle()
racine.mainloop() # Lancement de la boucle principale