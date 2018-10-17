# -*- coding: utf-8 -*-
import Basics as lp
import pandas as pd
import numpy as np
from random import randint
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegressionCV
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import SGDClassifier
##################################################
data = pd.read_csv("data6.txt" )
x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values
'''
import matplotlib.pyplot as plt
plt.scatter(x , y)
plt.show(')
'''

y = lp.LABLEENCODER(y , 2)
'''
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
x2 = scale.fit_transform(x)
'''
##################################################
def TRAIN_TEST_SPLIT(X_var , Y_var , TEST_SIZE = None , RAND_STATE = None):
	if TEST_SIZE == None :
		TEST_SIZE = randint(1,3)*10
	try:
		from sklearn.cross_validation import train_test_split
	except DeprecationWarning as e:
		print (e , "NEED TO BE CHECKED !")
		from sklearn.model_selection import train_test_split
	return train_test_split(X_var , Y_var , test_size = TEST_SIZE/100 , random_state = RAND_STATE)


class Classification_Strategy_Method:
	def __init__(self , x=None , y=None):
		self.x = x
		self.y = y
		self.x_original = x
		self.y_original = y
	def Methods_Lists(X):
		out = {
				0:"K-Nearest" ,
				1 : "FOREST" ,
				2 : "TREE" ,
				3 : "ANN" ,
				4 : "SUPPORT VECTOR" ,
				5 : "LOGISTIC REGRESSION" ,
				6 : "GNB" ,
				7 : "Gradient Boosting Algorithms" ,
				8 : "Linear SGD training"
				}
		return (out[X])
	def Split(self):
		try :
			self.x , self.x_t , self.y , self.y_t = TRAIN_TEST_SPLIT(self.x_original , self.y_original)
		except TypeError as E :
			if self.x == None or self.y == None :
				raise Warning("YOU SHOULD INPUT X AND Y IN MAIN CLF OR IN AUTO FUNCTION")
			else :
				print(E)
				exit()
	def _Knear(self , Split = False):
		if Split != False :
			self.Split()
		self.knear = KNeighborsClassifier(n_jobs = -1)
		self.knear.fit(self.x , self.y)
		if Split != False :
			self.kscore = self.knear.score(self.x_t , self.y_t)
		if verbose is True :
			print("_Knear Done ! Result : " , self.kscore )
			return self.kscore
	def _NN(self , Split = False):
		if Split != False :
			self.Split()
		self.nn = MLPClassifier(max_iter = 1000)
		self.nn.fit(self.x , self.y)
		if Split != False :
			self.nscore = self.nn.score(self.x_t , self.y_t)
		if verbose is True :
			print("_nn Done ! Result : " , self.nscore )
			return self.nscore
	def _Forest(self , Split = False):
		if Split != False :
			self.Split()
		self.forestclf = RandomForestClassifier(n_jobs = -1)
		self.forestclf.fit(self.x , self.y)
		if Split != False :
			self.fscore = self.forestclf.score(self.x_t , self.y_t)
		if verbose is True :
			print("_forest Done ! Result : " , self.fscore )
			return self.fscore
	def _Tree(self , Split = False):
		if Split != False :
			self.Split()
		self.tree = DecisionTreeClassifier()
		self.tree.fit(self.x , self.y)
		if Split != False :
			self.treescore = self.tree.score(self.x_t , self.y_t)
			return self.treescore
	def _SV(self , Split = False):
		if Split != False :
			self.Split()
		self.sv = SVC()
		self.sv.fit(self.x , self.y)
		if Split != False :
			self.svscore = self.sv.score(self.x_t , self.y_t)
			return self.svscore
	def _LR(self , Split = False):
		if Split != False :
			self.Split()
		self.lr = LogisticRegressionCV()
		self.lr.fit(self.x , self.y)
		if Split != False :
			self.lrscore = self.lr.score(self.x_t , self.y_t)
			return self.lrscore
	def _GNB(self , Split = False):
		if Split != False :
			self.Split()
		self.gnb = GaussianNB()
		self.gnb.fit(self.x , self.y)
		if Split != False :
			self.gnbscore = self.gnb.score(self.x_t , self.y_t)
			return self.gnbscore
	def _GBC(self , Split = False):
		if Split != False :
			self.Split()
		self.gbc = GradientBoostingClassifier()
		self.gbc.fit(self.x , self.y)
		if Split != False :
			self.gbcscore = self.gbc.score(self.x_t , self.y_t)
			return self.gbcscore
	def _SGD(self , Split = False):
		if Split != False :
			self.Split()
		self.sgd = SGDClassifier(max_iter = 1000 , tol = 0.003)
		self.sgd.fit(self.x , self.y)
		if Split != False :
			self.sgdscore = self.sgd.score(self.x_t , self.y_t)
			return self.sgdscore
	def _OUT(self , SPLIT):
