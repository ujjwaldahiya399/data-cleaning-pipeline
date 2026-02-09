import pandas as pd
import numpy as np

def clean_dataframe(df: pd.DataFrame):
    """
    cleans a panda dataframe by removing unwanted index columns,
    standardizing column names,handling missing values and removing duplicate rows.
    """
    df = df.copy()
    # Drop unwanted index-like columns
    df = drop_unnamed_columns(df) # CSVs saved with index often create Unnamed: 0
    # Standardize column names
    df = standardize_columns(df)
    # remove duplicate rows
    df = df.drop_duplicates()
    ## handle missing values
    df = handle_missing_values(df)
    return df

def drop_unnamed_columns(df: pd.DataFrame):
    """
    Drop columns created from CSV index
    :param df:
    :return:
    """
    columns_to_drop = [
        col for col in df.columns
        if col.lower().startswith("unnamed")
    ]
    return df.drop(columns=columns_to_drop,errors="ignore")

def standardize_columns(df: pd.DataFrame):
    """
    Make column names consistent
    :param df:
    :return:
    """
    df.columns = (
        df.columns.str.strip().str.lower().str.replace(" ", "_")
    )
    return df

def handle_missing_values(df: pd.DataFrame):
    """
    Filling missing values by replacing them with median for numberic cplumns, mode or 'unknown' for non-numberic columns.

    :param df:
    :return:
    """
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            median_value = df[col].median()
            df[col] = df[col].fillna(median_value)
        else:
            mode_series = df[col].mode(dropna=True)
            fill_value = mode_series[0] if not mode_series.empty else "Unknown"
            df[col] = df[col].fillna(fill_value)
    return df

