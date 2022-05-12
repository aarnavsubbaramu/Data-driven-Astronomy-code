#Write a get_features_targets function that splits the training data into input features and their corresponding targets. In our case, the inputs are the 4 colour indices and our targets are the corresponding redshifts.
#Your function is to return a tuple of:

    #features: a NumPy array of dimensions m ⨉ 4, where m is the number of galaxies;
    #targets: a 1D NumPy array of length m, containing the redshift for each galaxy.

#The data argument is the structured array described on the previous slide. The u flux magnitudes and redshifts are accessible as a column with data['u'] and data['redshift'].
#The four features are the colours u - g, g - r, r - i and i - z.


import numpy as np

def get_features_targets(data):
  features = np.zeros((data.shape[0], 4)) #'np.zeros()' creates an empty (axb) dimension array
  features[:, 0] = data['u'] - data['g']
  features[:, 1] = data['g'] - data['r']
  features[:, 2] = data['r'] - data['i']
  features[:, 3] = data['i'] - data['z']

  targets = data['redshift']
  return(features, targets)
