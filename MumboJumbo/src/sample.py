from Mumbo import MumboJumbo
Test = MumboJumbo(function=MumboJumbo.Benchmarks.Schwefel, minimization= True ,
                  initialization_bound=[-500 , 500] , termination = {'max_gen' : 1000 , 'max_n' : 0.001}  ,
                  initialization_sizing_method =  'differenziale' , dim = 100 , verbose=True , debug= False)
Test.evolve()
print(Test.result)