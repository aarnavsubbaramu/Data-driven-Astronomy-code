#Write import_bss and import_super functions that import the AT20G BSS and SuperCOSMOS catalogues from the files bss.dat and super.csv as described in the previous slides.
#Each function should return a list of tuples containing the object's ID (an integer) and the coordinates in degrees.
#The object ID should be the row of the object in the catalogue, starting at 1.

import numpy as np

def hms2dec(hr, m, sec):
  degree = 15*(hr + (m/60) + (sec/(60*60)))
  return(degree)

def dms2dec(d, arc_min, arc_sec):
  if d > 0:
    deg = d + (arc_min/60) + (arc_sec/(60*60))
  elif d < 0:
    deg = -1*((-d) + (arc_min/60) + (arc_sec/(60*60)))
  return(deg)

def import_bss():
  tup = []
  values = np.loadtxt('bss.dat', usecols = range(1, 7))
  for (x, row) in enumerate(values, 1):
    tup.append((x, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5])))
  return(tup)

def import_super():
  tup = []
  cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=(0, 1))
  for (x, row) in enumerate(cat, 1):
    tup.append((x, row[0], row[1]))
  return(tup)
  
