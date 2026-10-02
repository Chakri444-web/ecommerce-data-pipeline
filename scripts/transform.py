def transform_data(df):

    # remove duplicate rows
    df.drop_duplicates(inplace=True)

    # remove rows with missing values
    df.dropna(inplace=True)

    # standardize column names
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
    )

    print("Data Cleaned Successfully")

    print(df.head())

    return df