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

# Find number of chunks
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

for i in range(chunk_count):
    if i == chunk_count-1: # Zero-filling of the last chunk
        last_chunk_head = d[0][0]
        while last_chunk_head + CHUNK_SIZE >= d[len(d)-1][0]:
            last_time = d[len(d)-1][0]
            fill_zero = [last_time+1, 0]
            d.append(fill_zero)
    # Get seconds of data as a single chunk
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
    re_x = np.arange(df.index.min(), df.index.max(), 1/Hz) # 後で直す
    re_y = f(re_x)

    #re_df = pd.DataFrame(re_y, re_x)
    #print(re_df)
    #re_xy = re_df.to_numpy()
    #print(re_xy)

    store_df = pd.DataFrame()

    if i == 0:    # Store the first chunk
        #first_x = np.delete(re_x, slice(int(Hz*CHUNK_SIZE*3/4), None), None)
        #first_y = np.delete(re_y, slice(int(Hz*CHUNK_SIZE*3/4), None), None)
        #first_df = pd.DataFrame(first_x, first_y)
        first_df = pd.DataFrame(re_x, re_y)
        store_df = pd.concat([store_df, first_df], axis=0)
    elif i == chunk_count-1:  # Store the last chunk
        #last_x = np.delete(re_x, slice(None, int(Hz*CHUNK_SIZE*1/4)), None)
        #last_y = np.delete(re_y, slice(None, int(Hz*CHUNK_SIZE*1/4)), None)
        #last_df = pd.DataFrame(last_x, last_y)
        #print(last_df)
        last_df = pd.DataFrame(re_x, re_y)
        store_df = pd.concat([store_df, last_df], axis=0)
    else:   # intermediate lump
        #intermediate_X = np.delete(re_x, slice(None, int(Hz*CHUNK_SIZE*1/4)), None)
        #intermediate_X = np.delete(intermediate_X, slice(int(Hz*CHUNK_SIZE*3/4), None), None)
        #intermediate_y = np.delete(re_y, slice(None, int(Hz*CHUNK_SIZE*1/4)), None)
        #intermediate_y = np.delete(intermediate_y, slice(int(Hz*CHUNK_SIZE*3/4), None), None)
        #intermediate_df = pd.DataFrame(intermediate_X, intermediate_y)
        intermediate_df = pd.DataFrame(re_x, re_y)
        store_df = pd.concat([store_df, intermediate_df], axis=0)

print(store_df)

# save csv
#store_df.to_csv('reample.csv')