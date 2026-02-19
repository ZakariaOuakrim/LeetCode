SELECT score,
DENSE_RANK() OVER(PARTITION BY id ORDER BY score DESC) as rank 
FROM scores

