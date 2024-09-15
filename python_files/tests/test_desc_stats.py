from lilah_duboff_indiv_proj1.python_files.desc_stats import product


def test_product():
    assert product(5, 2) == 10
    assert product(-8, -1) == 8
    assert product(0, 1) == 0
    assert product(4, -5) == -20
