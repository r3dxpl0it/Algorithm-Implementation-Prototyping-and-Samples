'''_____________________________________________________________________
|[] R3DXPL0IT SHELL                                            |ROOT]|!"|
|"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"| 
|CODED BY > R3DXPLOIT(JIMMY)                                          | |
|EMAIL > RETURN_ROOT@PROTONMAIL.COM                                   | |
|GITHUB > https://github.com/r3dxpl0it                                | |
|WEB-PAGE > https://r3dxpl0it.Github.io                               |_|
|_____________________________________________________________________|/|
'''
import random 
POP_SIZE = 5 
TARGET = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]
MUT_RATE = .001
TOR_POP_SELECTION_SIZE = 4
ELITE = 1 		
SELECTION_SIZE = 4

class Choromos: 
	def __init__(self) : 
		self._genes = []
		self._fitness = 0
		for i in range(0 , len(TARGET)) : 
			if random.random() >= 0.5: 
				self._genes.append(1)
			else :
				self._genes.append(0)
	def get_genes(self) :
		return self._genes
	def get_fitness(self)  : 
		self._fitness = 0 
		for i in range (len(self._genes)): 
			if self._genes[i] is TARGET[i] : 
				self._fitness += 1 
		return self._fitness 
	def __str__(self)  : 
		return self._genes.__str__()
		
class Pop: 
	def __init__(self , size)  :
		self._Chor = []
		for i in range (size) : 
			self._Chor.append(Choromos())
	def get(self) : 
		return self._Chor
		
class Genetic_Alg : 
	@staticmethod 
	def Evol(pop) : 
		return Genetic_Alg._mut_pop(Genetic_Alg._crossover_pop(pop))


	@staticmethod 
	def _crossover_pop(pop) : 
		elite_pop = Pop(0)
		for i in range(ELITE) :
			elite_pop.get().append(pop.get()[i])
		i = ELITE 
		while i < POP_SIZE : 
			chrom1 = Genetic_Alg.selection_pop(pop).get()[0]
			chrom2 = Genetic_Alg.selection_pop(pop).get()[0]
			elite_pop.get().append(Genetic_Alg._crosover_chrom(chrom1,chrom2))
			i +=1 
		return elite_pop
	@staticmethod 


	def _mut_pop(pop) :
		for i in range(ELITE , POP_SIZE) : 
			Genetic_Alg._mut_chromosome(pop.get()[i])
		return pop

	@staticmethod 
	def _crosover_chrom(chrom1 , chrom2) :
		crosover_chrom = Choromos()
		for i in range(len(TARGET)) : 
			if random.random() >= 0.5 : 
				crosover_chrom.get_genes()[i] = chrom1.get_genes() [i]
			else :
				crosover_chrom.get_genes()[i] = chrom2.get_genes() [i]
		return crosover_chrom

	@staticmethod 	
	def _mut_chromosome(chrom) : 
		for i in range(len(TARGET)) : 
			if random.random() < MUT_RATE : 
				if random.random() < 0.5 : 
					chrom.get_genes()[i] = 1 
				else :
					chrom.get_genes()[i] = 0


	def selection_pop(pop)  : 
		tour_pop = Pop(0) 
		for i in range(TOR_POP_SELECTION_SIZE):
			tour_pop.get().append(pop.get()[random.randrange(0 , POP_SIZE)])
		tour_pop.get().sort(key = lambda x: x.get_fitness() , reverse = True )
		return tour_pop



def print_pop(pop , gen_num ) : 
	print ("---"*30)
	print ('Generation' , gen_num , 'Fittest : ' , pop.get()[0].get_fitness())
	print('Target:' , TARGET)
	print ("---"*30)
	i = 0 
	for foo in pop.get() : 
		print('Chormos : ',  i , "  :  "  , foo , 'FITNESS' , foo.get_fitness())
		i +=1  	

		
population = Pop(POP_SIZE)
population.get().sort(key = lambda x : x.get_fitness() , reverse = True)
print_pop(population , 0)
Generation_Number = 1 
while population.get()[0].get_fitness() < TARGET.__len__() : 
	population = Genetic_Alg.Evol(population)
	population.get().sort(key = lambda x : x.get_fitness() , reverse = True)
	print_pop(population , Generation_Number)
	Generation_Number += 1 

		
