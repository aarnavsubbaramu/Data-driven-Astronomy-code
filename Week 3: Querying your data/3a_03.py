#In this question, write a query to find the kepler_name and radius of each planet in the Planet table which is a confirmed exoplanet - meaning that their kepler_name is not NULL, or, equivalently, whose status is 'CONFIRMED'.
#Restrict your results to those planets whose radius lies between one and three earth radii, and remember that the radius of the planets is relative to the earth radius.


SELECT kepler_name, radius FROM Planet WHERE kepler_name IS NOT NULL AND radius BETWEEN 1 AND 3; #'IS NOT NULL' checks for non-null kepler_name values

or

SELECT kepler_name, radius FROM Planet WHERE status = 'CONFIRMED' AND radius BETWEEN 1 AND 3;
