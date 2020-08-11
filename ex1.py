import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# csv_file = r"D:\Users\Martin\Documents\git_checkout\learn_panda\data\Average and median gender pay ratio in annual wages, salaries and commissions.csv"
csv_file = r".\data\Average and median gender pay ratio in annual wages, salaries and commissions.csv"
out_csv = r".\data\out.csv"
df = pd.read_csv(csv_file)
col = ["REF_DATE", "GEO", "National Occupational Classification (NOC)", "Statistics", "VALUE"]
statistic = ["Average wages, salaries and commissions, males"]
# df = df[df["GEO"].isin(["Quebec"])]
# df = df[df["REF_DATE"] >= 2015]
df2 = df[(df["GEO"].isin(["Quebec"])) & (df["Statistics"].isin(statistic))]
# print(df2.head())
df2 = df[col]
df2.to_csv(out_csv, sep=',')
# print(df2)
# df = df([df["REF_DATE"] >= 2015]) & ([df["GEO"].isin(["Quebec"])])
all_occ = df[df["National Occupational Classification (NOC)"] == "All occupations"]
all_occ.to_csv(r".\data\all_occ.csv")
males_all_occ = df[(df["GEO"] == "Quebec") &
                   (df["Statistics"] == "Average wages, salaries and commissions, males") &
                   (df["National Occupational Classification (NOC)"] == "All occupations")]
males_all_occ_ser = males_all_occ["VALUE"].to_list()
# print("DATAFRAME", df)
females_all_occ = df[(df["GEO"] == "Quebec") &
                   (df["Statistics"] == "Average wages, salaries and commissions, females") &
                   (df["National Occupational Classification (NOC)"] == "All occupations")]
females_all_occ_ser = females_all_occ["VALUE"].to_list()
print("FEMALES", females_all_occ)

years = males_all_occ["REF_DATE"].to_list()
collect_data = pd.DataFrame({"year": years, "males average":males_all_occ_ser, "females average":females_all_occ_ser})
collect_data = collect_data.set_index(["year"])
print(collect_data)
collect_data.plot(kind="bar")
collect_data.plot()
plt.show()