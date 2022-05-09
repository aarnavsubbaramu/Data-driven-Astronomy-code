#Write a query that returns the radius of each star and planet pair whose radii have a ratio greater than the Sun-to-Earth radius ratio.
#Order the results in descending order based on the stellar (star) radii.
#Use sun_radius and planet_radius as attribute aliases for the star and planet radii.


SELECT Star.radius AS sun_radius, Planet.radius AS planet_radius #selecting 'Star' table 'radius' values and 'Planet' table 'radius' values; 'AS' is used to give an alias for the 'Star' and 'Planet' radii
FROM Star, Planet
WHERE Star.kepler_id = Planet.kepler_id #so that the kepler_id from both tables match
AND Star.radius > Planet.radius
ORDER BY Star.radius  DESC;
