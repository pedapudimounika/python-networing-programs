import pandas as pd
data = pd.read_csv("nba1.csv", index_col ="Name")

first = data["Age"]
first = data[["Age","College", "Salary"]]
print(first)