import keras 
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
batch_size = 128 
num_classes = 10 
epochs = 20 

(x_train , y_train) , (x_test , y_test) = mnist.load_data()
 
 
x_train = x_train.reshape(60000 , 784) 
x_test = x_test.reshape(10000 , 784) 
x_train = x_train.astype('float32') 
x_test = x_test.astype('float32') 
x_train /= 255
x_test /= 255
print (x_train.shape[0])
print(x_train.shape[0])

#Encoder with Keras 
y_train = keras.utils.to_categorical(y_train , num_classes) 
y_test = keras.utils.to_categorical(y_test , num_classes) 

model = Sequential() 
model.add(Dense(10 , activation = 'softmax' , input_shape = (784,)))

model.summary()

model.compile(loss = 'categorical_crossentropy', 
					optimizer = keras.optimizers.RMSprop() , 
					metrics = ['accuracy'] , 
					)
def naive_0() : 
	best_acc = 0.0 
	it = 0 
	while True : 
		w = np.random.standard_normal(size = (784 , 10))
		w = np.random.standard_normal(size = (10,))
		model.set_weights(weights =[w , b] )
		score = model.ecaluate(x_Test , y_test, verbose = 0)
		it += 1 
		if score[1] > best_acc : 
			best_acc = score[1] 
			print(best_acc) 
def naive_1() : 
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
