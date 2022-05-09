#Write a load_fits function that loads in a FITS file and finds the position of the brightest pixel (i.e. the maximum value) in its image data.
#To make this function work for arbitrary files, pass the name of the FITS file as an argument to the function.

from astropy.io import fits #flexible image transport system

import numpy as np

def load_fits(file):
  hdu = fits.open(file)
  data = hdu[0].data

  largest = np.argmax(data) #argmax function searches for the largest value in the array and returns the position of that value
  pix = np.unravel_index(largest, data.shape) #unravel_index function brings the tuple back to the inital data array dimension

  return(pix)
