"""importing pandas package for the describe function"""
"""Takes a csv file, reads it, and creates graphs"""

from ydata_profiling import ProfileReport
import pandas as pd
import matplotlib.pyplot as plt

#create a function that loads in a dataset
def load_dataset(path):
    """Takes a string URL path to a csv file, loads it into the script for analysis, and returns a dataframe"""
    try:
        data = pd.read_cvs(path)
        return data
    except FileNotFoundError:
        print(f"File {path} not found")
        return None
    # except Exception as error:
    #     print(f"Error while loading CSV File: {str(error)}")
    #     return None


def full_describe(driving_df):
    """function that sets a new df variable equal to the summary stats"""
    return driving_df.describe()


def summary_statistics(dataframe):
    """Takes the DataFrame and calls the describe function on it
    Args:
        DataFrame
    Returns:
        DataFrame containing summary statistics"""
    summary = dataframe.describe()
    markdown_output = summary.to_markdown()
    return markdown_output










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



# import sys

# def plot_visualize(dataframe):
#     auto_df = dataframe
#     """A test of data visualization for a given data set"""
#     weight = auto_df["weight"]
#     mpg = auto_df["mpg"]

#     fig, ax = plt.subplots()
#     ax.scatter(weight, mpg)
#     ax.set_xlabel("Vehicle Weight")
#     ax.set_ylabel("MPG")
#     ax.set_title("Scatter Plot of Vehicle Weight vs MPG by car origin")
#     return fig


# def save_plot(file_name, datafram):
#     plot_visualize(datafram).savefig(
#         "pythonproject/figures/" + f"scatter_plot_{file_name}.png"
#     )



# def df_min(dataframe, column_name):
#     """Takes a dataframe and returns the minimum value of the dataframe
#     Args:
#         dataframe
#     Returns:
#         minimum value of the dataframe"""
#     min = dataframe[column_name].min()
#     return min


# def df_max(dataframe, column_name):
#     """Takes a dataframe and returns the maximum value of the dataframe
#     Args:
#         dataframe
#     Returns:
#         maximum value of the dataframe"""
#     max = dataframe[column_name].max()
#     return max