'''_____________________________________________________________________
|[] R3DXPL0IT SHELL                                            |ROOT]|!"|
|"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"| 
|CODED BY > R3DXPLOIT(JIMMY)                                          | |
|EMAIL > RETURN_ROOT@PROTONMAIL.COM                                   | |
|GITHUB > https://github.com/r3dxpl0it                                | |
|WEB-PAGE > https://r3dxpl0it.Github.io                               |_|
|_____________________________________________________________________|/|
'''
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from numpy import arange

class Poly_Regressor():
	def __init__(self , X , Y , X_t=None , Y_t = None 	, Degree = 2 ):
		self.X = X
		self.Y = Y
		if X_t and Y_t != None :
			self.X_t = X_t
			self.Y_t = Y_t
		self.Degree = Degree
	def Split(self , TESTSIZE  = 0.2 , Rand = None):
		self.X , self.X_t , self.Y , self.Y_t = TRAIN_TEST_SPLIT(self.X
																				 , self.Y , TESTSIZE = TESTSIZE , RAND_STATE=Rand)

	def _new_x(self):
		self.poly_reg = PolynomialFeatures(degree= self.Degree)
		self.New_X = self.poly_reg.fit_transform(self.X)
	def _apply_new_x (self):
		self.poly_reg.fit(self.New_X , self.Y)
		self.clf_poly = LinearRegression(n_jobs= -1)
		self.clf_poly.fit(self.New_X ,  self.Y)
	def Apply(self):
		Poly_Regressor._new_x(self)
		Poly_Regressor._apply_new_x(self)
	def Draw(self ,over_right = False , Linespace = 100 ):
		import matplotlib.pyplot as plt
		if AttributeError :
			Poly_Regressor.Apply(self)
		linspace = arange(min(self.X) , max(self.X) , 1/Linespace)
		linspace = linspace.reshape(len(linspace) ,1 )
		if over_right != True:
			plt.cla()
		plt.scatter(self.X , self.Y)
		plt.plot(linspace , self.clf_poly.predict(self.poly_reg.fit_transform(linspace)))
		plt.show()
	def return_new_x(self):
		self.Apply()
		return self.New_X
	def return_clf_reg(self):
		self.Apply()
		return self.clf_poly , self.poly_reg

