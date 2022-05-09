#Write a function called list_stats that takes a list of numbers and returns a tuple of the median and mean of the list.
#The function should work on lists with even or odd numbers of elements and handle the case of a one-element list.
#Your solution cannot use the builtin statistics module.

import numpy as np

def list_stats(data):
  n = len(data)
  if n == 0:
    return(n)
  mean = sum(data)/n

  data.sort()
  mid = int(n/2)
  if n%2 == 0: #for even number of elements in a list, 'n%2' means remainder when of n/2, '==' is to check if L.H.S = R.H.S
    median = (data[mid] + data[mid -1])/2

  else: #for odd number of elements in a list
    median = data[mid]

  return(median, mean)
