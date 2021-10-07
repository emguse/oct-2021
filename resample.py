import pandas as pd
from collections import deque
from scipy import interpolate
import numpy as np

FILE_NAME = "sample_sin.csv" #"pressure.csv"

data = pd.read_csv(FILE_NAME).values.tolist()

# Create a deque object and make it a queue
d = deque(data)
# Get 4 seconds of data as a single chunk
start_row = d[0][0]
chunk = []
while start_row+4 >= d[0][0]:
    chunk.append(d.popleft())
print(len(chunk))

# resample
df = pd.DataFrame(chunk)
df = df.set_axis(['time', 'pressure'], axis=1)
df = df.set_index('time')
f = interpolate.interp1d(df.index, df.pressure, kind='cubic')
Hz = 512
re_x = np.arange(df.index.min(), df.index.max(), 1/Hz)
re_y = f(re_x)
re_df = pd.DataFrame(re_y, index=[re_x])

# save csv
re_df = pd.read_csv('reample.csv', index_col=0)