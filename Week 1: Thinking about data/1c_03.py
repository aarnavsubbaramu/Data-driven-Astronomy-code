#Write a median_fits function which takes a list of FITS filenames, loads them into a NumPy array, and calculates the median image (where each pixel is the median of that pixel over every FITS file).
#Your function should return a tuple of the median NumPy array, the time it took the function to run, and the amount of memory (in kB) used to store all the FITS files in the NumPy array in memory.
#The running time should include loading the FITS files and calculating the median.

import time
import numpy as np
from astropy.io import fits

def median_fits(file):
    start = time.time()   #start timer

    FITS = []  #read in all the FITS files and store in a list
    for file_name in file:
      hdu = fits.open(file_name)
      FITS.append(hdu[0].data)
      hdu.close()


    FITS_stack = np.dstack(FITS) #stack image arrays in 3D array for median calculation

    median = np.median(FITS_stack, axis=2)

    memory = FITS_stack.nbytes  #calculate the memory consumed by the data
    #or, equivalently:
    #memory = 200 * 200 * len(file) * fits_stack.itemsize

    memory /= 1024 #convert to kB; /= divides L.H.S by R.H.S and then assigns the end product to the L.H.S

    stop = time.time() - start #stop timer to calculate total time
    return(median, stop, memory)
