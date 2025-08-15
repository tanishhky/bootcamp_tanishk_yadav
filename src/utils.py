import pandas as pd

def get_summary_stats(df):
    """
    Calculates and returns descriptive summary statistics for a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing the summary statistics.
    """
    return df.describe()

def save_summary(df, file_path):
    """
    Saves a DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        file_path (str): The path to save the file to.
    """
    # Create the directory if it doesn't exist
    import os
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path)
    print(f"Summary saved to {file_path}")