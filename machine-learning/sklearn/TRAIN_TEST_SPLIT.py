'''_____________________________________________________________________
|[] R3DXPL0IT SHELL                                            |ROOT]|!"|
|"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"| 
|CODED BY > R3DXPLOIT(JIMMY)                                          | |
|EMAIL > RETURN_ROOT@PROTONMAIL.COM                                   | |
|GITHUB > https://github.com/r3dxpl0it                                | |
|WEB-PAGE > https://r3dxpl0it.Github.io                               |_|
|_____________________________________________________________________|/|
'''
try:
	from sklearn.cross_validation import train_test_split
except DeprecationWarning as e:
	print (e , "NEED TO BE CHECKED !")
from sklearn.model_selection import train_test_split

def TRAIN_TEST_SPLIT(X_var , Y_var , TEST_SIZE = 20 , RAND_STATE = None):

	return train_test_split(X_var , Y_var , test_size = TEST_SIZE/100 , random_state = RAND_STATE)

'''#DATA SPLITING IN 2 GROUPS (TEST/TRAIN):
	X_Train,X_Test,Y_Train,Y_Test = TRAIN_TEST_SPLIT(X , Y , TEST_SIZE=10)		'''


#DIRECT USAGE FROM SKLEARN
'''
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
'''
