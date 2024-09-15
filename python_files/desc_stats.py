"""Takes a csv file, reads it, and creates graphs"""

# from ydata_profiling import ProfileReport
import pandas as pd
import matplotlib.pyplot as plt

csv = "./data/us_driving_fatalities.csv"

driving_df = pd.read_csv(csv)
print(driving_df)


def full_describe():
    """function that sets a new df variable equal to the summary stats"""
    driving_stats = driving_df.describe()
    print(driving_stats.to_markdown())
    



full_describe()


def build_chart():
    """builds a histogram out of the target columns"""
    plt.bar(driving_df["year"], driving_df["fatal"])
    # plt.hist(driving_df["year"], driving_df['fatal'], color="blue", edgecolor="white")
    plt.xlabel("Year")
    plt.ylabel("Number of Fatalities")
    plt.title("Number of Fatalities by Year")
    plt.savefig("outputs/output.png")
    plt.show()


build_chart()


# ProfileReport(final data frame passed as parameter)
