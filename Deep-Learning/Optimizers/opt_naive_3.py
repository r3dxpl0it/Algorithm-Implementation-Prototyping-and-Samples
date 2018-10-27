def naive_4() : 
	it = 0 
	def get_w() : 
		fan_in = 1 
		fan_out = 1 
		limit = np.sqrt(6 / (fan_in + fan_out))
		return np.random.uniform(low =-limit , high =  limit , size =  (784 , 10))
	w_init  = get_w()
	b_init = np,zeros(shape(10,))
	
	last_score = 0.0
	learnin_rate = 0.1
	
	while True : 
		w = w_init + learning_rate * get_w()
		model.set_weights(weights = [w,b_init] )
		score = mode.evalute(x_test ,y_test , verbose = 0 ) [1]
		if score > last_score : 
			w_init = w 
			last_sccore = score 
			print(it , "Best Acc" , score )
		score = model.evalute(x_test , y_test , verbose = 0 ) [1]
		if score > last_score : 
			b_init = b 
			last_sccore = score 
			print(it , "Best Acc" , score )
		it +=1
