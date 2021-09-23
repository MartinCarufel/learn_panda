import pandas as pd
import tkinter.filedialog
import matplotlib.pyplot as plt
# import math

MOUNTH = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

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
    year = input("Pour quel année ?  ")
    essence = ["ULTRAMAR", "SHELL", "PETRO", "ESSO", "PETROCAN"]
    epicerie = ["METRO", "IGA", "SUPER C"]
    pharm = ["JEAN COUTU", "UNIPRIX"]
    allitem = essence + epicerie + pharm
    path = tkinter.filedialog.askopenfilenames()
    df_list = []
    for file in path:
        df_list.append(pd.read_csv(file, encoding="ISO-8859-1", header=None))
    date_list = []
    df = pd.concat(df_list, ignore_index=True)
    df = clean_csv(df)
    date_filter = [year + "/" + x for x in MOUNTH]
    # val = {"epicerie": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    val_list = []
    for date_filter in date_filter:
        date_new_df = df[df.stack().str.contains(date_filter).any(level=0)]
        newdf = date_new_df[date_new_df.stack().str.contains('|'.join(epicerie)).any(level=0)]
        # newdf = df[df.stack().str.contains('|'.join(epicerie)).any(level=0)]
        val_list.append(newdf.sum()["Credit"])
    print(val_list)
    val_list_db = pd.DataFrame({"epicerie": val_list}, index=['Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aou', 'Sep', 'Oct', 'Nov', 'Dec'])
    print(val_list_db)
    val_list_db.plot(kind="bar")
    plt.show()
    # amount = newdf["Credit"]
    # total = round(amount.sum(),2)
    # print(total)
