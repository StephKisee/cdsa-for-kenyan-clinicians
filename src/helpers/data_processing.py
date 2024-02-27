"""
This module contains all the functions to process the data
"""

import pandas as pd

def load_data():
    pass


def split_cells(df: pd.DataFrame,
                column: str,
                uv: list = None,
                sep: str = "&") -> pd.DataFrame:
    """
    Split the cells of a column into multiple rows
    """
    if uv is None:
        df.rename(columns={column: "col"}, inplace=True)
        df = df.assign(col=df["col"].str.split(sep)).explode("col").reset_index(drop=True)
        df.rename(columns={"col": column}, inplace=True)
    else:
        if not isinstance(uv, list):
            uv = list(uv)
        for i in uv:
            df[column] = df[column].str.replace(i, i + sep)
        df[column] = df[column].str.replace(sep + r"\s+", sep, regex=True)
        df[column] = df[column].str.replace(sep + r"$", "", regex=True)

        df.rename(columns={column: "col"}, inplace=True)
        df = df.assign(col=df["col"].str.split(sep)).explode("col").reset_index(drop=True)
        df.rename(columns={"col": column}, inplace=True)

        df[column] = df[column].str.strip()

    return df


def clean_data():
    pass


def transform_data():
    pass


def save_data():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
