print("Starting test...")

from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:12345@localhost/ecommerce_pipeline"
)

try:
    with engine.connect() as conn:
        print("Connected Successfully")
except Exception as e:
    print(e)