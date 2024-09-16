# from lilah_duboff_indiv_proj1.python_files.desc_stats_main import product
"""Takes a csv file, reads it, and creates graphs"""

import pandas as pd
import sys
sys.path.append('python_files')
from desc_stats_main import (
    save_as_markdown
)


test_csv = pd.read_csv("./data/us_driving_fatalities.csv")

def test_save_as_markdown():
    """Tests that the csv can be converted to markdown"""
    result = save_as_markdown()
    assert result is None

if __name__ == "__main__":
    test_save_as_markdown()