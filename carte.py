class carte():
    #les carte spéciale se répartisse en plusieur famille :
    # les +2 possédant une couleur action "+2" V
    # les +4 possédant ne possédant pas de couleur action "+4"
    # les changement de couleur action "chcouleur" 
    # changement de sens avec une couleur "chsens" V
    # interdiction de jouer avec une couleur "interdit" V
    def __init__(self,valeur,spe,couleur=""):
        self.spe = spe
        self.valeur = valeur
        self.couleur = couleur
        
    def isSpe(self):
        return self.spe
    
    def __repr__(self):

        if self.couleur == "rouge":
            return '\033[31m' + self.couleur + " " + str(self.valeur) + '\033[39m'
        if self.couleur == "bleu":
            return '\033[34m' + self.couleur + " " + str(self.valeur) + '\033[39m'
        if self.couleur == "vert":
            return '\033[32m' + self.couleur + " " + str(self.valeur) + '\033[39m'
        if self.couleur == "jaune":
            return '\033[33m' + self.couleur + " " + str(self.valeur) + '\033[39m'
        
        return '\033[37m' + self.couleur + " " + str(self.valeur) + '\033[39m'

