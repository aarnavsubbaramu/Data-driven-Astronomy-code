#In this problem we implement the function median_diff. The function calculates the median residual error of our model, i.e. the median difference between our predicted and actual redshifts.
#The median_diff function takes two arguments – the predicted and actual/target values.
#The median of differences is be calculated according to the formula: med_diff=median(|Yi,pred−Yi,act|)



import numpy as np

def median_diff(predicted, actual):                   #median difference
  error = np.median(np.abs(predicted[:] - actual[:])) #since med_diff = median(|Yi,pred−Yi,act|)

  return(error)

targets = np.load('targets.npy')                      #load actual redshift
predictions = np.load('predictions.npy')              #load predicted redshift

dif = median_diff(predictions, targets)

print('Median difference:', np.round(dif, 3))         #'np.round(<variable>, <number of places to round the variable to>)'
