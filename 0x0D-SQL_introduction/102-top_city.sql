-- Display the top 3 cities based on average temperature in July and August
-- Summer vibes.

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
