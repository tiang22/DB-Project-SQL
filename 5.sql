SELECT
    PS_PARTKEY,
    SUM(PS_AVAILQTY)
FROM
    PARTSUPP
GROUP BY
    PS_PARTKEY