#Write a crossmatch function that crossmatches two catalogues within a maximum distance. Return a list of matches and non-matches for the first catalogue against the second.
#The list of matches contains tuples of the first and second catalogue object IDs and their distance. The list of non-matches contains the unmatched object IDs from the first catalogue only.
#Both lists are required to be ordered by the first catalogue's IDs.

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

def crossmatch(cat1, cat2, max_radius):
    matches = []
    no_matches = []
    for (id1, ra1, dec1) in cat1:
        closest_dist = np.inf
        closest_id2 = None
        for (id2, ra2, dec2) in cat2:
            dist = angular_dist(ra1, dec1, ra2, dec2)
            if dist < closest_dist: #least value algorithm
                closest_id2 = id2
                closest_dist = dist

        #Ignore match if it's outside the maximum radius
        if closest_dist > max_radius: #greatest value algorithm
            no_matches.append(id1)
        else:
            matches.append((id1, closest_id2, closest_dist))

    return(matches, no_matches)
