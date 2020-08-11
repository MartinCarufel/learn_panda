import pandas as pd

sf = pd.Series(pd.date_range("2020-01-01", "2020-02-1", freq="d"))
print(sf)
df = pd.DataFrame(index=sf)
print("aaa")