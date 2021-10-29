import pandas as pd
import matplotlib.pyplot as plt

df_row = pd.read_csv('./test/20211028.csv', names=('tmp', 'hum', 'atm'))
print(df_row)

df_row.plot(subplots=True)
plt.show()

plt.savefig('./test/fig.png')