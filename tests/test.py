from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "secondary_data.csv"


def test_raw_dataset_exists() -> None:
    assert RAW_DATA_PATH.exists()


def test_raw_dataset_schema() -> None:
    df = pd.read_csv(RAW_DATA_PATH, sep=";", nrows=10)

    expected_columns = {
        "class",
        "cap-diameter",
        "cap-shape",
        "cap-color",
        "stem-height",
        "stem-width",
        "habitat",
        "season",
    }

    assert expected_columns.issubset(df.columns)
    assert set(df["class"]).issubset({"e", "p"})
