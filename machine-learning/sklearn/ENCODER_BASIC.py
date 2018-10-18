'''_____________________________________________________________________
|[] R3DXPL0IT SHELL                                            |ROOT]|!"|
|"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"| 
|CODED BY > R3DXPLOIT(JIMMY)                                          | |
|EMAIL > RETURN_ROOT@PROTONMAIL.COM                                   | |
|GITHUB > https://github.com/r3dxpl0it                                | |
|WEB-PAGE > https://r3dxpl0it.Github.io                               |_|
|_____________________________________________________________________|/|
'''
#Lable Encode
def LABLEENCODER(init_data , cat_num , col = 0  , mode = 'basic' , Hot_encoder = False):
	from sklearn.preprocessing import LabelEncoder , OneHotEncoder
#	if (col != -1 and mode == 'basic') or (col == -1 and mode != 'basic') :
#		raise TypeError
	try :
		if mode == 'basic' :
			Encode_target = LabelEncoder()
			init_data= Encode_target.fit_transform(init_data)
			if Hot_encoder == True:
				O_H_E = OneHotEncoder(categorical_features = cat_num)
				init_data = O_H_E.fit_transform(init_data)
		if mode == 'express' :
			Encode_target = LabelEncoder()
			init_data[:,col] = Encode_target.fit_transform(init_data[:,col])
			if Hot_encoder == True:
				O_H_E = OneHotEncoder(categorical_features = cat_num)
				init_data = O_H_E.fit_transform(init_data).toarray()
		return init_data
	except TypeError :
		print("TYPE ERROR IN THE INPUT DATA")


'''
#DATA LABLE ENCODING (COL WIS)
X = LABLEENCODER( X, col = 0 , mode = 'express' , Hot_encode=True)
Y = LABLEENCODER(Y , mode = 'basic' )
'''
'''
# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
'''
