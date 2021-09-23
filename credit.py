#codinf:utf-8
import pandas as pd
import variable
import tkinter.filedialog
import matplotlib.pyplot as plt
import save_file

# df = pd.read_csv(r".\data\conciliation_20200724.csv", header=None)
# df = df.iloc[:, [0, 3, 4, 5, 11, 12]]
# df = df.rename(columns={0:"Carte", 3:"Date", 4:"id", 5:"Desc", 11:"Credit", 12:"Debit"})
# # print(df)

class date_extract():
    # def __init__(self):
    #     year = None
    #     mount = None
    #     day = None

    def get_year(self, date_string):
        full_date = date_string.split("/")
        return full_date[0]

    def get_mount(self, date_string):
        full_date = date_string.split("/")
        return int(full_date[1])

    def get_day(self, date_string):
        full_date = date_string.split("/")
        return full_date[2]

class depense():
    def __init__(self, dataframe, dep_type):
        self.df = dataframe
        self.dep_type = dep_type

    def dep_type_mount(self, dep_list):
        self.dep_list = dep_list
        date_ex = date_extract()
        val = {"01": [0], "02": [0], "03": [0], "04": [0], "05": [0], "06": [0],
               "07": [0], "08": [0], "09": [0], "10": [0], "11": [0], "12": [0]}

        for ind in self.df.index:
            for x in self.dep_list:
                if x in self.df.loc[ind]["Desc"]:
                    val[date_ex.get_mount(self.df.loc[ind]["Date"])][0] += self.df.loc[ind]["Credit"]

        return val

    def dep_type_mount_v(self, dep_list, year):
        self.dep_list = dep_list
        self.year = year
        date_ex = date_extract()
        val = {self.dep_type: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        val_list = []

        for ind in self.df.index:
            for x in self.dep_list:
                if x in self.df.loc[ind]["Desc"] and date_ex.get_year(self.df.loc[ind]["Date"])==year:
                    val_list.append(str(self.df.loc[ind]["Date"])+"-"+self.df.loc[ind]["Desc"]+": "+str(self.df.loc[ind]["Credit"]))
                    val[self.dep_type][date_ex.get_mount(self.df.loc[ind]["Date"])-1] += self.df.loc[ind]["Credit"]
                    break
                    # val[date_ex.get_mount(self.df.loc[ind]["Date"])][0] += self.df.loc[ind]["Credit"]

        return (val, val_list)



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



if __name__ == "__main__":
    year = input("Pour quel année ?  ")
    path = tkinter.filedialog.askopenfilenames()
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
    date_ex = date_extract()
    for ind in df.index:
        days = date_ex.get_day(df.loc[ind, "Date"])
        # print(type(days))

    essence = ["ULTRAMAR", "SHELL", "PETRO", "ESSO", "PETROCAN"]
    epicerie = ["METRO", "IGA", "SUPER C"]
    pharm = ["JEAN COUTU", "UNIPRIX"]
    resto = save_file.read_file_list("resto.csv")

    dp_ess = depense(df, "Essence")
    dp_epi = depense(df, "Epicerie")
    dp_pharm = depense(df, "Pharmacie")
    dp_resto = depense(df,"resto")

    dp_essence, dp_essence_list = dp_ess.dep_type_mount_v(essence, year)
    dp_epicerie, dp_epicerie_list = dp_epi.dep_type_mount_v(epicerie, year)
    dp_pharmacie, dp_pharmacie_list = dp_pharm.dep_type_mount_v(pharm, year)
    dp_restaurant, dp_restaurant_list = dp_resto.dep_type_mount_v(resto, year)

    dp_ess_df = pd.DataFrame(dp_essence,
                index=['Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aou', 'Sep', 'Oct', 'Nov', 'Dec'])
    dp_epicerie_df = pd.DataFrame(dp_epicerie,
                index=['Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aou', 'Sep', 'Oct', 'Nov', 'Dec'])
    dp_pharmacie_df = pd.DataFrame(dp_pharmacie,
                index=['Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aou', 'Sep', 'Oct', 'Nov', 'Dec'])
    dp_restaurant_df = pd.DataFrame(dp_restaurant,
                index=['Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aou', 'Sep', 'Oct', 'Nov', 'Dec'])
    # saveFile = tkinter.filedialog.asksaveasfilename()
    # df.to_csv(saveFile)
    # df.to_csv(path[0:-4] + "_new.csv",)
    # frame = [dp_ess_df, dp_epicerie_df]
    # result = pd.concat(frame)
    # print(dp_ess_df)
    # print(dp_ess_df)
    result = pd.merge(dp_ess_df, dp_epicerie_df, left_index=True, right_index=True)
    result = pd.merge(result, dp_pharmacie_df, left_index=True, right_index=True)
    result = pd.merge(result, dp_restaurant_df, left_index=True, right_index=True)
    result.to_csv("result_data.csv")
    result.plot(kind="bar")
    for i in range(len(dp_restaurant_list)):
        print(dp_restaurant_list[i])
    # dp_val_df.plot(kind="bar")
    plt.show()

