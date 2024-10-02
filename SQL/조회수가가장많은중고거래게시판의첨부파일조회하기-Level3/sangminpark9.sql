SELECT
    CONCAT("/home/grep/src/",
           f.BOARD_ID, "/",
           f.FILE_ID,
           f.FILE_NAME,
           f.FILE_EXT ) AS FILE_PATH
FROM USED_GOODS_BOARD AS b
JOIN USED_GOODS_FILE AS f ON f.BOARD_ID = b.BOARD_ID
WHERE b.VIEWS = (SELECT
                    MAX(VIEWS)
                FROM USED_GOODS_BOARD)
ORDER BY f.FILE_ID DESC

/*
CONCAT("/home/grep/src/",
           f.BOARD_ID, "/",
           f.FILE_ID,
           f.FILE_NAME,
           f.FILE_EXT ) AS FILE_PATH
*/
