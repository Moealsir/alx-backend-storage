-- glam rock
SELECT band_name, 
  CASE 
	WHEN split IS NULL THEN 2022 - formed    
	ELSE split - formed
END AS lifespan
FROM metal_bands 
WHERE FIND_IN_SET('Glam rock', REPLACE(style, ', ', ',')) > 0
ORDER BY lifespan DESC LIMIT 100;
