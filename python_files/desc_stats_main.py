"""Takes a csv file, reads it, and creates graphs"""

from ydata_profiling import ProfileReport
import lib


def save_as_markdown():
    """Takes the output and writes it to an html file"""
    with open("file name", "a") as file:
        file.write("name")


def main():
    """Loads a dataset
    generates summary stats and visualizations"""
    csv = "./data/us_driving_fatalities.csv"
    driving_df = lib.load_dataset(csv)

    if driving_df is not None:
        print(lib.full_describe(driving_df))
        lib.build_bar_chart(driving_df, False)


if __name__ == "__main__":
    main()
