#Let's implement the binapprox algorithm to calculate the median of a list of numbers. This algorithm is quite complex, so we'll break it down into managable parts.
#Your task is to write two functions:
 #median_bins to calculate the mean, standard deviation and the bins (steps 1-6 on the previous slide);
 #median_approx which calls median_bins and then calculates the approximated median (steps 7-8).

import numpy as np

def median_bins(data, B):
  mean = np.mean(data)
  sd = np.std(data) #standard deviation

  #Initialise bins
  left_bin = 0
  bins = np.zeros(B)
  bin_width = 2*sd/B

  #Bin data
  for value in data:
    if value < mean - sd:
      left_bin += 1
    elif value < mean + sd:
      bin = int((value - (mean - sd))/bin_width)
      bins[bin] += 1
    #Ignore values above mean + std

  return(mean, sd, left_bin, bins)


def median_approx(values, B):
  #Call median_bins to calculate the mean, sd, and bins for the input values
  mean, sd, left_bin, bins = median_bins(values, B)

  #Position of the middle element
  N = len(values)
  mid = (N + 1)/2

  count = left_bin
  for b, bincount in enumerate(bins):
    count += bincount
    if count >= mid:
      #Stop when the cumulative count exceeds the midpoint
      break

  width = 2*sd/B
  median = (mean - sd) + width*(b + 0.5)
  return(median)
