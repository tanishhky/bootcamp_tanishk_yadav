import pandas as pd

def detect_outliers_iqr(series: pd.Series) -> pd.Series:
    """Detects outliers using the Interquartile Range (IQR) method.""" [cite: 378]
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return (series < lower_bound) | (series > upper_bound)

def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """Detects outliers using the Z-score method.""" [cite: 379]
    mean = series.mean()
    std = series.std()
    z_scores = (series - mean) / std
    return abs(z_scores) > threshold