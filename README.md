# BITSoM_BA_25072062-fleximart-data-architecture

# FlexiMart Data Architecture Project

**Student Name:** Sonia Garg
**Student ID:** BITSoM_BA_25072062
**Email:** sonia30garg@gmail.com
**Date:** 08/01/2026

## Project Overview

I've created ETL pipeline in python code which is reading data from three csv files i.e, Customers_raw, Products and Sales_raw. 
After reading, cleaned and transformed the data i.e, proper email, phone and data format and ensure the coreect data types.
After cleaning, loaded the data in MySql tables to run the business queries.

## Repository Structure
├── part1-database-etl/
│   ├── etl_pipeline.py
│   ├── schema_documentation.md
│   ├── business_queries.sql
│   └── data_quality_report.txt
├── part2-nosql/
│   ├── nosql_analysis.md
│   ├── mongodb_operations.js
│   └── products_catalog.json
├── part3-datawarehouse/
│   ├── star_schema_design.md
│   ├── warehouse_schema.sql
│   ├── warehouse_data.sql
│   └── analytics_queries.sql
└── README.md

## Technologies Used

- Python 3.12.7, pandas, mysql-connector-python
- MySQL 9.0
- MongoDB 6.0

## Setup Instructions

### Database Setup

```bash
# Create databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run Part 1 - ETL Pipeline
python part1-database-etl/etl_pipeline.py

# Run Part 1 - Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

# Run Part 3 - Data Warehouse
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql


### MongoDB Setup

mongosh < part2-nosql/mongodb_operations.js

## Key Learnings

1. Leaned coding in Python, MYSQL and MongoDB

## Challenges Faced

1. Time was very limited to complete the assignment. And the time required to complete the assignemnt is more.
Please give extra time to complete it.
