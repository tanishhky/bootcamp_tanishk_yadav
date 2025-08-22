import pandas as pd
from sklearn.preprocessing import StandardScaler

def fill_missing_median(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Fills missing values in a column with the column's median.""" [cite: 156]
    median_val = df[column].median()
    df[column] = df[column].fillna(median_val)
    return df

def drop_missing(df: pd.DataFrame, subset_cols: list) -> pd.DataFrame:
    """Drops rows with missing values in specified columns.""" [cite: 157]
    return df.dropna(subset=subset_cols)

def normalize_data(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Normalizes a numeric column using StandardScaler.""" [cite: 158]
    scaler = StandardScaler()
    df[f"{column}_normalized"] = scaler.fit_transform(df[[column]])
    return df