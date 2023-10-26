path=r'D:\data structures Notes\python_pro\venv\supermarket_sales - Sheet1.csv'
import pandas as pd

def load_Data(path):
    df= pd.read_csv(path)
    return df

