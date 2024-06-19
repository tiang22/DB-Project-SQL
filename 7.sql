SELECT
    *
FROM
    CUSTOMER AS C
WHERE
    EXISTS (
        SELECT
            *
        FROM
            CUSTOMER AS C_,
            ORDERS AS O
        WHERE
            O.O_CUSTKEY = C_.C_CUSTKEY
            AND O.O_TOTALPRICE < 10000
            AND C_.C_CUSTKEY = C.C_CUSTKEY
    )