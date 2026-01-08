ENTITY: customers
Purpose:  
    Stores core information about each customer in the system.

Attributes:
    customer_id – Unique identifier for each customer (Primary Key)
    first_name – Customer’s first name
    last_name – Customer’s last name
    email – Customer’s email address (must be unique)
    phone – Customer’s phone number
    city – Customer’s city of residence
    registration_date – Date the customer registered in the system

Relationships:
    1:M relationship with orders  
    One customer can place many orders.
    The orders table contains a customer_id foreign key referencing customers(customer_id).

ENTITY: orders
Purpose:  
    Stores information about each order placed by a customer.

Attributes:
    order_id – Unique identifier for each order (Primary Key)
    customer_id – References the customer who placed the order (Foreign Key)
    order_date – Date the order was placed
    total_amount – Total monetary value of the order
    status – Current status of the order (e.g., Pending, Completed, Cancelled)

Relationships:
    One order can contain many order items (1:M with order_items)
    Many orders belong to one customer (M:1 with customers)

ENTITY: order_items
Purpose:  
    Stores item‑level details for each order.

Attributes:
    order_item_id – Unique identifier for each order item (Primary Key)
    order_id – References the order this item belongs to (Foreign Key)
    product_id – References the purchased product (Foreign Key)
    quantity – Number of units purchased
    unit_price – Price per unit at the time of purchase
    subtotal – Computed as quantity × unit_price

Relationships:
    Many order items belong to one order (M:1 with orders)
    Many order items reference one product (M:1 with products)

Normalization Explanation (3NF Justification)
This schema follows Third Normal Form (3NF) to ensure data consistency, reduce redundancy, and prevent anomalies. Each table represents a single, well‑defined entity: customers, orders, and order_items. All non‑key attributes in each table depend solely on the primary key. For example, in the customers table, attributes such as first_name, last_name, email, phone, and city depend only on customer_id. There are no transitive dependencies because no non‑key attribute depends on another non‑key attribute.

Functional Dependencies
customers:  
customer_id → first_name, last_name, email, phone, city, registration_date

orders:  
order_id → customer_id, order_date, total_amount, status

order_items:  
order_item_id → order_id, product_id, quantity, unit_price, subtotal

Avoiding Anomalies
Update anomaly: Customer details (e.g., email) appear only once in the customers table, preventing inconsistent updates.
Insert anomaly: A new customer can be added without requiring an order, because customers and orders are stored separately.
Delete anomaly: Deleting an order does not remove the customer, since customer data is independent of order records.

By ensuring each table stores only attributes directly related to its primary key, the design maintains data integrity and supports scalable transactional operations.

Sample Data Representation
customers
customer_id	first_name	last_name	email	phone	city	registration_date
C001	John	Doe	john@example.com	1234567890	New York	2024‑01‑01
C002	Jane	Smith	jane@example.com	9876543210	Chicago	2024‑01‑02
orders
order_id	customer_id	order_date	total_amount	status
1001	C001	2024‑01‑15	45999.00	Completed
1002	C002	2024‑01‑16	5998.00	Completed
order_items
order_item_id	order_id	product_id	quantity	unit_price	subtotal
1	1001	P001	1	45999.00	45999.00
2	1002	P004	2	2999.00	5998.00
