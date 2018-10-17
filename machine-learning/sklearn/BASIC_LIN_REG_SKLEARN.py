
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

	
	
	
#Another Version that i have Written for Another Test : 
#OLDER CODE :
#
'''
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def SINGLE_AND_MULTIPLE_LINEAR_REGRESSION_BASIC(X_TRAINER , Y_TRAINER , X_TESTER  , Y_TESTER ,
                        return_Table = False  , N_JOBS = 1):
	#Fit simple Linear Model with n_jobs
	Regs = LinearRegression(n_jobs=N_JOBS)
	Regs.fit(X_TRAINER , Y_TRAINER)
	#Predicting The Test_Set Results
	if return_Table == True:
		return 	Regs.predict(X_TESTER) , Regs.score(X_TESTER)

def SINGLE_LINEAR_REGRESSION_VPLUS(X_TRAINER , Y_TRAINER , X_TESTER  , Y_TESTER ,
					  visulizing_mode = False ,  return_Table = False  , N_JOBS = -1 ,
                       TITLE = None , X_lab= None , Y_lab = None , Show = None):
	#import Lib
	#Fit simple Linear Model with n_jobs
	Regs = LinearRegression(n_jobs=N_JOBS)
	Regs.fit(X_Train , Y_Train)
	#Predicting The Test_Set Results
	Y_Pred = Regs.predict(X_Test)
	if return_Table == True:
		return 	Regs.predict(X_TESTER) , Regs.score(X_TESTER)
	#Visualizing
	if visulizing_mode == True :
        plt.scatter(X_Train , Y_Train , color ='red')
        plt.scatter(X_Test , Y_Test , color = 'blue' )
        plt.plot(X_Train ,Regs.predict(X_Train) , color = 'green')
        if TITLE != None :
            plt.title(TITLE)
        if X_lab != None :
            plt.xlabel(X_lab)
        if Y_lab != None :
            plt.ylabel(Y_lab)
        if Show != None :
            plt.show()


#ACC , PRED = SINGLE_AND_MULTIPLE_LINEAR_REGRESSION_BASIC(X_train , y_train , x_test , y_test)
#
#Regressor = LinearRegression()
#Regressor.fit(TRAIN_SET_X , TRAIN_SET_Y)
#Regressor.fit(TEST_SET_X)
#Regressor.score(TEST_SET_X , TEST_SET_Y)
'''
	
