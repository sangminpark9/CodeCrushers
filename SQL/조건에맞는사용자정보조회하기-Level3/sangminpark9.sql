SELECT 
    u.USER_ID,
    u.NICKNAME,
    CONCAT(u.CITY,' ',
           u.STREET_ADDRESS1,' ',
           u.STREET_ADDRESS2) AS 전체주소,
    CONCAT(LEFT(u.TLNO, 3), '-',
           SUBSTRING(u.TLNO,4,4), '-',
           RIGHT(u.TLNO,4)
          )AS 전화번호
FROM USED_GOODS_USER as u
JOIN (SELECT
    *,
    COUNT(*) as cnt
FROM USED_GOODS_BOARD
GROUP BY WRITER_ID
HAVING cnt >= 3) as t ON t.WRITER_ID = u.USER_ID
ORDER BY USER_ID DESC
