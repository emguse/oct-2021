import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

con = sqlite3.connect('./test/env.db')
cur = con.cursor()

cur.execute('select * from enviroment')
l = cur.fetchall()
cur.close()

df = pd.DataFrame(l, columns=('id', 'datetime', 'tmp', 'hum', 'atm'))
df = df.drop('id', axis=1)
print(df)
df.plot(x='datetime', subplots=True)
plt.show()

plt.savefig('./test/fig_db.png')