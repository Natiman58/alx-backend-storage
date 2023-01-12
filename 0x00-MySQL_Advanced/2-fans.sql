-- A sql script that ranks origins of bands by total no of fans
-- in descending(order highest to lowest)
SELECT `origin`, SUM(`fans`) AS nb_fans FROM metal_bands GROUP BY `origin` ORDER BY nb_fans DESC;

