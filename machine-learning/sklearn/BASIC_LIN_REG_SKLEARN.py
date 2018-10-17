
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class Linear_Regression():
	def __init__(self , X_TRAINER , Y_TRAINER , X_TESTER=None  , Y_TESTER=None):
		self.X_TRAINER = X_TRAINER
		self.Y_TRAINER = Y_TRAINER
		if X_TESTER  != None and Y_TESTER != None :
			self.X_TESTER = X_TESTER
			self.Y_TESTER = Y_TESTER
	def Apply(self , N_JOBS = -1):
		clf = LinearRegression(n_jobs=N_JOBS)
		clf.fit(self.X_TRAINER , self.Y_TRAINER)
		self.clf = clf
	def Split(self , TESTSIZE  = 0.2 , Rand = None):
		self.X_TRAINER , self.X_TESTER , self.Y_TRAINER , self.Y_TESTER = TRAIN_TEST_SPLIT(self.X_TRAINER
																				 , self.Y_TRAINER , TESTSIZE = TESTSIZE , RAND_STATE=Rand)
	def Prediction(self , New_data = None) :
		if New_data != None:
			 return self.clf.predict(New_data)
		elif New_data == None and self.X_TESTER != None:
			 return self.clf.predict(self.X_TESTER)
		else :
			raise Warning("IF DIDNT PASS ANY THING FOR TEST SET NEW_DATA SHOULDNT LEFT BLANK!")
	def Fit_new(self , X):
		self.Apply()
		self.clf.fit()
	def Draw(self, TITLE = None , X_lab= None , Y_lab = None , Show = None):
		if self.X_TESTER == None or self.Y_TRAINER == None :
			raise Warning("PLOTING WITHOUT TEST SET IS NOT POSSIBLE")
		else :
			try :
				plt.scatter(self.X_TRAINER , self.X_TRAINER , color ='red')
				plt.scatter(self.X_TESTER , self.Y_TESTER , color = 'blue' )
				plt.plot(self.X_TRAINER ,self.clf.predict(self.X_TRAINER) , color = 'green')
				if TITLE != None :
					plt.title(TITLE)
				if X_lab != None : plt.xlabel(X_lab)
				if Y_lab != None:   plt.ylabel(Y_lab)
				if Show != None :
				   plt.show()
			except AttributeError :
				self.Apply()
	def return_clf(self):
		self.Apply()
		return self.clf
