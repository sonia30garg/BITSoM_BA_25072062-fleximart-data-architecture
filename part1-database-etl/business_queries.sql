SELECT 
    c.first_name,
    c.last_name,
    c.email,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.subtotal) AS total_amount_spent
FROM customers c
JOIN orders o 
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name, c.email
HAVING 
    COUNT(DISTINCT o.order_id) >= 2
    AND SUM(oi.subtotal) > 5000
ORDER BY 
    total_amount_spent DESC;


SELECT 
    p.category AS category,
    COUNT(DISTINCT p.product_id) AS num_products,
    SUM(oi.quantity) AS total_quantity_sold,
    SUM(oi.subtotal) AS total_revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY 
    p.category
HAVING 
    SUM(oi.subtotal) > 10000
ORDER BY 
    total_revenue DESC;



SELECT
    DATE_FORMAT(order_date, '%M') AS month_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.subtotal) AS monthly_revenue,
    SUM(SUM(oi.subtotal)) OVER (
        ORDER BY MONTH(order_date)
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue
FROM orders o
JOIN order_items oi 
    ON o.order_id = oi.order_id
WHERE YEAR(order_date) = 2024
GROUP BY MONTH(order_date), DATE_FORMAT(order_date, '%M')
ORDER BY MONTH(order_date);


