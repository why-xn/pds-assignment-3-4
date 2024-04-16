import pandas as pd

def cleanup():
    df = pd.read_csv('../data_raw/diabetes.csv')
    df_clean = df.dropna()
    df_clean.to_csv('../data_clean/diabetes.csv', index=False)


cleanup()
