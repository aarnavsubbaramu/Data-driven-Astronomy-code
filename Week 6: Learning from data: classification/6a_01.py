#To start, we need to split the data into training and testing sets.
#Your task is to implement the splitdata_train_test function. It takes a NumPy array and splits it into a training and testing NumPy array based on the specified training fraction. The function takes two arguments and should return two values:
#Arguments

    #data: the NumPy array containing the galaxies in the form described in the previous slide;
    #fraction_training: the fraction of the data to use for training. This is a float between 0 and 1.

#The number of training rows should be truncated if necessary. For example, with a fraction of 0.67 and our 780 galaxies, the number of training rows is 780*0.67 = 722.6, which is truncated to 722 using int. The remaining row are to be used for testing.
#Return values

    #training_set: the first value is a NumPy array training set;
    #testing_set: the second value is a NumPy array testing set.

#Using the supplied driver code, and our input data and a fraction of 0.7, the program is to print the following values:

#Number data galaxies: 780
#Train fraction: 0.7
#Number of galaxies in training set: 546
#Number of galaxies in testing set: 234



import numpy as np

def splitdata_train_test(data, fraction_training):
  np.random.shuffle(data)                                 #to shuffle the rows of the data array in place 
  split = int(fraction_training*(data.size))
  return(data[:split], data[split:])

data = np.load('galaxy_catalogue.npy')
fraction_training = 0.7

(training, testing) = splitdata_train_test(data, fraction_training)

print('Number data galaxies:', data.size)                 #'<file_name>.size' has the same function as len(<file_name>)
print('Train fraction:', fraction_training)
print('Number of galaxies in training set:', len(training))
print('Number of galaxies in testing set:', len(testing))