#		out = {
#				"K" : self._Knear(Split = SPLIT) ,
#				"NN" : self._NN(Split = SPLIT) ,
#				"FOREST" : self._Forest(Split = SPLIT) ,
#				"TREE" : self._Tree(Split = SPLIT) ,
#				"SV" : self._SV(Split = SPLIT) ,
#				}
		return [
				self._Knear(Split = SPLIT) ,
				self._Forest(Split = SPLIT) ,
				self._Tree(Split = SPLIT) ,
				self._NN(Split = SPLIT) ,
				self._SV(Split = SPLIT) ,
				self._LR(Split = SPLIT) ,
				self._GNB(Split = SPLIT) ,
				self._GBC(Split = SPLIT) ,
				self._SGD(Split = SPLIT) ,
				]
	def _Backend_Core(self , SPLIT_ = True , X = None , Y = None , verbose = False):
		if (self.x.__bool__  == None or self.y.__bool__ == None):
			if (X.__bool__== None or Y.__bool__ == None) :
				raise Warning("YOU SHOULD INPUT X AND Y IN MAIN CLF OR IN AUTO FUNCTION")
			else :
				self.x = X
				self.y = Y
				self.x_original = X
				self.y_original = Y
		if verbose is True :
			print (self._OUT(SPLIT = SPLIT_))
			return self._OUT(SPLIT = SPLIT_)
		else :
			return self._OUT(SPLIT = SPLIT_)
	def Best_Loop_val(self):
		sm = len(self.x[0])*len(self.x)
		if sm < 10000 :
			return 5
		elif sm < 35000 :
			return 4
		elif sm < 65000 :
			return 3
		elif sm < 100000 :
			return 2
		else :
			return 1
	def Evaluation_Best_Strategy_Core(self , SPLIT_ = True , x = None , y = None , verbose = False ,
									 Accuracy = 1 , Mode = 'name'):
		Accuracy = Accuracy*self.Best_Loop_val()
		Startegies_performance = []
		for i in range(Accuracy):
			Startegies_performance.append(self._Backend_Core(SPLIT_ = SPLIT_ , X = x , Y = y , verbose = verbose))
		Startegies_performance = np.average(Startegies_performance , axis = 0)
		self.best_startegy = pd.Series(Startegies_performance).idxmax()
		self.Strategies_result = Startegies_performance
		return self.best_startegy
	def __best__(self):
		try :
			print (Classification_Strategy_Method.Methods_Lists(self.best_startegy))
			return self.Strategies_result
		except AttributeError as e :
			raise Warning("THE COMPUTATION FOR DETERMINING BEST STRATEGY HAS NOT BEEN RUN YET THE VALUE OF BEST STRATEGY HAVE NOT FOUND MAKE SURE TO RUN THE FUNCTION 'AUTO' FIRST ")


test = Classification_Strategy_Method(x , y)
test.Evaluation_Best_Strategy_Core(verbose = True , Accuracy= 10)
res2 = test.__best__()
