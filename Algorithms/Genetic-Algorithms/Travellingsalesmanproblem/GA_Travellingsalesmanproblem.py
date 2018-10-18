'''_____________________________________________________________________
|[] R3DXPL0IT SHELL                                            |ROOT]|!"|
|"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"| 
|CODED BY > R3DXPLOIT(JIMMY)                                          | |
|EMAIL > RETURN_ROOT@PROTONMAIL.COM                                   | |
|GITHUB > https://github.com/r3dxpl0it                                | |
|WEB-PAGE > https://r3dxpl0it.Github.io                               |_|
|_____________________________________________________________________|/|
'''
import matplotlib.pyplot as plt
import numpy as np

CITIES_SIZE = 50 
CROSS_OVER_RATE = 0.01
MUTATE_RATE = 0.01
POPULATION_SIZE = 1000
MAX_GEN = 100


class GENETIC_ALG(object):
    def __init__(self, indivitual_size, cross_over, mutation_rate, pop_size, ):
        self.indivitual_size = indivitual_size
        self.cross_over = cross_over
        self.mutate_rate = mutation_rate
        self.pop_size = pop_size

        self.pop = np.vstack([np.random.permutation(indivitual_size) for _ in range(pop_size)])

    def read_ch(self, DNA, city_position): 
        line_x = np.empty_like(DNA, dtype=np.float64)
        line_y = np.empty_like(DNA, dtype=np.float64)
        for i, d in enumerate(DNA):
            city_coord = city_position[d]
            line_x[i, :] = city_coord[:, 0]
            line_y[i, :] = city_coord[:, 1]
        return line_x, line_y

    def get_fitness(self, line_x, line_y):
        total_distance = np.empty((line_x.shape[0],), dtype=np.float64)
        for i, (xs, ys) in enumerate(zip(line_x, line_y)):
            total_distance[i] = np.sum(np.sqrt(np.square(np.diff(xs)) + np.square(np.diff(ys))))
        fitness = np.exp(self.indivitual_size * 2 / total_distance)
        return fitness, total_distance

    def select(self, fitness):
        idx = np.random.choice(np.arange(self.pop_size), size=self.pop_size, replace=True, p=fitness / fitness.sum())
        return self.pop[idx]

    def crossover(self, parent, pop):
        if np.random.rand() < self.cross_over:
            i_ = np.random.randint(0, self.pop_size, size=1)                       
            cross_points = np.random.randint(0, 2, self.indivitual_size).astype(np.bool)   
            keep_city = parent[~cross_points]                                       
            swap_city = pop[i_, np.isin(pop[i_].ravel(), keep_city, invert=True)]
            parent[:] = np.concatenate((keep_city, swap_city))
        return parent

    def mutate(self, child):
        for point in range(self.indivitual_size):
            if np.random.rand() < self.mutate_rate:
                swap_point = np.random.randint(0, self.indivitual_size)
                swapA, swapB = child[point], child[swap_point]
                child[point], child[swap_point] = swapB, swapA
        return child

    def launch(self, fitness):
        pop = self.select(fitness)
        pop_copy = pop.copy()
        for parent in pop:
            child = self.crossover(parent, pop_copy)
            child = self.mutate(child)
            parent[:] = child
        self.pop = pop


class TPS(object):
    def __init__(self, n_cities):
        self.city_position = np.random.rand(n_cities, 2)
        plt.ion()

    def draw(self, lx, ly, total_d):
        plt.cla()
        plt.scatter(self.city_position[:, 0].T, self.city_position[:, 1].T, s=100, c='blue')
        plt.plot(lx.T, ly.T, 'black')
        plt.text(-0.05, -0.05, "Total distance=%.2f" % total_d, fontdict={'size': 20, 'color': 'green'})
        plt.xlim((-0.1, 1.1))
        plt.ylim((-0.1, 1.1))
        plt.pause(0.01)

try : 
	ga = GENETIC_ALG(indivitual_size=CITIES_SIZE, cross_over=CROSS_OVER_RATE, mutation_rate=MUTATE_RATE, pop_size=POPULATION_SIZE)
	env = TPS(CITIES_SIZE)
	temp = 0
	for generation in range(MAX_GEN):
		lx, ly = ga.read_ch(ga.pop, env.city_position)
		fitness, total_distance = ga.get_fitness(lx, ly)
		ga.launch(fitness)
		best_idx = np.argmax(fitness)
		if temp < best_idx  : 
			temp = best_idx 
			print('Gen:', generation, '| best fit: %.2f' % fitness[temp],)
		env.draw(lx[best_idx], ly[best_idx], total_distance[best_idx])
	plt.ioff()
	plt.show()
except KeyboardInterrupt : 
	quit()
