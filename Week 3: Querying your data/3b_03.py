#To practise your outer joins, write a query which returns the kepler_id, t_eff and radius for all stars in the Star table which haven't got a planet as join partner.
#Order the resulting table based on the t_eff attribute in descending order.



SELECT kepler_id, t_eff, Star.radius
FROM Star LEFT OUTER JOIN Planet #to keep all entries in the 'Star' table while joining 
USING (kepler_id)
WHERE Planet.koi_name IS NULL #no planet partner
ORDER BY t_eff DESC;
