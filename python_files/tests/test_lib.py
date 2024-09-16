"""
Testing the library file functions

"""
import io
import sys

sys.path.append("python_files")

from lib import (
    load_dataset,
    full_describe,
    build_bar_chart,
)

# Shortened mock CSV data as a string (only "year" and "fatal" columns)
mock_csv_data = """
,state,year,fatal
1,al,1982,839
2,al,1983,930
3,al,1984,932
4,al,1985,882
5,al,1986,1081
"""
test_path = io.StringIO(mock_csv_data)


def test_load_dataset():
    """test that loading the CSV will work"""
    result = load_dataset(test_path)
    assert result is not None
    assert result.shape == (5, 4)


def test_full_describe():
    test_path = io.StringIO(mock_csv_data)
    test_df = load_dataset(test_path)

    result = full_describe(test_df)
    assert result is not None


def test_build_bar_chart():
    test_path = io.StringIO(mock_csv_data)
    test_df = load_dataset(test_path)

    result = build_bar_chart(test_df, False)
    assert result is None


if __name__ == "__main__":
    test_load_dataset()
    test_full_describe()
    test_build_bar_chart()
