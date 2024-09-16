"""
Testing the library file functions

"""

from python_files.lib import (
    load_dataset,
)

test_csv = "./data/us_driving_fatalities.csv"


def test_load_dataset():
    """test that loading the csv will work"""
    test_df = load_dataset(test_csv)
    assert test_df is not None
    assert test_df.shape == (336, 35)


if __name__ == "__main__":
    test_load_dataset()
