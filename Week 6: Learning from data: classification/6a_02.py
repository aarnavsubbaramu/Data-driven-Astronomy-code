#Next, we generate features and targets for the decision tree.
#The generate_features_targets function is mostly complete. However, you need to calculate the concentration values for the u, r and z filters.
#Your task is to calculate the concentration for each filter from the 50% and 90% Petrosian radius measurements:
  #conc=petroR50/petroR90

#As described earlier, data has the following fields:

    #colours: u-g, g-r, r-i, and i-z;
    #eccentricity: ecc
    #4th adaptive moments: m4_u, m4_g, m4_r, m4_i, and m4_z;
    #50% Petrosian: petroR50_u, petroR50_r, petroR50_z;
    #90% Petrosian: petroR90_u, petroR90_r, petroR90_z.



import numpy as np

def generate_features_targets(data):

  targets = data['class']
  #complete the function by calculating the concentrations
  features = np.empty(shape=(data.size, 13))              
  features[:, 0] = data['u-g']
  features[:, 1] = data['g-r']
  features[:, 2] = data['r-i']
  features[:, 3] = data['i-z']
  features[:, 4] = data['ecc']
  features[:, 5] = data['m4_u']
  features[:, 6] = data['m4_g']
  features[:, 7] = data['m4_r']
  features[:, 8] = data['m4_i']
  features[:, 9] = data['m4_z']

  #fill the remaining 3 columns with concentrations in the u, r and z filters
  features[:, 10] = data['petroR50_u']/data['petroR90_u']  #concentration in 'u' filter
  features[:, 11] = data['petroR50_r']/data['petroR90_r']  #concentration in 'r' filter
  features[:, 12] = data['petroR50_z']/data['petroR90_z']  #concentration in 'z' filter

  return(features, targets)

data = np.load('galaxy_catalogue.npy')
features, targets = generate_features_targets(data)

  #print the shape of each array to check the arrays are the correct dimensions.
print('Features shape:', features.shape)
print('Targets shape:', targets.shape)
