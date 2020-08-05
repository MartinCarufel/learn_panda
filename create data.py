import pandas as pd # This is always assumed but is included here as an introduction.
import numpy as np
import matplotlib.pyplot as plt
import random


date = pd.date_range('20200701', '20200715')
df = pd.DataFrame(np.random.randint(1, 10, 15), index=date)
print(df.head())

df = df.rename(columns={0:"One"})
print(df.head())