# create a simple category based on crime levels and compare unemployment rates between the groups

# import pandas library
import pandas as pd

# load crime.csv dataset into a dataframe
crime_dataset_to_dataframe = pd.read_csv("crime.csv")

# using a function, create a new column called risk based on ViolentCrimesPerPop
def risk_level_of_crimes(crime_rate):
    # for crime rate >= 0.50
    if crime_rate >= 0.50:
        return "HighCrime"
    else:
        return "LowCrime"

# run risk_level function on every value in the column ViolentCrimesPerPop
# store the results in a new column "risk"
crime_dataset_to_dataframe["risk"] = crime_dataset_to_dataframe["ViolentCrimesPerPop"].apply(risk_level_of_crimes)

# group data by risk (high low)
grouping_data_by_risk = crime_dataset_to_dataframe.groupby("risk")

# calculate the average value of PctUnemployed
average_value_of_PctUnemployed = (
    grouping_data_by_risk["PctUnemployed"].sum()/grouping_data_by_risk["PctUnemployed"].count()
)

# print the average unemployment rate for HighCrime and LowCrime
print("The average unemployment rate: ")
print("HighCrime:", average_value_of_PctUnemployed["HighCrime"])
print("LowCrime:", average_value_of_PctUnemployed["LowCrime"])
