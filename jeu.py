import pyxel
import labyrinthe
import ennemi
import vaisseau

class Jeu:
    """"""

    directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self):
        pyxel.init(128, 128)
        pyxel.mouse(visible=True)
        self.lab = labyrinthe.Labyrinthe()
        self.dire = 1
        self .vso = vaisseau.Vaisseau(self.lab.coords[2][0])
        self.ennemis = [ennemi.Ennemi(self.lab.coords[3][5][0],
                                      self.lab.coords[3][5][1],
                                      1),
                        ennemi.Ennemi(self.lab.coords[6][8][0],
                                      self.lab.coords[6][8][1],
                                      2),
                        ennemi.Ennemi(self.lab.coords[12][4][0],
                                      self.lab.coords[12][4][1],
                                      3),
                        ennemi.Ennemi(self.lab.coords[17][15][0],
                                      self.lab.coords[17][15][1],
                                      4)]


    def draw(self):
        self.lab.dessine()
        self.vso.dessine(self.dire, self.lab)
        for ennemi in self.ennemis:
            ennemi.mouvement()
            ennemi.dessine()


     def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.dire = 1
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.dire = 2
        elif pyxel.btn(pyxel.KEY_UP):
            self.dire = 4
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.dire = 3
        else:
            self.dire = 1

jeu = Jeu()
pyxel.run(jeu.update, jeu.draw)

