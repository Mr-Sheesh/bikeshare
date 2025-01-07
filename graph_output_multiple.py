import os
import pandas as pd
import matplotlib.pyplot as plt

def process_and_plot(files):
    combined_df = pd.DataFrame()

    #ファイルの読み取り
    for file in files:
        df = pd.read_csv(file)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    # 時間情報の処理
    combined_df['last_reported'] = pd.to_datetime(combined_df['last_reported'], unit='s', errors='coerce')

    # 列のフィルタとソート
    time_series_data = combined_df[['last_reported', 'station_id', 'num_bikes_available']].dropna()
    time_series_data = time_series_data.sort_values(by=['station_id', 'last_reported'])

    # プロット
    unique_stations = time_series_data['station_id'].unique()
    plt.figure(figsize=(18, 12))
    for station_id in unique_stations:
        station_data = time_series_data[time_series_data['station_id'] == station_id]
        plt.plot(station_data['last_reported'], station_data['num_bikes_available'], label=f"Station {station_id}")

    plt.title("Number of Bikes Available Over Time by Station (All Stations)")
    plt.xlabel("Timestamp")
    plt.ylabel("Number of Bikes Available")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='xx-small', ncol=2)
    plt.grid(True)
    plt.tight_layout()

    # ファイルに保存
    output_plot = "station_data_plot.png"
    plt.savefig(output_plot)
    plt.show()

    print(f"Plot saved as {output_plot}")

if __name__ == "__main__":

    # ワーキングディレクトリを確認
    print(f"Current working directory: {os.getcwd()}")

    # CSVファイルを格納するディレクトリを指定
    directory = "./bikeshare/merged_data"

    # ディレクトリ内のCSVファイル情報を取得
    csv_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.csv')]

    if not csv_files:
        print("No CSV files found in the specified directory.")
    else:
        process_and_plot(csv_files)
