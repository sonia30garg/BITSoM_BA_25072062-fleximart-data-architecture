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
