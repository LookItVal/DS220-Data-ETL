import pandas as pd
import os

def main():
  normalizeFileNames()
  df = combinedTimeSeries()
  df.to_csv("Data_Exports/Combined_Time_Series.csv", index=False)


def normalizeFileNames():
  for dir in os.listdir("Raw_Data"):
    for file in os.listdir(f"Raw_Data/{dir}"):
      if file == ".DS_Store":
        continue
      os.rename(f"Raw_Data/{dir}/{file}", f"Raw_Data/{dir}/{file.split('(')[0]}.csv")


def combinedTimeSeries():
  df = pd.DataFrame()
  for dir in os.listdir("Raw_Data"):
    data = pd.read_csv(f"Raw_Data/{dir}/Time_series.csv")
    df = pd.concat([df, data])
  return df


if __name__ == "__main__":
  main()

