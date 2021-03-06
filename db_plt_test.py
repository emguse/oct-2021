import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

con = sqlite3.connect('./test/env.db')
cur = con.cursor()
cur.execute('SELECT * FROM enviroment WHERE date >= DATETIME(\'now\', \'localtime\', \'-30 days\');')
l = cur.fetchall()
cur.close()
df = pd.DataFrame(l, columns=('id', 'datetime', 'tmp', 'hum', 'atm'))
df = df.drop('id', axis=1)
print(df)
df.plot(x='datetime', subplots=True)
plt.show()
plt.savefig('./test/fig_30days.png')

con = sqlite3.connect('./test/env.db')
cur = con.cursor()
cur.execute('SELECT * FROM enviroment WHERE date >= DATETIME(\'now\', \'localtime\', \'-7 days\');')
l = cur.fetchall()
cur.close()
df = pd.DataFrame(l, columns=('id', 'datetime', 'tmp', 'hum', 'atm'))
df = df.drop('id', axis=1)
print(df)
df.plot(x='datetime', subplots=True)
plt.show()
plt.savefig('./test/fig_7days.png')

con = sqlite3.connect('./test/env.db')
cur = con.cursor()
cur.execute('SELECT * FROM enviroment WHERE date >= DATETIME(\'now\', \'localtime\', \'-1 days\');')
l = cur.fetchall()
cur.close()
df = pd.DataFrame(l, columns=('id', 'datetime', 'tmp', 'hum', 'atm'))
df = df.drop('id', axis=1)
print(df)
df.plot(x='datetime', subplots=True)
plt.show()
plt.savefig('./test/fig_1days.png')
