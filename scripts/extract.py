import pandas as pd

def extract_data():

    df = pd.read_csv(
        "data/raw/ecommerce_sales_data.csv"
    )

    print("Dataset Loaded Successfully")
    print(df.head())

    return df

if __name__ == "__main__":

    df = extract_data()