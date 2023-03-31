SELECT history_id
, car_id, date_format(start_date, '%Y-%m-%d') as start_date
, date_format(end_date, "%Y-%m-%d") as end_date,
IF (datediff(end_date, start_date) + 1 >= 30 ,'장기 대여', '단기 대여') AS RENT_TYPE 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE MONTH(start_date) = 9 && YEAR(start_date) = 2022
ORDER BY history_id DESC;