# Library untuk manipulasi data
import pandas as pd
import matplotlib.pyplot as plt

# Import data csv
df = pd.read_csv('dataset.csv')

# print(df.head()); print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe().round())

# convert dtype of DATE, object to datetime64[ns]
df['date'] = pd.to_datetime(df['date'])
# conver dtype of TIME, object to timedelta64[ns]
df['time'] = pd.to_timedelta(df['time']+' :00')

"""
df['year_name'] = df['date'].dt.year
df['month_name'] = df['date'].dt.month
df['date_name'] = df['date'].dt.day
"""

# convert dtype of TIME, object to int64
#df['time'] = pd.to_datetime(df['time'], format='%H:%M').dt.hour

#print(df.dtypes)
#print(df.head())

# grouping PRODUCT by TERJUAL
prod_terjual = pd.DataFrame(df.groupby('product').sum()['terjual'])
# sorting prod_terjual menurun
prod_terjual.sort_values(by=['terjual'], inplace=True, ascending=False)
print(prod_terjual[:5])

"""
tes = pd.DataFrame(df.groupby(['product', 'date']).sum()['terjual'])
print(tes)
"""

# data penjualan satu bulan terakhir
last_month = pd.DataFrame(df.sort_values(by='date',ascending=True)
            .set_index('date').last('1M')
            .groupby(['date']).sum()['terjual']
            )

last_month.plot(figsize=(14,7))
plt.xlabel('Tanggal')
plt.ylabel('Penjualan')
#plt.show()
#print(last_month)
last_month.sort_values(by='terjual', inplace=True, ascending=False)
#print(last_month)
print('Puncak pembelian pada')
print(last_month[:1])
#print('dengan ', last_month[1][0] , ' penjualan')




"""
# grouping DATE by TERJUAL
date_terjual = pd.DataFrame(df.groupby('date').sum()['terjual'])
date_terjual.sort_values(by=['terjual'], inplace=True, ascending=False)
print(date_terjual[:10])

# grouping DATE setiap bulan by TERJUAL
perbln_terjual = pd.DataFrame(df.groupby(pd.Grouper(key='date', freq='1M')).sum()['terjual'])
print(perbln_terjual)

# grouping DATE setiap hari by TERJUAL
perhr_terjual = pd.DataFrame(df.groupby(pd.Grouper(key='date', freq='1D')).sum()['terjual'])
print(perhr_terjual[len(perhr_terjual)-30:])

# grouping DATE setiap minggu by TERJUAL
permg_terjual = pd.DataFrame(df.groupby(pd.Grouper(key='date', freq='7D')).sum()['terjual'])
print(permg_terjual[len(permg_terjual)-4:])
"""
##################################
"""
from datetime import date, timedelta

last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)

start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)

# For printing results
print("First day of prev month:", start_day_of_prev_month)
print("Last day of prev month:", last_day_of_prev_month)
"""