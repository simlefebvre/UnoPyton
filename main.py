import random as rd
import carte as ct
import copy

class set():
	def __init__(self):
		self.tab = []

	def __repr__(self):
		return str(self.tab)

	def add(self, carte):
		self.tab.append(copy.deepcopy(carte))
        
	def remove(self, carte):
		self.tab.remove(carte)
    
	def isIn(self, carte):
		return carte in self.tab
    	
	def pickOne(self, cible):
		cible.add(self.tab.pop())
    
class draw(set):
	def filling(self):
		for i in {'rouge','vert','bleu','jaune'}:
			for j in range(10):
				if j == 0 :
					carte = ct.carte(j,False,i)
					self.add(carte)
				else : 
					carte = ct.carte(j,False,i)
					self.add(carte)
					self.add(carte)
			self.add(ct.carte("+2",True,i))
			self.add(ct.carte("+2",True,i))
			self.add(ct.carte("chsens",True,i))
			self.add(ct.carte("chsens",True,i))
			self.add(ct.carte("interdit",True,i))
			self.add(ct.carte("interdit",True,i))
		for i in {"+4","chcouleur"}:
			for j in range(4):
				self.add(ct.carte(i,True))
		self.melange()
	def melange(self):
		rd.shuffle(self.tab)

class hand(set):
	def piochee(self, pioche):
		pioche.pickOne(self)

class defausse(set): #liste du type queue (la derniere carte mise sera celle à l'indice le plus grand)
	def derniere_carte(self):
		return self.tab[-1]