import pandas as pd

# squirrel_count
# Fur Color, Count

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color_count = squirrel_data["Primary Fur Color"].value_counts()

# Convert series to dataframe
fur_color_count_df = fur_color_count.reset_index()

# Renaming columns
fur_color_count_df.columns = ["Fur Color", "Counts"]

# Saving as a csv file
fur_color_count_df.to_csv("squirrel_count.csv")
