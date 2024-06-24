import pandas as pd

def main():
  df = pd.read_csv("Large_Data_Sets/NewLaunchData/Search_keywords.csv")
  df["Avg. CPC"] = df["Avg. CPC"].str.replace("$", "").astype(float)
  df = df.sort_values(by=["Clicks"], ascending=False)
  print(df)
  styled_df = df.style.map(colorAvgCPC)
  styled_df.to_html("styled_dataframe.html")


def colorAvgCPC(x):
  if type(x) == str:
    return
  if type(x) == int:
    return
  r = 0
  if x < 1:
    r = 0
  elif x > 5:
    r = 255
  else:
    r = int((x - 1) * (255 - 0) / (5 - 1) + 0)
  g = 0
  if x < 0:
    g = 255
  elif x > 5:
    g = 0
  else:
    g = 255 - int((x - 0) * (255 - 0) / (5 - 0) + 0)
  print(f'background-color: rgb({r}, {g}, 0)')
  return f'background-color: rgb({r}, {g}, 0)'


if __name__ == "__main__":
  main()