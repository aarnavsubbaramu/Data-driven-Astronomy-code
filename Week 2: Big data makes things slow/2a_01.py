#Write two functions, one that converts right ascension from HMS to decimal degrees, called hms2dec, and another that converts declination from DMS to decimal degrees, called dms2dec.
#Right ascension is always an angle from 0 to 24 hours.
#Declination is always an angle from -90° to +90°.


#right asecnsion (from HMS to decimal degrees)
def hms2dec(hr, mit, sec):
  degree = 15*(hr + (mit/60) + (sec/(60*60)))
  return(degree)

#declination (from DMS to decimal degrees)
def dms2dec(d, arc_min, arc_sec):
  if d > 0:
    deg = d + (arc_min/60) + (arc_sec/(60*60))
  elif d < 0:
    deg = -1*((-d) + (arc_min/60) + (arc_sec/(60*60)))

  return(deg)
