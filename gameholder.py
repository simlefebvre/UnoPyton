import main
import joueur
import tour as tr
import random as rd

class gameHolder():
    def __init__(self):
        self.pioche = main.draw()
        self.pioche.filling()
        self.joueurs = []
        self.defausse = main.defausse()
        self.idJoueur = 0
        self.sens = 0 #0 : va de 0 à inf, 1 : vas de inf à 0
    def preparation(self):
        nbJoueur = input("Combien de Joueur voulez-vous ? ")
        nbJoueur = int(nbJoueur)
        for i in range(nbJoueur):
            nom = input("Quel est le nom du joueur "+ str(i) + " ? ")
            self.addJoueur(joueur.joueur(main.hand(),nom))

        self.distribution(nbJoueur) 
        self.pioche.pickOne(self.defausse)
        if self.defausse.derniere_carte().couleur == "":
            i = rd.randint(0,3)
            couleur = ['rouge','vert','bleu','jaune']
            c = couleur[i]
            self.defausse.derniere_carte().couleur = c
            
    def addJoueur(self, joueur):
        self.joueurs.append(joueur)
    def distribution(self, nombreJoueur):
        for j in range(7):
            for i in range(nombreJoueur):
                self.joueurs[i].main.piochee(self.pioche)

    def start(self):
        nbfin = 0 #nombre de joueur ayant terminer
        while(nbfin != len(self.joueurs)-1):
            test = False
            joueur =self.joueurs[self.idJoueur]
            while(joueur.isWin()):
                if self.sens == 0:
                    if self.idJoueur != 2:
                        self.idJoueur = self.idJoueur+1
                    else:
                        self.idJoueur = 0
                    joueur =self.joueurs[self.idJoueur] 
                else:
                    if self.idJoueur != 2:
                        self.idJoueur = self.idJoueur-1
                    else:
                        self.idJoueur = 0
                    joueur =self.joueurs[self.idJoueur] 
                
            print(joueur.nom,"c'est ton tour !")
            while(not test):
                joueur.afficheMain()
                print("la premiére carte sur le plateau est : ",self.defausse.derniere_carte())
                nCarte = input('Quelle carte voulais vous jouer ? (-1 pour piocher) ')
                if nCarte.isdigit() or nCarte == '-1':
                    nCarte = int(nCarte)
                    if nCarte > len(joueur.main.tab):
                        test = False
                    else:
                        if nCarte == -1:
                            t = tr.coup(self,joueur)
                            t.pioche()
                            test = True
                        else:
                            carte = joueur.main.tab[nCarte]
                            t = tr.coup(self,joueur,carte)
                            test,win = t.joueCoups()
                            if test and win:
                                nbfin = nbfin +1 
                else:
                    test = False
