"""
Testing the library file functions

"""
import sys
sys.path.append('python_files')

from lib import (
    load_dataset,
    full_describe,
    build_bar_chart,
    save_plot
)

test_path = "./data/us_driving_fatalities.csv"
test_df = load_dataset(test_path)

def test_load_dataset():
    """test that loading the csv will work"""
    result = load_dataset(test_path)
    assert result is not None
    assert result.shape == (336, 35)

def test_full_describe():
    result  = full_describe(test_df)
    assert result is not None


def test_build_bar_chart():
    result = build_bar_chart(test_df)
    # assert result is None

def test_save_plot():
    result = save_plot(test_df)
    # assert result is None


if __name__ == "__main__":
    test_load_dataset()
    test_full_describe()
    test_build_bar_chart()
    test_save_plot()
