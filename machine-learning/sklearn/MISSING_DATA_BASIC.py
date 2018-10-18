'''_____________________________________________________________________
|[] R3DXPL0IT SHELL                                            |ROOT]|!"|
|"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"| 
|CODED BY > R3DXPLOIT(JIMMY)                                          | |
|EMAIL > RETURN_ROOT@PROTONMAIL.COM                                   | |
|GITHUB > https://github.com/r3dxpl0it                                | |
|WEB-PAGE > https://r3dxpl0it.Github.io                               |_|
|_____________________________________________________________________|/|
'''
from sklearn.preprocessing import Imputer

def MISSING_DATA_BASIC(init_data , start_col , end_col , Missing_Val = 'NaN' ,  Strategy = 'median'):
	imputer = Imputer(missing_values= Missing_Val , strategy = Strategy)
	imputer = imputer.fit(init_data[:,start_col:end_col+1])
	init_data[:,start_col:end_col+1] = imputer.transform(init_data[:,start_col:end_col+1])


'''
#INDIRECT USAGE :

#MISSING VALUE PREDICTION (COL WIS)
MISSING_DATA_BASIC(X , start_col=1 , end_col=2)


#DIRECT USAGE :

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, FROM:TO])
X[:, FROM:TO] = imputer.transform(X[:, FROM:TO])
'''
