import joueur
import carte
import random as rd
import copy

class coup():
    def __init__(self,gh,joueur,carte=None):
        self.carte = carte
        self.gh = gh
        self.joueur = joueur
        self.derniereCarte = self.gh.defausse.derniere_carte()

    def isValide(self):
        if self.carte.isSpe() and self.carte.couleur =="":
            return True
        else:
            return (self.derniereCarte.couleur == self.carte.couleur) or (self.derniereCarte.valeur == self.carte.valeur)
    
    def joueCoups(self):
        if self.isValide():
            if self.carte.isSpe():
                if self.carte.valeur == "+2": #cas d'un +2
                    if self.gh.sens == 0:
                        for i in range(2):
                            if self.gh.idJoueur != len(self.gh.joueurs)-1:
                                self.gh.pioche.pickOne(self.gh.joueurs[self.gh.idJoueur+1].main)
                            else:
                                self.gh.pioche.pickOne(self.gh.joueurs[0].main)
                    else:
                        for i in range(2):
                            self.gh.pioche.pickOne(self.gh.joueurs[self.gh.idJoueur-1].main)
                    self.chgJoueur()

                if self.carte.valeur == "+4": #cas d'un +4

                    if self.gh.sens == 0:
                        for i in range(4):
                            if self.gh.idJoueur != len(self.gh.joueurs)-1:
                                self.gh.pioche.pickOne(self.gh.joueurs[self.gh.idJoueur+1].main)
                            else:
                                self.gh.pioche.pickOne(self.gh.joueurs[0].main)
                    else:
                        for i in range(4):
                            self.gh.pioche.pickOne(self.gh.joueurs[self.gh.idJoueur-1].main)
                    couleur = input("Quel couleur souhaitez vous ?")
                    self.carte.couleur = couleur
                    self.chgJoueur()

                if self.carte.valeur == "chcouleur": #cas d'un joker
                    couleur = input("Quel couleur souhaitez vous ?")
                    self.carte.couleur = couleur

                if self.carte.valeur == "chsens": #cas de la carte de changement de sens
                    if self.gh.sens == 0 :
                        self.gh.sens = 1 
                    else :
                        self.gh.sens = 0

                if self.carte.valeur == "interdit": #cas d'un interdit
                   test = self.chgJoueur()#on change de joueur 2 fois

            if self.gh.defausse.derniere_carte().valeur == "chcouleur" or self.gh.defausse.derniere_carte().valeur == "+4" :
                self.gh.defausse.derniere_carte().couleur = ""

            self.gh.defausse.add(self.carte) #on met la carte dans la déffause et on l'enleve de la main
            self.joueur.main.remove(self.carte)

            #on passe au joueur d'aprés
            test = self.chgJoueur()
            return True,test
        else :
            print("le coups n'est pas valide, faite autre chose !")
            return False,False

    def chgJoueur(self):
        test = self.joueur.gagne()
        if self.gh.sens == 0:
            if self.gh.idJoueur == len(self.gh.joueurs)-1:
                self.gh.idJoueur = 0
            else:
                self.gh.idJoueur=self.gh.idJoueur+1 
        else:
            if self.gh.idJoueur == 0:
                self.gh.idJoueur = len(self.gh.joueurs)-1
            else:
                self.gh.idJoueur=self.gh.idJoueur-1 
        return test

    def pioche(self):
        self.joueur.main.piochee(self.gh.pioche)
        self.chgJoueur()
    
    def melange(self):
        if len(self.gh.pioche.tab) == 0:
            
            self.gh.pioche = copy.deepcopy(self.gh.defausse)
            carte = copy.deepcopy(self.gh.defausse[-1])
            self.gh.defausse.remove(carte)
            rd.shuffle(self.gh.defausse)
            self.gh.defausse = [carte]