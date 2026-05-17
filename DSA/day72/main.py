import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")

clean_df = df.dropna()

spread_col = (
    clean_df["Mid-Career 90th Percentile Salary"]
    - clean_df["Mid-Career 10th Percentile Salary"]
)

clean_df.insert(1, "spread", spread_col)

low_risk = clean_df.sort_values("spread")

highest_potential = clean_df.sort_values(['Mid-Career 90th Percentile Salary'],ascending = False)
highest_potential[['Undergraduate Major','Mid-Career 90th Percentile Salary']].head()


