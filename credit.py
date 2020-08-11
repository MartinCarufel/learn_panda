import pandas as pd


# df = pd.read_csv(r".\data\conciliation_20200724.csv", header=None)
# df = df.iloc[:, [0, 3, 4, 5, 11, 12]]
# df = df.rename(columns={0:"Carte", 3:"Date", 4:"id", 5:"Desc", 11:"Credit", 12:"Debit"})
# # print(df)

achat_martin = {}


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

def sort_trasaction(dataframe):
    df = dataframe
    for ind in df.index:
        if df.loc[ind, "Carte"] == "MASTERCARD 5598280224899018":

            df.loc[ind, "att"] = "m"
        else:
            df.loc[ind, "att"] = "c"
    return df

    pass


if __name__ == "__main__":
    df = pd.read_csv(r".\data\conciliation_20200724.csv", header=None)

    # print(df)
    df = clean_csv(df)
    df = sort_trasaction(df)
    print(df)

