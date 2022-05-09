#Write a function called angular_dist that calculates the angular distance between any two points on the celestial sphere given their right ascension and declination.
#Your function should take arguments in decimal degrees and return the distance in decimal degrees too.

import numpy as np

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
