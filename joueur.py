class joueur():
    def __init__(self,main,nom):
        self.main = main
        self.nom = nom
        self.fini = False

    def __repr__(self):
        return self.nom + " a la main : " + str(self.main) + "a terminer ? " + str(self.fini)

    def gagne(self):
        if len(self.main.tab) == 0:
            print("Félicitation tu as termine !")
            return True
        else : 
            return False

    def isWin(self):
        return len(self.main.tab) ==0

    def afficheMain(self):
        tMain = self.main.tab
        for index,value in enumerate(tMain):
            print("carte n°",str(index),":",str(value))