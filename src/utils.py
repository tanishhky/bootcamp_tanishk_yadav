import pandas as pd

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates descriptive statistics for the numeric columns of a DataFrame.
    [cite: 207]
    Args:
        df: The input DataFrame.

    Returns:
        A DataFrame containing the summary statistics.
    """
    return df.describe()