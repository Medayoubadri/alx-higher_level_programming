-- Calculate and display the average temperature by city
-- In Gotham, it's always freezing. Elsewhere? Let's find out.

SELECT city, ROUND(AVG(temperature), 4) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
