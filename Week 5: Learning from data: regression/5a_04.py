#In this problem, we use median_diff from the previous question to validate the decision tree model.
#Your task is to complete the validate_model function.
#The function is to split the features and targets into train and test subsets, like this 50:50 split for features:

    #split = features.shape[0]//2
    #train_features = features[:split]
    #test_features = features[split:]

#Your function then uses the training split (train_features and train_targets) to train the model.
#Finally, it measures the accuracy of the model using median_diff on the test_targets and the predicted redshifts from test_features.

#The function is to take 3 arguments:

    #model: the decision tree regressor;
    #features - the features for the data set;
    #targets - The targets for the data set.



import numpy as np
from sklearn.tree import DecisionTreeRegressor

def get_features_targets(data):
  features = np.zeros((data.shape[0], 4))             #'np.zeros()' creates an empty (axb) dimension array
  features[:, 0] = data['u'] - data['g']
  features[:, 1] = data['g'] - data['r']
  features[:, 2] = data['r'] - data['i']
  features[:, 3] = data['i'] - data['z']

  targets = data['redshift']
  return(features, targets)

def median_diff(predicted, actual):                   #median difference function
  error = np.median(np.abs(predicted - actual))
  return(error)

def validate_model(model, features, targets):         #function thet splits data into training and testing subsets
  split = 2*(features.shape[0]//3)
  train_features, test_features = features[:split], features[split:]
  train_targets, test_targets = targets[:split], targets[split:]

  model.fit(train_features, train_targets)            #to train the model
  prediction = model.predict(test_features)           #to produce predicted redshifts
  return(median_diff(test_targets, prediction))       #to calculate accuracy with the median difference function

data = np.load('sdss_galaxy_colors.npy')
(features, targets) = get_features_targets(data)

dtree = DecisionTreeRegressor()
dif = validate_model(dtree, features, targets)        #to validate the model
print('Median difference is:', np.round(dif, 3))
