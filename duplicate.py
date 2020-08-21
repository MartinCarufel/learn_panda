#codinf:utf-8
import pandas as pd
import variable
import tkinter.filedialog
import matplotlib.pyplot as plt

not_a_resto = ["AGOO", "BELL", "JEAN COUTU", "IGA", "LE LUNCH",  "METRO", "NETFLIX", "RONA", "CDN TIRE", "ULTRAMAR" ,"VIRGIN"]
resto = ["AU COQ", "DOMINOS", "EGGSQUIS", "HARVEYS", "MCDONALD", "SUBWAY", "JUMBO"]

def clean_csv(dataframe):
    df = dataframe

    df = df.iloc[:, [0, 3, 4, 5, 11, 12]]
    df = df.rename(columns={0: "Carte", 3: "Date", 4: "id", 5: "Desc", 11: "Credit", 12: "Debit"})
    for ind in df.index:
        # print(df["Debit"][ind])
        # print(ind)
        if pd.notnull(df["Debit"][ind]):
            df.loc[ind, "Credit"] = df.loc[ind, "Debit"] * -1

    df = df.loc[:, ["Carte", "Date", "id", "Desc", "Credit"]]
    return df

if __name__ == "__main__":
    path = tkinter.filedialog.askopenfilenames()
    print(path)
    # df = pd.read_csv(r".\data\conciliation_20200724.csv", header=None)
    # df = pd.read_csv("D:/Users/Martin/Google_Drive/conciliation_20200724.csv", encoding = "ISO-8859-1", header=None)
    df_list = []
    for file in path:
        df_list.append(pd.read_csv(file, encoding="ISO-8859-1", header=None))

    df = pd.concat(df_list, ignore_index=True)
    df = clean_csv(df)
    # print(df)
    df_no_duplicate = df.drop_duplicates(subset="Desc")
    df_no_duplicate.to_csv("no_duplicate.csv")


    for ind in df_no_duplicate.index:
        for value in not_a_resto:
            if value in df_no_duplicate.loc[ind, "Desc"]:
                print("not a resto")


