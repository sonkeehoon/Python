-- 자동차 대여 기록에서 장기/단기 대여 구분하기 : https://school.programmers.co.kr/learn/courses/30/lessons/144854
SELECT BOOK_ID, AUTHOR_NAME, date_format(PUBLISHED_DATE,'%Y-%m-%d')
FROM BOOK INNER JOIN AUTHOR ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
WHERE CATEGORY = '경제' ORDER BY PUBLISHED_DATE;
-- SELECT * FROM BOOK;