import pandas as pd
def column_average(filename, column):
    data = pd.read_csv(filename)
    if column not in data.columns:
        raise ValueError("Column not found")
    values = pd.to_numeric(data[column], errors="coerce").dropna()
    if values.empty:
        raise ValueError("No numeric values available")
    return round(values.mean(), 2)
