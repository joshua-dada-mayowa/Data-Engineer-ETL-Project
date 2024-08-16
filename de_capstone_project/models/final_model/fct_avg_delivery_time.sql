
{{ config(materialized='table') }}
SELECT
    ROUND(AVG(delivery_time_hours),2) AS avg_delivery_time_days
FROM
    {{ ref('int_avg_delivery_time') }}
