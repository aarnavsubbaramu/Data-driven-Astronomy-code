# Let's analyse the size of the unconfirmed exoplanets.
#Your task is to write a query that calculates the:

    #minimum radius;
    #maximum radius;
    #average radius; and
    #standard deviation of the radii

#of unconfirmed planets (with a NULL value in kepler_name) in the Planet tableSELECT min(radius), max(radius), avg(radius), stddev(radius) FROM Planet WHERE kepler_name IS NULL;


SELECT min(radius), max(radius), avg(radius), stddev(radius) FROM Planet WHERE kepler_name IS NULL; #'kepler_name' IS NULL is for 'UNCONFIRMED' exoplanets
