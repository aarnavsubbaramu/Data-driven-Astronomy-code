#You need to find out how many planets in the Planet database are in a multi-planet system. Planets sharing the same star will have the same kepler_id, but different koi_name values.
#Your query should return a table in which each row contains the kepler_id of the star and the number of planets orbiting that star (i.e. that share this kepler_id).
#Limit your results to counts above one and order the rows in descending order based on the number of planets.


SELECT kepler_id, count(koi_name) FROM Planet #count() returns the number of rows of 'koi_name'; 'koi_name' is the string identifier for each KOI (Kepler Object of Interest)
GROUP BY kepler_id #aggregates all values of kepler_id
HAVING count(koi_name) > 1
ORDER BY count(koi_name)  DESC; #orders the columns by descending count(koi_name)
