import pandas as pd

# Creating a detailed dataset for days of the week, temperature, and weather conditions
weather_data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] * 4,  # Repeated week days
    "Temperature": [25, 22, 28, 30, 27, 26, 24, 23, 29, 21, 25, 31, 28, 22, 20, 26, 24, 27, 30, 29, 21, 23, 28, 24, 22,
                    30, 26, 25],  # Temperatures for each day
    "Condition": ["Sunny", "Cloudy", "Rainy", "Sunny", "Partly Cloudy", "Rainy", "Sunny", "Cloudy", "Rainy", "Sunny",
                  "Partly Cloudy", "Rainy",
                  "Sunny", "Cloudy", "Rainy", "Sunny", "Partly Cloudy", "Rainy", "Sunny", "Cloudy", "Rainy", "Sunny",
                  "Partly Cloudy", "Rainy",
                  "Sunny", "Cloudy", "Rainy", "Sunny"]  # Weather conditions for each day
}

# Creating a DataFrame to represent the weather dataset
weather_df = pd.DataFrame(weather_data)

# Saving the DataFrame to a CSV file for further analysis or sharing
csv_file_path = "./weekly_weather.csv"  # Path where the CSV will be saved
weather_df.to_csv(csv_file_path, index=False)  # Save without including the DataFrame index

# Outputting the CSV file path for reference
print(csv_file_path)
