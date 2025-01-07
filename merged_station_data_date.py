import requests
import pandas as pd
import json
import datetime

now = datetime.datetime.now()
date = now.strftime("%Y_%m_%d_%H_%M_%S")

def fetch_json(url):
    """Fetch JSON data from a URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    # URLs for station information and status
    station_info_url = "https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_information.json"
    station_status_url = "https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_status.json"

    # Fetch JSON data
    station_info_data = fetch_json(station_info_url)
    station_status_data = fetch_json(station_status_url)

    # Convert JSON data to DataFrames
    station_info_df = pd.DataFrame(station_info_data['data']['stations'])
    station_status_df = pd.DataFrame(station_status_data['data']['stations'])

    # Merge DataFrames on station_id
    merged_df = pd.merge(station_info_df, station_status_df, on='station_id', how='inner')

    # Add DataFrames on date
    merged_df['date'] = date

    # Save the merged DataFrame to a CSV file
    output_file = date + "_merged_station_data.csv"
    merged_df.to_csv("merged_data/" + output_file, index=False, encoding='utf-8-sig')

    print(f"Merged data has been saved to {output_file}")

if __name__ == "__main__":
    main()
