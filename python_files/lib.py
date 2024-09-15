"""importing pandas package for the describe function"""
"""Takes a csv file, reads it, and creates graphs"""

from ydata_profiling import ProfileReport
import pandas as pd
import matplotlib.pyplot as plt

#create a function that loads in a dataset
def load_dataset(path):
    """Takes a string URL path to a csv file, loads it into the script for analysis, and returns a dataframe"""
    try:
        data = pd.read_csv(path)
        return data
    except FileNotFoundError:
        print(f"File {path} not found")
        return None
    except Exception as error:
        print(f"Error while loading CSV File: {str(error)}")
        return None


def full_describe(driving_df):
    """function that sets a new df variable equal to the summary stats"""
    summary_stats = driving_df.describe()
    stats_markdown = summary_stats.to_markdown()
    return stats_markdown



def build_bar_chart(driving_df):
    """builds a histogram out of the target columns"""
    plt.bar(driving_df["year"], driving_df["fatal"])
    # plt.hist(driving_df["year"], driving_df['fatal'], color="blue", edgecolor="white")
    plt.xlabel("Year")
    plt.ylabel("Number of Fatalities")
    plt.title("Number of Car Crash Fatalities by Year")
    plt.show()


def build_scatterplot():
    """builds a scatterplot out of the target columns"""

def save_plot(file_name, driving_df):
    build_bar_chart(driving_df).savefig(
        "./outputs/" + f"barchart_{file_name}.png"
    )

# ProfileReport(final data frame passed as parameter)