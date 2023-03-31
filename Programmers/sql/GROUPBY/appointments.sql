-- 진료과별 총 예약 횟수 출력하기 : https://school.programmers.co.kr/learn/courses/30/lessons/132202
SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE MONTH(APNT_YMD) = "5" AND YEAR(APNT_YMD) = "2022"
GROUP BY MCDP_CD,DATE_FORMAT(APNT_YMD,'%Y-%m')
ORDER BY 5월예약건수,진료과코드;