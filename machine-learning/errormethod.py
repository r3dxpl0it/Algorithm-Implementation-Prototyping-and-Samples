'''_____________________________________________________________________
|[] R3DXPL0IT SHELL                                            |ROOT]|!"|
|"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"| 
|CODED BY > R3DXPLOIT(JIMMY)                                          | |
|EMAIL > RETURN_ROOT@PROTONMAIL.COM                                   | |
|GITHUB > https://github.com/r3dxpl0it                                | |
|WEB-PAGE > https://r3dxpl0it.Github.io                               |_|
|_____________________________________________________________________|/|
'''
import numpy as Np
def ERROR_METHOD(REAL , PRED , error_type = 'relative' , mode = 'avg'):
	if error_type =='relative' :
		if mode == 'avg':
			return Np.average(abs(REAL - PRED)/abs(REAL));
		elif mode == 'array' :
			return abs(REAL - PRED)/abs(REAL);
	elif error_type == 'abs' :
		if mode == 'avg':
			return Np.average(abs(REAL - PRED));
		elif mode == 'array' :
			return abs(REAL - PRED);
