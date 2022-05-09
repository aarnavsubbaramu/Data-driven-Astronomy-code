from astropy.io import fits
import numpy as np

def mean_fits(file):
  n = len(file)
  if n > 0:
    hdu = fits.open(file[0])
    data = hdu[0].data #1
    hdu.close() #to free memory of the file

    for i in range(1, n): #to load each element ([1], [2],..., [n]) in the file into the array 'data'
      hdu = fits.open(file[i])
      data += hdu[0].data #+= is to add each value of 'i' in range (1,n) to the 'data' variable (summation) stored from #1
      hdu.close()

    mean = data/n #similar to a list
    return(mean)
