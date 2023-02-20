SELECT order_id, product_id, DATE_FORMAT(out_date,'%Y-%m-%d') out_date, 
        CASE WHEN DATE_FORMAT(out_date,'%y-%m-%d') > '22-05-01' THEN '출고대기'
            WHEN DATE_FORMAT(out_date,'%y-%m-%d') <= '22-05-01' THEN '출고완료'
            ELSE '출고미정'
            END '출고여부'
FROM food_order
ORDER BY order_id