import numpy as np
from collections import Counter
def K_NEAREST(DATA = None , PREDICT = None , K = 5):
  DATA = np.any(DATA)
  if(DATA) >= K :
    raise Warning("K is set to a value less than total voting groups!")
  Dist = []
  for group in DATA :
    for Feature in DATA[group]:
      try :
        euclidean_distance = np.linalg.norm(np.array(Feature)-np.array(PREDICT))
      except ModuleNotFoundError or ImportError :
        euclidean_distance = np.sqrt(np.sum((np.array(Feature)-np.array(PREDICT))**2))
  Dist.append([euclidean_distance,group])
  votes = [i[1] for i in sorted(Dist)[:K]]
  vote_result = Counter(votes).most_common(1)[0][0]
  return vote_result
else :
  raise Warning("mode handeling error , Use Documentaion , Manual or Sample_Code")

