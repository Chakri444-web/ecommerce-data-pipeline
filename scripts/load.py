
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def load_data(df):
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    database = os.getenv("DB_NAME")

    connection_string = (
        f"mysql+pymysql://{user}:{password}@{host}/{database}"
    )

    engine = create_engine(connection_string)

    df.to_sql(
        name="sales_data",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data Loaded into MySQL")
