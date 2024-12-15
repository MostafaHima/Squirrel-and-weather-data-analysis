import pandas as pd  # Importing Pandas library for data manipulation

# Read the squirrel census data from a CSV file
squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240827.csv")

# Count the number of squirrels for each primary fur color
fur_color_counts = squirrel_data['Primary Fur Color'].value_counts()

# Calculate the count of squirrels with specific fur colors manually
black_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Black"])  # Count black squirrels
gray_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Gray"])    # Count gray squirrels
cinnamon_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Cinnamon"])  # Count cinnamon squirrels

# Create a dictionary to summarize fur colors and their counts
squirrel_fur_summary = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],  # Fur colors
    "Count": [str(black_count), str(gray_count), str(cinnamon_count)]  # Corresponding counts
}

# Convert the dictionary into a Pandas DataFrame
squirrel_fur_df = pd.DataFrame(squirrel_fur_summary)

# Write the summary data to a new CSV file
with open("squirrel_fur_summary.csv", mode='w') as summary_file:
    summary_file.write(str(squirrel_fur_df))

# Read the newly created CSV file to ensure the data is written correctly
summary_data = pd.read_csv("squirrel_fur_summary.csv")
print(summary_data)  # Print the content of the summary data
