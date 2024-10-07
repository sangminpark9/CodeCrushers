WITH reviewer_cnt_t AS (
    SELECT MEMBER_ID, COUNT(*) AS reviewer_cnt
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
),
max_reviewer AS (
    SELECT MEMBER_ID
    FROM reviewer_cnt_t
    WHERE reviewer_cnt = (SELECT MAX(reviewer_cnt) FROM reviewer_cnt_t)
)
SELECT
    m.MEMBER_NAME,
    r.REVIEW_TEXT,
    DATE_FORMAT(r.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM REST_REVIEW AS r
JOIN MEMBER_PROFILE AS m ON m.MEMBER_ID = r.MEMBER_ID
JOIN max_reviewer As mr ON mr.MEMBER_ID = r.MEMBER_ID
ORDER BY REVIEW_DATE ASC, r.REVIEW_TEXT ASC
