# Re-importing necessary libraries after the reset
import pandas as pd
import matplotlib.pyplot as plt

# File paths from files
file_path_1 = 'merged_data/2024_12_21_22_07_53_merged_station_data.csv'
file_path_2 = 'merged_data/2024_12_21_22_22_10_merged_station_data.csv'

# Reading the CSV files into DataFrames
df1 = pd.read_csv(file_path_1)
df2 = pd.read_csv(file_path_2)

# Combine the two DataFrames
combined_df = pd.concat([df1, df2], ignore_index=True)

# Convert the 'last_reported' column to datetime format
combined_df['last_reported'] = pd.to_datetime(combined_df['last_reported'], unit='s', errors='coerce')

# Filter necessary columns and sort by station_id and timestamp
time_series_data = combined_df[['last_reported', 'station_id', 'num_bikes_available']].dropna()
time_series_data = time_series_data.sort_values(by=['station_id', 'last_reported'])

# Plotting time series for the first 10 stations for clarity
unique_stations = time_series_data['station_id'].unique()

plt.figure(figsize=(14, 8))
for station_id in unique_stations[:1503]:  # Limit to 10 stations for readability
    station_data = time_series_data[time_series_data['station_id'] == station_id]
    plt.plot(station_data['last_reported'], station_data['num_bikes_available'], label=f"Station {station_id}")

plt.title("Number of Bikes Available Over Time by Station")
plt.xlabel("Timestamp")
plt.ylabel("Number of Bikes Available")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()