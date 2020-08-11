import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_file = r".\data\cars.csv"

df = pd.read_csv(csv_file)
print(df.dtypes)
# convert_dict = {"Car": str,
#                 "MPG": float,
#                 "Cylinders":int,
#                 "Displacement":float,
#                 "Horsepower":float,
#                 "Weight":float,
#                 "Acceleration":float,
#                 "Model":int,
#                 "Origin":str}
#
# df = df.astype(convert_dict)
# print(df.dtypes)

cyl_8 = df.loc[df["Cylinders"] == 8 , ["Car", "Horsepower"]]
cyl_8 = cyl_8.set_index("Car")
cyl_8 = cyl_8.sort_values(by="Horsepower")
print(cyl_8.head())


muscle_car = df.loc[(df["Cylinders"] == 8) & (df["Horsepower"] >= 150), ["Car", "Horsepower", "Cylinders"]]
muscle_car = muscle_car.set_index("Car").sort_values(by="Horsepower")
muscle_car.to_csv(r".\data\muscle_car.csv")
# muscle_car = df.loc[df["Horsepower"] >= 150.0, ["Car", "Horsepower"]]
print(muscle_car)
# print(df.columns)
select_col = ["Car", "Cylinders", "Horsepower", ]
all_8_cylinder = df.loc[df["Cylinders"] == 8, select_col]
all_8_cylinder = all_8_cylinder.set_index("Car")
print(all_8_cylinder)