#Write a query which queries both the Star and the Planet table and calculates the following quantities:

    #the average value of the planets' equilibrium temperature t_eq, rounded to one decimal place;
    #the minimum effective temperature t_eff of the stars;
    #the maximum value of t_eff;
#Your query is required to only use those star-planet pairs whose stars have a higher temperature (t_eff) than the average star temperature in the table. Try to use a subquery to solve this problem!


SELECT ROUND(AVG(Planet.t_eq), 1), MIN(Star.t_eff), MAX(Star.t_eff)
FROM Star JOIN Planet
USING (kepler_id)
WHERE Star.t_eff > (
  SELECT AVG(t_eff) FROM Star #sub-query
);
