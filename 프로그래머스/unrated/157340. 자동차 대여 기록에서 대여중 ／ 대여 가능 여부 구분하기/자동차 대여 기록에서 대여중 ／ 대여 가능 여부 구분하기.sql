SELECT car_id,
    CASE
        WHEN max(end_date) >= '2022-10-16' THEN '대여중'
    ELSE '대여 가능'
    END AS AVAILABILITY
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE start_date <= '2022-10-16'
    -- 10-16 부터 대여중인 차를 조회
GROUP BY car_id
ORDER BY car_id DESC;