"""Takes a csv file, reads it, and creates graphs"""

from ydata_profiling import ProfileReport
import lib

def save_as_markdown():
    with open ("file name", "a") as file:
        file.write("name")

def main():
    csv = "./data/us_driving_fatalities.csv"
    driving_df = lib.load_dataset(csv)

    if driving_df is not None:
        lib.full_describe(driving_df)
    
        lib.build_bar_chart(driving_df)
        lib.save_plot(driving_df)

    profile = ProfileReport(driving_df)
    profile.to_notebook_iframe()
    profile.to_file("data.html")

if __name__ == "__main__":
    main()


# ProfileReport(final data frame passed as parameter)
