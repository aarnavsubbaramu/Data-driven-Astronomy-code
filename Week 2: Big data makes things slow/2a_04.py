#Write a find_closest function that takes a catalogue and the position of a target source (a right ascension and declination) and finds the closest match for the target source in the catalogue.
#Your function should return the ID of the closest object and the distance to that object.

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

def angular_dist(ra1, dec1, ra2, dec2):

  #convert degree to radians since NumPy trigonometric functions only take radians as input
  r1 = np.radians(ra1)
  d1 = np.radians(dec1)
  r2 = np.radians(ra2)
  d2 = np.radians(dec2)

  a = np.sin((d2-d1)/2)**2 #since a=sin2|δ1−δ2|2
  b = np.cos(d1)*np.cos(d2)*np.sin((r1-r2)/2)**2 #since b=cosδ1cosδ2sin2|α1−α2|2
  ang_distance = 2*np.arcsin(np.sqrt(a + b)) #since d=2arcsin√(a+b)
  dec_deg = np.degrees(ang_distance) #convert from radians back to degrees

  return(dec_deg)

def find_closest(cat, ra, dec):
  min_dist = np.inf
  min_id = None
  for (id1, ra1, dec1) in cat:
    dist = angular_dist(ra1, dec1, ra, dec)
    if dist < min_dist:
      min_id = id1
      min_dist = dist

  return(min_id, min_dist)
