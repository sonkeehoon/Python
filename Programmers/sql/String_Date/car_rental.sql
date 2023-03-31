-- 자동차 대여 기록에서 장기/단기 대여 구분하기 : https://school.programmers.co.kr/learn/courses/30/lessons/151138
SELECT history_id
, car_id, date_format(start_date, '%Y-%m-%d') as start_date
, date_format(end_date, "%Y-%m-%d") as end_date,
IF (datediff(end_date, start_date) + 1 >= 30 ,'장기 대여', '단기 대여') AS RENT_TYPE 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE MONTH(start_date) = 9 && YEAR(start_date) = 2022
ORDER BY history_id DESC;