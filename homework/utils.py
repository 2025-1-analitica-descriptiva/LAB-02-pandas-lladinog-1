import pandas as pd

def get_dataframe(file_path):
    """
    Returns a pandas DataFrame from a TSV file
    """
    return pd.read_csv(file_path, sep='\t')

def get_column_value_counts(file_path, column_name):
    """
    Returns the value counts of a specified column in a TSV file in alphabetical order.
    """
    df = get_dataframe(file_path)
    return df[column_name].value_counts().sort_index()

def get_column_values_by_group(file_path, group_column, target_column):
    """
    Returns the values of a target column grouped by a specified column in a TSV file.
    """
    df = get_dataframe(file_path)
    return df.groupby(group_column)[target_column]

def get_unique_sorted_column_values(file_path, column_name):
    """
    Returns a list of unique values from a specified column in a TSV file, sorted alphabetically.
    """
    df = get_dataframe(file_path)
    return sorted(df[column_name].str.upper().unique().tolist())
