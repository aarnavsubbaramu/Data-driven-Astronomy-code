#Write a query which finds the radii of those planets in the Planet table which orbit the five largest stars in the Star table.
#Your query is required to return the planet's koi_name and radius as well as the corresponding star radius.


SELECT Planet.koi_name, Planet.radius, Star.radius
FROM Star JOIN Planet
USING (kepler_id)
WHERE Star.kepler_id IN (
  SELECT kepler_id FROM Star
  ORDER BY Star.radius DESC
  LIMIT 5 #five largest stars (radii-wise)
);
