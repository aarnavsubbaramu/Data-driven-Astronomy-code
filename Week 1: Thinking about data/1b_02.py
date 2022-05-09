#Mean of a 1D array.
#Write a calc_stats function that reads data from a CSV file and calculates its mean and the median.
#Your function should take the name of the file as an argument and return the mean and median in a tuple, rounded to one decimal place.
#Your solution cannot use the builtin statistics module.

import numpy as np

def calc_stats(file):
  data = np.loadtxt(file, delimiter = ',')
  mean = np.mean(data)
  median = np.median(data)
  return(np.round(mean,1), np.round(median,1)) #to round to 1 decimal place (np.round(mean,1))
