import numpy as np 
import math 
from random import random 
import random as rdm 
import itertools 
import time 
import os 
import sys 

class MumboJumbo() : 
    def __init__(self,
                 function,
                 optimum_fitness= None, 
                 initialization_sizing_method = 'default',
                 initialization_bound = None ,
                 termination = {} , 
                 #prelimetary_bound = None , 
                 minimization = True,
                 dim = None, 
                 verbose = False ,  
                 debug = False) :
        self.verbose = verbose 
        self.debug = debug
        if optimum_fitness is None :
            if random() < 0.5 : 
                wine_space = np.linspace(initialization_bound[0] , initialization_bound[1])
                if self.debug : 
                    print('NORMAL SPACE' , wine_space)
                self.optimum_fitness = function(wine_space)/(abs(function(wine_space)))
            else : 
                self.optimum_fitness = 0 
        else : 
            self.optimum_fitness = optimum_fitness
        if self.verbose : 
            print('OPTIMUM',self.optimum_fitness)
        else : 
            self.optimum_fitness = optimum_fitness
        if 'max_n' not in termination.keys() : 
            self.termination = {'max_n' : 0.0000000000001}
        else : 
            self.termination = { 'max_n' : termination['max_n']} 
        if 'max_gen' not in termination.keys() :
            self.termination = {'max_gen' : 1000}
        else :
            self.termination['max_gen'] = termination['max_gen']
        self.initialization_bound = initialization_bound
        if self.debug : 
            print(termination)
            print(self.initialization_bound)

        if type(self.initialization_bound) is not list :
            raise TypeError
        if minimization : 
            self.minimization = True
        else : 
            self.minimization = False 
        if '-inf' in self.initialization_bound : 
            self.bound1 = -10**10 

        elif 'inf' in self.initialization_bound : 
            self.bound2 = 10**10 
        else : 
            self.bound1 = self.initialization_bound[0]
            self.bound2 = self.initialization_bound[1]
        if dim is None : 
            self.dim = 10 
        else : 
            if type(dim) == int : 
                self.dim = dim 
            else : 
                raise TypeError
        if initialization_sizing_method is 'default' : 
            self._space_sizing = 100 
            self.method = 'default'
        else : 
            self.method = initialization_sizing_method
        self.function = function
        self.fitness = None 
        self.indivitual = None 

        self.termination = termination
    @staticmethod
    def _random_intract(b1 , b2 , dim) :
        b1 -= (rdm.betavariate(100,10000)*random() + rdm.betavariate(100,10000)) + (1/dim)
        b2 += (rdm.betavariate(100,10000)*random() + rdm.betavariate(100,10000)) + (1/dim)
        return b1,b2 
    def _initialization_bound(self)  : 
        if self.bound1 == self.bound2  : 
            self.bound1 , self.bound2 = self._random_intract(self.bound1 , self.bound2 , self.dim)
        self._space = np.linspace(self.bound1 , self.bound2, self.dim) 
        return self._space 
    def _selection_bound(self) : 
        self.indivitual_list_fail = list()
        for points in range(len(self._space)-1) :
            self.indivitual_list_fail.append(np.random.uniform(self._space[points] , self._space[points+1] , self.dim))
        return self.indivitual_list_fail
    def _defult(self , method = 'default'):
        if method is 'default' : 
            self.fitness_list = list()
            for ind_group in self.indivitual_list_fail : 
                a = abs(self.function(ind_group))
                self.fitness_list.append(a) 
            if self.debug: 
                print('FAIL' , self.indivitual_list_fail)
                print('IND LIST' , self.fitness_list)
                print('SELECTED' , self.indivitual_list_fail[np.argmin(self.fitness_list)])
            rt1 = self.indivitual_list_fail[np.argmin(self.fitness_list)]
            rt2 = self.function(self.indivitual_list_fail[np.argmin(self.fitness_list)])
            return rt1 , rt2
        elif method is 'differenziale' : 
            self.fitness_list = list()
            for ind_group in self.indivitual_list_fail : 
                #a =  abs(self.function(ind_group))
                a =  abs(abs(self.function(ind_group)) - abs(self.optimum_fitness))
                self.fitness_list.append(a) 
            if self.debug: 
                print('IND LIST' , self.indivitual_list_fail)
                print('FITNESS LIST' , self.fitness_list)
                print('IND SELECTED' , self.indivitual_list_fail[np.argmin(self.fitness_list)])
            rt1 = self.indivitual_list_fail[np.argmin(self.fitness_list)]
            rt2 = self.function(self.indivitual_list_fail[np.argmax(self.fitness_list)])
            rt2 = self.function(rt1)
            return rt1 , rt2
    def evolve(self , trial = 0 , max_run = None) :
        if self.debug : 
            print('Method:', self.method)
        if self.method is 'default' : 
            if max_run is None : 
                max_run = self.termination['max_gen']-1
            else :
                max_run -= 1
            self._initialization_bound()
            self._selection_bound()
            counter = 0 
            self.best_indivitual_ever , self.best_fitness_ever = self._defult(self.method)
            self.indivitual , self.fitness = self.best_indivitual_ever , self.best_fitness_ever
            self.best_generation = 0
            if self.verbose : 
                print('Generation' , counter , 'Fitness' , self.fitness , '\nInd' , self.indivitual)
            if self.minimization is True : 
                while (abs(self.best_fitness_ever) > abs(self.optimum_fitness+self.termination['max_n'])) or (abs(self.best_fitness_ever) < abs(self.optimum_fitness+self.termination['max_n'])) : 
                    self.bound1 = self.indivitual[0]
                    self.bound2 = self.indivitual[-1] 
                    self._initialization_bound()
                    self._selection_bound()  
                    self.indivitual , self.fitness = self._defult()

                    if counter > max_run :
                        if self.debug : 
                            print('Broke')
                        break
                    else : 
                        counter += 1 

                    if self.debug : 
                        print('Generation' , counter , 'Fitness' , self.fitness , 'Ind' , self.indivitual)
                    if abs(self.fitness) < abs(self.best_fitness_ever) : 
                        self.best_fitness_ever = self.fitness
                        self.best_indivitual_ever = self.indivitual 
                        self.best_generation = counter
                        if self.verbose : 
                            print('Generation' , counter , 'Fitness' , self.fitness , '\nInd' , self.indivitual)
                self.result = {'Function' :  self.function.__name__ , 
                      'Dimension': self.dim , 
                      'Method': self.method , 
                      'Best_Generation' : self.best_generation , 
                      'Last_Generation' : counter ,
                      'Best_Fitness' : self.best_fitness_ever ,
                      'Best_Indivial': [x for x in self.best_indivitual_ever]}
        if self.method is 'differenziale' : 
            if max_run is None : 
                max_run = self.termination['max_gen']-1
            else :
                max_run -= 1
            self._initialization_bound()
            self._selection_bound()
            counter = 0 
            self.best_indivitual_ever , self.best_fitness_ever = self._defult(self.method)
            self.indivitual , self.fitness = self.best_indivitual_ever , self.best_fitness_ever
            self.best_generation = 0
            if self.verbose : 
                print('Generation' , counter , 'Fitness' , self.fitness , '\nInd' , self.indivitual)
            if self.minimization is True : 
                while (abs(self.best_fitness_ever) > abs(self.optimum_fitness+self.termination['max_n'])) or (abs(self.best_fitness_ever) < abs(self.optimum_fitness+self.termination['max_n'])) : 
                    self.bound1 = self.indivitual[0]
                    self.bound2 = self.indivitual[-1] 
                    self._initialization_bound()
                    self._selection_bound()  
                    self.indivitual , self.fitness = self._defult()

                    if counter > max_run :
                        if self.debug : 
                            print('Broke')
                        break
                    else : 
                        counter += 1 

                    if self.debug : 
                        print('Generation' , counter , 'Fitness' , self.fitness , 'Ind' , self.indivitual)
                    if abs(self.fitness) < abs(self.best_fitness_ever) : 
                        self.best_fitness_ever = self.fitness
                        self.best_indivitual_ever = self.indivitual 
                        self.best_generation = counter
                        if self.verbose : 
                            print('Generation' , counter , 'Fitness' , self.fitness , '\nInd' , self.indivitual)
                self.result = {'Function' :  self.function.__name__ , 
                      'Dimension': self.dim , 
                      'Method': self.method , 
                      'Best_Generation' : self.best_generation , 
                      'Last_Generation' : counter ,
                      'Best_Fitness' : self.function(self.best_indivitual_ever) ,
                      'Best_Indivial': [x for x in self.best_indivitual_ever]}
        else :
            raise NotImplementedError
    def extended_evolve(self) : 
        self.total_eval = int(np.sqrt(self.termination['max_gen']))
        self.result_archive = {}
        for run in range(self.total_eval) : 
            self.evolve(trial = run , max_run = self.total_eval)
            self.result_archive[run] = self.result
        ls = []
        [ls.append(self.result_archive[item]['Best_Fitness']) for item in self.result_archive]
        best_run = np.argmin(ls)
        self.result = {'Number_of_Runs' : self.total_eval,
                       'Best_run' : best_run ,  
                       'Result' : self.result_archive[best_run]}
    def __str__(self) : 
        return self.result
    def __doc__(self) : 
        return '''
        #Call The Mumbo Jumbo 
        Test = MumboJumbo(function=Ros, minimization= True , optimum_fitness= 4 , 
                  initialization_bound=[-10 , 10] , termination = {'max_gen' : 10000 , 'max_n' : 0}  ,
                  dim = 100 , verbose=True , debug= False)
        #Start Evolving
        Test.evolve()
        #Print Class
        print(Test.result)
        
        Test.extended_evolve()
        print(Test.result_archive)
        print(Test.result)
        '''
    class Benchmarks : 
        def Ackley(ind) : 
            fitness = 0
            type(ind)
            for i in range(0 , len(ind)) :
                fitness += (-20 * math.exp(-0.2 * math.sqrt((ind[i]**2 + ind[i]**2)) / 2)) 
                fitness += -(math.exp((math.cos(2 * math.pi + ind[i]) + math.cos(2 * math.pi + ind[i]))/2)) 
                fitness += 20 + math.exp(1)
            return (fitness)
        def Sphere (ind):
            fitness = 0
            for i in range(0, len(ind)) :
                fitness += ind[i]**2
            return fitness
        def Rastrigin (ind):
            """ Classical Rastrigin with A=10 """
            A = 10
            fitness = A * len(ind) + sum([(x**2 - A * np.cos(2.0 * math.pi * x)) for x in ind])
            return fitness
        def Griewank (ind):
            fitness = f1 = 0
            f2 = 1
            for i in range(len(ind)) :
                f1 += ind[i]**2
                f2 *= math.cos(float(ind[i]) / math.sqrt(i+1))
                fitness += 1 + (float(f1)/4000.0) - float(f2)
            return -fitness
        def Zakh (ind):
            fitness = 0
            for i in range(0, len(ind)) :
                fitness += ind[i]+np.power(1/2*((i+1)*ind[i]),2)+np.power(1/2*((i+1)*ind[i]),4)
            return fitness
        def all_equal(ind):
            fitness = 0.0
            for a, b in itertools.permutations(range(len(ind)), 2):
                fitness += (ind[a] - ind[b])**2
            return (fitness)
        def Ros (ind):
            fitness = 0
            for i in range(0 , len(ind)-1) :
                fitness += (100*((ind[i]**2)-ind[i+1])**2)+(1-ind[i])**2
            return fitness
        def Schwefel (ind):
            fitness = 0
            fitness = (418.9828872724337998*len(ind)-sum(item*math.sin(math.sqrt(abs(item))) for item in ind))
            return fitness
        def Sty (ind):
            fitness = 0
            for i in range(0, len(ind)) :
                fitness += (ind[i]**4) - (16*ind[i]**2) +(5*ind[i])
            fitness /= float(2.0)
            return fitness