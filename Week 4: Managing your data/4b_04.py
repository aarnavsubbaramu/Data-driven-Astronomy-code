#Let's add another element to our query.
#Sort the resulting table in ascending order to match the result you get with:

#SELECT kepler_id, radius
#FROM Star
#WHERE radius > 1.0
#ORDER BY radius ASC;

#You can use your results from the last problem and then build up on that. Again, the function is to be named query and it is to take the filename as argument.




import numpy as np

def query(file):
  values = np.loadtxt(file, delimiter = ',', usecols = (0,2))
  data = values[values[:, 1] > 1, :]
  filter_data = data[np.argsort(data[:, 1]), :]        #'np.argsort()' sorts the elements of an array in ascending order
  return(filter_data)
