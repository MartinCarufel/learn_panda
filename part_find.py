import pandas as pd
s = "Mon auto est rouge"
to_f = "Mon"
f_dic = {"auto":"a", "bike":"b", "pelle":"c"}
res = s.find(to_f)


for key, value in f_dic.items():
    if key in s:
        print(value)


print(res)

df = pd.DataFrame({"A":["001", "002", "003"], "desc":["Mon auto est rouge", "Mon bike est rouge", "Ma pelle est bleu"]})


for ind in df.index:
    if df.loc[ind, "desc"].find("bike") != -1:
        print(df.loc[ind, "desc"])