def naive_0() : 
	best_acc = 0.0 
	it = 0 
	while True : 
		w = np.random.standard_normal(size = (784 , 10))
		b = np.random.standard_normal(size = (10,))
		model.set_weights(weights =[w , b] )
		score = model.ecaluate(x_Test , y_test, verbose = 0)
		it += 1 
		if score[1] > best_acc : 
			best_acc = score[1] 
			print(best_acc) 
