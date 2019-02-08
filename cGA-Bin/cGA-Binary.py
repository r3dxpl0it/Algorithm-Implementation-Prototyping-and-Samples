'''
|EMAIL > RETURN_ROOT@PROTONMAIL.COM                                   | |
|GITHUB > https://github.com/r3dxpl0it                                | |
|WEB-PAGE > https://r3dxpl0it.Github.io                               |_|
'''
from random import random
class CompactGeneticAlg : 
  
	def __init__(self) :
		self.bound = None 
  #Fitness Evaulation 
	def _Fitness_value_(self , ind) : 
		return self.fitness_function(ind) 
  #Create Simple Probob Vecotor 
	def _generate_probob_vec(self , probob = 0.5) : 
		return [probob] * self.size
  #Create random Population 
	def _generate_vd(self) : 
		if self.bound is not None : 
			raise NotImplementedError 
		value = str()
		for chor in self.indivitual : 
			value += "1" if random() < chor else "0"
		return self._Fitness_value_(value)
  #Compete two generated vectors 
	def compete(self, ind0 , ind1) : 
		if self._Fitness_value_(ind0) > self._Fitness_value_(ind1) : 
			self.winner = ind0
			self.loser = ind1
		else : 
			self.winner = ind1
			self.loser = ind0 
  #update
	def update_disturb(self) : 
		for i in range(len(self.indivitual)) : 
			if self.winner[i] != self.loser[i]:
				if self.winner[i] == '1':
					self.indivitual[i] += 1.0 / float(self.size)
				else:
					self.indivitual[i] -= 1.0 / float(self.size)
  #Initialize , For not Termination Status(max gen) : compete ! 
  #Update Best best on Compete()
	def evolve(self , generations, size, population_size, fitness_function , bound = None) : 
		self.maxgen = generations
		self.size = size
		self.popsize = population_size 
		self.indivitual = None 
		self.best = None
		self.fitness_function = fitness_function
		self.indivitual = self._generate_probob_vec()		
		for i in range(self.maxgen) : 
			s1 = self._generate_vd()
			s2 = self._generate_vd()
			self.compete(s1, s2)
			if self.best : 
				if self._Fitness_value_(self.winner) > self._Fitness_value_(self.best):
					self.best = self.winner 
					print ("generation: ",i + 1," best value: ",self.best," best fitness:",float(self._Fitness_value_(self.best)))
			else:
				self.best = self.winner
				print ("generation: ",i + 1," best value: ",self.best," best fitness:",float(self._Fitness_value_(self.best)))
			self.update_disturb()

if __name__ == '__main__':
	f = lambda x: x*2
	test = CompactGeneticAlg()
	test.evolve(100, 32, 10, f)
