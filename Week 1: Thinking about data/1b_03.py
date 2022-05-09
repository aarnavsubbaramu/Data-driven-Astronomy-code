#Write a mean_datasets function that reads in a list of CSV files and returns an array of the mean of each cell in the data files.
#The files each contain n rows and m columns, giving a total of n x m cells. The individual cells are separated by commas, and all CSV files in the list will have the same number of rows and columns.
#The result should have the same dimensions as the input files. The result should be a NumPy array with individual entries rounded to one decimal place.

import numpy as np

def mean_datasets(file):
  n = len(file)
  if n > 0:
    data = np.loadtxt(file[0], delimiter = ',') #1 #storing file as an array called data

    for i in range(1, n): #to load each element ([1], [2],..., [n]) in the file into the array 'data'
      data += np.loadtxt(file[i], delimiter = ',') #+= is to add each value of 'i' in range (1,n) to the 'data' variable (summation) stored from #1

    mean = data/n #similar to a list
    return(np.round(mean, 1))
