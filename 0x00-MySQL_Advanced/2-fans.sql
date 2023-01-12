-- A sql script that ranks origins of bands by no of fans
-- in descending(order highest to lowest)
SELECT `origin`, `fans` FROM metal_bands ORDER BY `fans` DESC;
