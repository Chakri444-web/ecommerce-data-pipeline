# E-Commerce Data Pipeline – ETL Project

## Project Overview

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python and MySQL. It extracts raw e-commerce sales data from a CSV file, processes and transforms the data using Python, and loads the processed data into a MySQL database.

A Power BI dashboard is included to visualize the sales data and generate business insights.

## Project Architecture

```text
Raw CSV Dataset
      |
      ▼
Extract (Python)
      |
      ▼
Transform (Python)
      |
      ▼
Load (Python + MySQL)
      |
      ▼
Power BI Dashboard
```

## Technologies Used

- **Python** – ETL pipeline development and data processing
- **MySQL** – Relational database for storing processed data
- **SQLAlchemy** – Database connectivity
- **PyMySQL** – MySQL database driver
- **Power BI** – Data visualization and reporting
- **Git & GitHub** – Version control and project hosting

## Project Structure

```text
ecommerce-data-pipeline/
│
├── data/
│   └── raw/
│       └── ecommerce_sales_data.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── test_connection.py
│   └── main.py
│
├── etl_dashboard.pbix
├── .gitignore
└── README.md
```

## ETL Process

### 1. Extract
- Read raw e-commerce sales data from a CSV file.
- Extract the required data for processing.

### 2. Transform
- Process and clean the extracted data using Python.
- Apply the required data transformations.
- Prepare structured data for database storage.

### 3. Load
- Establish a connection to MySQL.
- Load the transformed data into the database.
- Use SQLAlchemy and PyMySQL for database connectivity.

## Power BI Dashboard

The project includes a Power BI dashboard (`etl_dashboard.pbix`) to visualize and explore e-commerce sales data.

## How to Run the Project

1. Clone the repository.
2. Install the required packages:

```bash
pip install sqlalchemy pymysql python-dotenv
```

3. Configure your MySQL database credentials in a local `.env` file.
4. Make sure MySQL is running and the database is configured.
5. Run the ETL pipeline:

```bash
python scripts/main.py
```

6. Open `etl_dashboard.pbix` using Power BI Desktop.

## Key Learning Outcomes

- Understanding ETL pipeline architecture.
- Extracting data from CSV files using Python.
- Processing and transforming data.
- Connecting Python applications to MySQL.
- Loading data into relational databases.
- Creating dashboards using Power BI.

## Conclusion

This project demonstrates an end-to-end ETL workflow integrating Python, MySQL, and Power BI to extract, process, store, and visualize e-commerce sales data.
