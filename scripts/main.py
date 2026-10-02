from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():

    df = extract_data()

    transformed_df = transform_data(df)

    load_data(transformed_df)

    print("ETL Pipeline Completed Successfully")

if __name__ == "__main__":

    run_pipeline()