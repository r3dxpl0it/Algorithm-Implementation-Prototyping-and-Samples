import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import matplotlib.pyplot as plt

class Support_Vector_Regression():
	def __init__(self , X , Y , Auto = False):
		self.X = X
		self.Y = Y
		if Auto == True :
			Support_Vector_Regression.Auto(self)
	def Scale(self):
		Scaler_X = StandardScaler()
		Scaler_y = StandardScaler()
		self.X = Scaler_X.fit_transform(self.X)
		self.Y = Scaler_y.fit_transform(self.Y)
	def fit(self):
		clf = SVR(kernel='rbf')
		clf.fit(self.X , self.Y)
		self.clf = clf
#	def predict_Num(self):
#		return Scaler_y.inverse_transform(regs.predict(Scaler_X.transform(np.array([[6.5]]))))
	def Draw(self , Linespace = True):
		if Linespace == True :
			linspace = np.arange(min(self.X) , max(self.X) , 0.1)
			linspace = linspace.reshape((len(linspace) , 1 ))
		else :
			Linespace = self.X
		plt.scatter(self.X , self.Y)
		plt.plot(linspace  , self.clf.predict(linspace))
	def Auto(self):
		self.Scale()
		self.fit()
		self.Draw()
	def return_clf(self):
		self.Apply()
		return self.clf


#TEST = Support_Vector_Regression(X , y , Auto=True)

'''
#SIMPLE SCALAR SHOULD BE USED EACH TIME FOR X(TEST AND TRAIN) AND Y(TRAIN)
from sklearn.preprocessing import StandardScaler
Scaler_X = StandardScaler()
Scaler_y = StandardScaler()
X = Scaler_X.fit_transform(X)
y = Scaler_y.fit_transform(y)
from sklearn.svm import SVR

regs = SVR(kernel='rbf')
regs.fit(X , y)
new_prediction = Scaler_y.inverse_transform(regs.predict(Scaler_X.transform(np.array([[6.5]]))))

import matplotlib.pyplot as plt
linspace = np.arange(min(X) , max(X) , 0.1)
linspace = linspace.reshape((len(linspace) , 1 ))
plt.scatter(X , y)
plt.plot(linspace  , regs.predict(linspace))
'''
