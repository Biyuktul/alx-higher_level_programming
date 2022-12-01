-- displaying the average temprature by city
-- ordered by temperature descending in mysql

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
