import numpy as np
import pandas as pd

arr = np.random.rand(3)
print("Numpy array:")
print(arr)

# Conversion of array to series
series = pd.Series(arr)
print("\nSeries:")
print(series)

# Conversion of series to dataframe
df = pd.DataFrame(series, columns=['A'])
print("\nSeries to DataFrame:")
print(df)
