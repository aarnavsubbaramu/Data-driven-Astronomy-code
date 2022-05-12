#Your task is to put this together for our photometric redshift data.
#Copy your get_features_targets from the previous problem. Use the comments to guide your implementation.
#Finally, print the first 4 predictions. It is to print this:

#[ 0.539301    0.1645703   0.04190006  0.04427702]



import numpy as np
from sklearn.tree import DecisionTreeRegressor

def get_features_targets(data):
  features = np.zeros((data.shape[0], 4))       #'np.zeros()' creates an empty (axb) dimension array
  features[:, 0] = data['u'] - data['g']
  features[:, 1] = data['g'] - data['r']
  features[:, 2] = data['r'] - data['i']
  features[:, 3] = data['i'] - data['z']

  targets = data['redshift']
  return(features, targets)

data = np.load('sdss_galaxy_colors.npy')       #to load the data to produce features and targets
(features, targets) = get_features_targets(data)

dtree = DecisionTreeRegressor()                #to initialize the decision tree regression learning algorithm
dtree.fit(features, targets)                   #to train the model
predictions = dtree.predict(features)          #to make a prediction

print(predictions[0:4])                        #to print out first 4 predictions of redshifts
