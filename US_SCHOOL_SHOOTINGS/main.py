
import csv 
import pandas as pd
import plotly.express as ple

class CleanData():
    def __init__(self, filepath: str) -> None:
        if len(filepath) == 0:
            return print("file path is empty")
            
        self.filepath = filepath
        try:
            self.data = pd.read_csv(filepath)
        except:
            print("Error reading the csv to a dataframe")

    def get_summary_stats(self):
        print("___________________________COLUMS_________")
        for col in self.data.columns:
            print(col)
        print("___________________________DESCRIPTION_________")
        print(self.data.describe())
        print("___________________________FIRST 5 Entries_________")
        print(self.data.head(5))

    def EDA(self):
        # a map showing the occurence of shooting in each state
        state_counts = self.data["state"].value_counts().reset_index()
        state_counts.columns = ["state", "count"]

        fig = ple.choropleth(
            state_counts,
            locations="state",
            locationmode="USA-states",
            color="count",
            color_continuous_scale="Blues",  # darker = higher
            scope="usa",
            labels={"count": "Shooting Occurences"},
            title="School Shooting Occurences by State"
        )

        fig.show()




if __name__=="__main__":
    cleaner = CleanData("US_SCHOOL_SHOOTINGS/school-shootings-data.csv")
    cleaner.get_summary_stats()
    cleaner.EDA()
    
