#codinf:utf-8
import pandas as pd
import variable
import tkinter.filedialog

# df = pd.read_csv(r".\data\conciliation_20200724.csv", header=None)
# df = df.iloc[:, [0, 3, 4, 5, 11, 12]]
# df = df.rename(columns={0:"Carte", 3:"Date", 4:"id", 5:"Desc", 11:"Credit", 12:"Debit"})
# # print(df)

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

def find_transaction(input, search_dict):
    input = input
    sd = search_dict
    for key, value in sd.items():
        if key in input:
            return value

    return "Not found"

def sort_trasaction(dataframe):
    df = dataframe
    for ind in df.index:
        if df.loc[ind, "Carte"] in ["MASTERCARD 5598280224899018", "VISA 4540330755072014"]:
            df.loc[ind, "att"] = find_transaction(df.loc[ind, "Desc"], variable.achat_martin)
        elif df.loc[ind, "Carte"] in ["MASTERCARD 5598280224899026", "VISA 4540330755072022"]:
            df.loc[ind, "att"] = find_transaction(df.loc[ind, "Desc"], variable.achat_anne_marie)
    return df

    pass


if __name__ == "__main__":
    path = tkinter.filedialog.askopenfilenames()
    print(path)
    # df = pd.read_csv(r".\data\conciliation_20200724.csv", header=None)
    # df = pd.read_csv("D:/Users/Martin/Google_Drive/conciliation_20200724.csv", encoding = "ISO-8859-1", header=None)
    df_list = []
    for file in path:
        df_list.append(pd.read_csv(file, encoding="ISO-8859-1", header=None))

    df = pd.concat(df_list, ignore_index=True)
    # print(df)
    df = clean_csv(df)
    df = sort_trasaction(df)

    print(df)
    saveFile = tkinter.filedialog.asksaveasfilename()
    df.to_csv(saveFile)
    # df.to_csv(path[0:-4] + "_new.csv",)

