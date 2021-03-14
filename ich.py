class feu(parcelles):

    def __init__(self,color,coordoneex,coordoneey,duree_feu):
       self.couleur = color
       self.durée = duree_feu

    
class cendre_tiede(parcelles):

    def __init__(self,color,coordoneex,coordoneey,durée_tiede):
        self.couleur = color
        self.durée = durée_tiede

class prairie(parcelles):

    def __init__(self,couleur,durée):
        super().__init__(couleur, durée)
        self.couleur = "yellow"

class forêt(parcelles):

    def __init__(self,couleur,durée):
        super().__init__(couleur, durée)
        self.couleur = "green"

class cendres_éteinte(parcelles):

    def __init__(self,couleur,durée):
        self.couleur = "black"


def random_parcelle(event):
    """ me les parcelles aléatoirement sur le terrain """
    canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
    canvas.grid()
    for i in range(10):
        for j in range(10):
            couleur=rd.randint(0,6)
            if couleur == 0:
                eau = eau()
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



                            if couleur == 1:
                foret = foret(i,j)
                canvas.config(fill=foret.get_color())

            if couleur == 2:
                feu = feu(i,j)
                canvas.config(fill=feu.get_color())

            if couleur == 3:
                cendre_t = cendre_t(i,j)
                canvas.config(fill=cendre_t.get_color())

            if couleur == 4:
                prairie = prairie(i,j)
                canvas.config(fill=prairie.get_color())

            if couleur == 5:
                cendre_e = cendre_e(i,j)
                canvas.config(fill=cendre_e.get_color())
   

class feu(parcelles):

    def __init__(self,coordoneex,coordoneey):
        super().__init__(coordoneex,coordoneey)
        self.color = "red"
        self.duree_feu = 5
    
    def get_color(self):
        return self.color
    
class cendre_t(parcelles):

    def __init__(self,coordoneex,coordoneey):
        super().__init__(coordoneex,coordoneey)
        self.color = "grey"
        self.duree_tiede = 5
    
    def get_color(self):
        return self.color

class prairie(parcelles):

    def __init__(self,coordoneex,coordoneey):
        super().__init__(coordoneex,coordoneey)
        self.color = "yellow"
    
    def get_color(self):
        return self.color

class foret(parcelles):

    def __init__(self,coordoneex,coordoneey):
        super().__init__(coordoneex,coordoneey)
        self.color = "green"
    
    def get_color(self):
        return self.color

class cendre_e(parcelles):

    def __init__(self,coordoneex,coordoneey):
        super().__init__(coordoneex,coordoneey)
        self.color = "black"
    
    def get_color(self):
        return self.color
    