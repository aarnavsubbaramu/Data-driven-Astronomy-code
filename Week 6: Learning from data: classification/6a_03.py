#It is time to use the functions we wrote to split the data and generate the features, and then train a decision tree classifier.
#Your task is complete the dtc_predict_actual function by following the Python comments.
#The purpose of the function is to perform a held out validation and return the predicted and actual classes for later comparison.
#The function takes a single argument which is the full data set and should return two NumPy arrays containing the predicted and actual classes respectively.



import numpy as np
from sklearn.tree import DecisionTreeClassifier


#copy your splitdata_train_test function here
def splitdata_train_test(data, fraction_training):
  np.random.shuffle(data)
  split = int(fraction_training*(data.size))
  return(data[:split], data[split:])


#copy your generate_features_targets function here
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


#complete this function by splitting the data set and training a decision tree classifier
def dtc_predict_actual(data):
  #split the data into training and testing sets using a training fraction of 0.7
  (train, test) = splitdata_train_test(data, 0.7)

  #generate the feature and targets for the training and test sets i.e. train_features, train_targets, test_features, test_targets
  (train_features, train_targets) = generate_features_targets(train)
  (test_features, test_targets) = generate_features_targets(test)

  #instantiate a decision tree classifier
  dtree = DecisionTreeClassifier()

  #train the classifier with the train_features and train_targets
  dtree.fit(train_features, train_targets)

  #get predictions for the test_features
  predictions = dtree.predict(test_features)

  #return the predictions and the test_targets
  return(predictions, test_targets)
