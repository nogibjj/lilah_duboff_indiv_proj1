import pandas as pd
import matplotlib.pyplot as plt

"""Takes a csv file, reads it, and creates graphs"""


# create a function that loads in a dataset
def load_dataset(path):
    """Takes a string URL path to a csv file,
    loads it into the script for analysis,
    returns a dataframe"""
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
    return summary_stats


def build_bar_chart(driving_df, is_jupyter):
    """builds a histogram out of the target columns"""

    plt.bar(driving_df["year"], driving_df["fatal"])
    plt.xlabel("Year")
    plt.ylabel("Number of Fatalities")
    plt.title("Number of Car Crash Fatalities by Year")
    plt.show()
    if is_jupyter == True:
        plt.savefig("./driving_fatalities.png")
    elif is_jupyter == False:
        plt.savefig("./outputs/output.png")     
        
        


def build_scatterplot():
    """builds a scatterplot out of the target columns"""
    # can be used to build scatterplots



