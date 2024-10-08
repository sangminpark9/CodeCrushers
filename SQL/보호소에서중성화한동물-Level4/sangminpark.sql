WITH first_ch_t AS (
    SELECT ANIMAL_ID
    FROM ANIMAL_INS
    WHERE SEX_UPON_INTAKE NOT LIKE "%Spayed%" AND
          SEX_UPON_INTAKE NOT LIKE "%Neutered%"
)
SELECT
    o.ANIMAL_ID,
    o.ANIMAL_TYPE,
    o.NAME
FROM ANIMAL_OUTS AS o
JOIN first_ch_t AS it ON it.ANIMAL_ID = o.ANIMAL_ID -- 처음에 중성화 아닌
WHERE o.SEX_UPON_OUTCOME LIKE "%Spayed%" OR
      o.SEX_UPON_OUTCOME LIKE "%Neutered%"
ORDER BY o.ANIMAL_ID
