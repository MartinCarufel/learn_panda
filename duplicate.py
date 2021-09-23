#codinf:utf-8
import pandas as pd
import variable
import tkinter.filedialog
import matplotlib.pyplot as plt
import save_file

not_a_resto = ["AGOO", "BELL", "JEAN COUTU", "IGA", "LE LUNCH",  "METRO", "NETFLIX", "RONA", "CDN TIRE", "ULTRAMAR" ,"VIRGIN"]
# not_a_resto = ["AGOO"]
# resto = ["AU COQ", "DOMINOS", "EGGSQUIS", "HARVEYS", "MCDONALD", "SUBWAY", "JUMBO"]

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
    # df_no_duplicate.to_csv("no_duplicate.csv")


    for ind in df_no_duplicate.index:
        resto = save_file.read_file_list("resto.csv")
        not_resto = save_file.read_file_list("not_resto.csv")
        if len(resto[0]) > 1 and len(not_resto[0]) > 1:
            identified = not_a_resto + resto + not_resto
        elif len(resto[0]) > 1 and len(not_resto[0]) < 1:
            identified = not_a_resto + resto
        elif len(resto[0]) < 1 and len(not_resto[0]) > 1:
            identified = not_a_resto + not_resto
        else:
            identified = not_a_resto

        # print(df_no_duplicate.loc[ind, "Desc"])
        # print(identified)
        # input("press enter")
        res = any(ident in df_no_duplicate.loc[ind, "Desc"] for ident in identified)

        # using list comprehension
        # checking if string contains list element
        # res = [ele for ele in identified if (ele not in df_no_duplicate.loc[ind, "Desc"])]
        # res = any(ele in df_no_duplicate.loc[ind, "Desc"] for ele in identified)
        if not res:
            print(df_no_duplicate.loc[ind, "Desc"])
            rep = input("Es-ce un restaurant ? (o/n)")
            if rep.upper() == "O":
                save_file.add_resto_keyword()
            else:
                save_file.add_not_resto_keyword()



