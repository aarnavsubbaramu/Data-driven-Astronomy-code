#Your first task is to replicate the following SQL query:

#SELECT kepler_id, radius
#FROM Star
#WHERE radius > 1.0;

#The data is stored in stars.csv, with the kepler_id in the first column and the radius in the last.
#Write a function called query which takes the CSV filename as an argument and returns the data in a 2-column NumPy array.



import numpy as np

def query(file):
  values = np.loadtxt(file, delimiter = ',', usecols = (0,2))
  data = values[values[:, 1] > 1, :]    #returns an array of boolean (true/false) result for the given condition
  return(data)
