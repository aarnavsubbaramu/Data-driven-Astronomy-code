# Write a time_stat function to time our statistic implementations.
#time_stat should take three arguments: the func function we're timing, the size of the random array to test, and the number of experiments to perform.
#It should return the average running time for the func function.

import numpy as np
import statistics
import time

def time_stat(function,size,n):
  total = 0
  for i in range(n):
    data = np.random.rand(size)
    start = time.time()
    res = function(data)
    total += time.time() - start
  return(total/n)
