#Mean of a list.
#Write a function calculate_mean that calculates the mean of a list of numbers.
#Your solution cannot use the builtin statistics module.

def calculate_mean(data):
  mean = sum(data)/len(data)
  return(mean)
