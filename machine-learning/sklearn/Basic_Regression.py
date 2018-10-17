

#X_var = np.array([1 , 2, 3 ,4, 5 , 6] , dtype = np.float64)
#Y_var = np.array([5 ,4 ,6, 5, 6 ,7] , dtype = np.float64)


import numpy as np
from statistics import mean
#import warnings
class Basic_Regression:
	def __init__(self,x , y ):
#	def __init__(self,x , y , xt = None , yt = None):
		self.x = x
		self.y =y
#		if xt != None :
#			self.xt = xt
#		if yt !=None :
#			self.yt = yt
#		self.line = Regression.fit(self , self.x , self.y)
	def slope(self , x , y):
		 return (((mean(x)*mean(y)) - mean(x*y))/((mean(x)*mean(x)) - mean(x*x)))
	def intercept(self , x , y):
		 return (mean(y) - self.slope(x,y)*mean(x))
	def fit(self , x , y , x_test=None , y_test=None):
		self.x = x
		self.y = y
#		if x_test == None or y_test == None :
#			warnings.warn("X AND Y FOR TESTING SET HAVE NOT BEEN IMPORTED")
		self.line = [(X*self.slope(x,y))+self.intercept(x,y) for X in x ]
		return self.line
	def mean_squared_err(original , array):
		return sum((original - array)**2)
	def determination(self):
		y_mean_ln = [mean(self.y) for ys in self.y]
#		regression_err = Regression.mean_squared_err(self.y , Regression.fit(self , self.x , self.y))
#		y_mean_err = Regression.mean_squared_err(self.y , y_mean_ln)
		return 1 - (self.mean_squared_err(self.y , self.fit(self.x , self.y))
			   / self.mean_squared_err(self.y , y_mean_ln))
	def draw(self , over_right = False):
		import matplotlib.pyplot as plt
		if over_right != True:
			plt.cla()
		plt.scatter(self.x, self.y)
		plt.plot(self.x , self.fit(self.x , self.y))
		plt.show()
	def draw3d(self):
		import matplotlib.pyplot as plt
#		from mpl_toolkits.mplot3d import Axes3D
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.scatter(self.x ,self.y)
		ax.plot(self.x , self.fit(self.x , self.y))
		plt.show()
'''
test = Regression(xs , ys)
print(test.determination())
test.draw(over_right=True)
'''

