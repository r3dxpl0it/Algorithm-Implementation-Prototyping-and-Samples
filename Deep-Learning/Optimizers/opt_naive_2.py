def naive_2() : 
	it = 0 
	w_init = np.random.standard_normal(size = (784 , 10))
	b_init = np.random.standard_normal(size = (10,))
	last_score =  0.0
	learning_rate = 0.1 
	while True : 
		w = w_init + learning_rate * np.random.standard_normal(size = (784 , 10))
		b = b_init + learning_rate *np.random.standard_normal(size = (10,))
		model.set_weights(weights =[w , b] )
		score = model.ecaluate(x_Test , y_test, verbose = 0)[1]
		it += 1
	
