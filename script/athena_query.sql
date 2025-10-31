-- athena_query.sql
-- Consulta para validar e transformar dados simulados

SELECT 
    id,
    value,
    date,
    CAST(value * 1.15 AS DECIMAL(10,2)) AS value_adjusted,
    DATE_FORMAT(date, '%Y-%m-%d') AS formatted_date
FROM raw_data.sample_data
WHERE value > 0;
