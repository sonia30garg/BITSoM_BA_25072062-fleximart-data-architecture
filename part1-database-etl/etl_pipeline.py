import pandas as pd
import mysql.connector

# Read Customers_raw data from csv file
customers_df = pd.read_csv("customers_raw.csv")


# Remove duplicates while keeping first entry
customers_df = customers_df.drop_duplicates(subset="customer_id", keep="first")

# Convert date formats to YYYY-MM-DD
customers_df["registration_date"] = pd.to_datetime(customers_df["registration_date"], dayfirst=True, errors="coerce")

# Filling missed emails in data
customers_df['email'] = customers_df.apply(
    lambda row: f"{row['first_name']}.{row['last_name']}@gmail.com"
    if pd.isna(row['email']) else row['email'],
    axis=1
)

# Remove all non-digit characters, keep last 10 digits, add +91-
customers_df["phone"] = (
    customers_df["phone"]
    .astype(str)
    .str.replace(r"\D", "", regex=True)   # remove everything except digits
    .str[-10:]                             # keep last 10 digits
    .apply(lambda x: f"+91-{x}" if pd.notnull(x) and len(x)==10 else x)
)

#----------------------------------- Product_raw-----------------------------------------
# Read product_raw data from csv file
products_df = pd.read_csv("products_raw.csv")
print(df1)

# 1. Standardize category names 
products_df["category"] = products_df["category"].str.strip().str.lower().str.capitalize()

# Fill missing price with median price of that category
products_df["price"] = products_df.groupby("category")["price"].transform(
    lambda x: x.fillna(x.median())
)

# Fill missing stock_quantity with median of that category
products_df["stock_quantity"] = products_df.groupby("category")["stock_quantity"].transform(
    lambda x: x.fillna(x.median())
)

# -----------------------------
# 3. Ensure correct data types
# -----------------------------
products_df["price"] = products_df["price"].astype(float)
products_df["stock_quantity"] = products_df["stock_quantity"].astype(int)


# 4. Remove unwanted space, leading and trailing spaces
products_df["product_name"] = (
    products_df["product_name"]
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

#-----------------------------------Sales_raw data--------------------------------------------
# Read Sales_raw data from csv file
sales_df = pd.read_csv("sales_raw.csv")
print(sales_df)

# Remove duplicate entries
sales_df = sales_df.drop_duplicates(subset=["transaction_id", "customer_id", "product_id"], keep="first")

# Convert transaction_date formats to YYYY-MM-DD
sales_df["transaction_date"] = pd.to_datetime( sales_df["transaction_date"], 
                                        dayfirst=True, 
                                        errors="coerce" 
                                       )

# ----------------------------- 
# 4. Standardize status values
# ----------------------------- 
sales_df["status"] = sales_df["status"].str.strip().str.capitalize()

# ----------------------------- 
# 5. Ensure numeric types 
# ----------------------------- 
sales_df["quantity"] = sales_df["quantity"].astype(int)
sales_df["unit_price"] = sales_df["unit_price"].astype(float)


# Filling the missing value with some unknown value
sales_df["customer_id"] = sales_df["customer_id"].fillna("UNKNOWN_CUSTOMER")
sales_df["product_id"]  = sales_df["product_id"].fillna("UNKNOWN_PRODUCT")

#Load a pandas DataFrame into a MySQL table using mysql.connector.
def load_dataframe_to_mysql(df, table_name, host, user, password, database):
    

    # Connect to MySQL 
    conn = mysql.connector.connect( 
        host=host, 
        user=user, 
        password=password, 
        database=database )

    cursor = conn.cursor()
    columns = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    data = [tuple(row) for row in customers_df.to_numpy()]
    cursor.executemany(query, data)
    conn.commit()
    print(f"{cursor.rowcount} rows inserted into '{table_name}'")
    cursor.close() 
    conn.close()

#Loading datasets to mysql by calling the function
load_dataframe_to_mysql(customers_df, "customers", "localhost", "root", "root_123", "fleximart")
load_dataframe_to_mysql(products_df, "products", "localhost", "root", "root_123", "fleximart")
load_dataframe_to_mysql(sales_df, "orders", "localhost", "root", "root_123", "fleximart")

