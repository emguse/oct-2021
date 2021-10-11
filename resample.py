import pandas as pd
from collections import deque
from scipy import interpolate
import numpy as np

Hz = 256 # resampling rate
CHUNK_SIZE = 4 # chunk size [sec]
FILE_NAME = "./press_log/20211009-163236.csv" #"pressure.csv"

data = pd.read_csv(FILE_NAME).values.tolist()

# Create a deque object and make it a queue
d = deque(data)

# Find the number of chunks
start_time = d[0][0]
last_time = d[len(d)-1][0]
total_time = last_time - start_time
chunk_count = divmod(total_time, CHUNK_SIZE)
print("total_time: "+ str(total_time))
if chunk_count[1] == 0:
    chunk_count = chunk_count[0]
else:
    chunk_count = int(chunk_count[0]) + 1
print("chunk_count: "+ str(chunk_count))
# 1234567890
# 1234 -> 123 
# #For the first chunk, use the first 3/4.
# 3456 -> 45 -> 12345 
# For the second and subsequent chunks, 
# use the starting position 3/4 of the way down, 
# discard the first 1/4 and the last 1/4, and use the middle 2/4.
# ...
# 7890 -> 890 -> 1234567890
# For the last chunk, use the last 3/4.


# Get same seconds of data as a single chunk
start_row = d[0][0]
chunk = []
while start_row+CHUNK_SIZE >= d[0][0]:
    chunk.append(d.popleft())
print(len(chunk))

# resample
df = pd.DataFrame(chunk)
df = df.set_axis(['time', 'pressure'], axis=1)
df = df.set_index('time')
f = interpolate.interp1d(df.index, df.pressure, kind='cubic')
re_x = np.arange(df.index.min(), df.index.max(), 1/Hz)
re_y = f(re_x)
re_df = pd.DataFrame(re_y, index=[re_x])

# save csv
re_df.to_csv('reample.csv')