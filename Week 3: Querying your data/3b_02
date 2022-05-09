#Write a query which counts the number of planets in each solar system where the corresponding stars are larger than our sun (i.e. their radius is larger than 1).
#Your query is required to return the star's radius and its number of planets, showing only rows where the number of planets is more than one.
#Sort the rows in descending order based on the star radii.


SELECT Star.radius, COUNT(Planet.koi_name) #'COUNT' counts the number of values of the given variable
FROM Star JOIN Planet
USING (kepler_id)
WHERE Star.radius >= 1
GROUP BY Star.kepler_id
HAVING COUNT(Planet.koi_name) > 1
ORDER BY Star.radius DESC;
