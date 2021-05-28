from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')
#print(df.head()); print(df.tail())

#print(df.shape)
#print(df.columns)
#print(df.info())
#print(df.describe().round())

df['date'] = pd.to_datetime(df['date'])
#df['time'] = pd.to_datetime(df['time'])
df['time'] = pd.to_timedelta(df['time']+' :00')

#print(df.dtypes)
print(df.head())

#DATA 1 BULAN TERKAHIR
last_month = (df.sort_values(by='date',ascending=True)
    .set_index('date').last('1M')
    )

#PRODUK TERLARIS
last_month_mostSelling = pd.DataFrame(last_month
    .groupby(['product']).sum()['terjual']
    )

last_month_mostSelling.plot.bar(title='Grafik Penjualan Akhir Bulan per Produk')
plt.xlabel('Product')
plt.ylabel('Penjualan')

last_month_mostSelling.sort_values(by='terjual', inplace=True, ascending=False)
print(last_month_mostSelling)
print('Produk terlaris adalah',
    last_month_mostSelling.index[0],
    'dengan', last_month_mostSelling['terjual'][0], 'penjualan.'
    )


#TANGGAL PUNCAK PENJULAN
last_month_bestDate = pd.DataFrame(last_month
    .groupby(['date']).sum()['terjual']
    )

last_month_bestDate.plot(title='Grafik Penjualan Akhir Bulan per Hari')
plt.xlabel('Tanggal')
plt.ylabel('Penjualan')

last_month_bestDate.sort_values(by='terjual', inplace=True, ascending=False)
print(last_month_bestDate.head())
print('Puncak pembelian pada',
    last_month_bestDate.index.strftime('%d %b %Y')[0],
    'dengan', last_month_bestDate['terjual'][0], 'penjualan.'
    )

#JAM PUNCAK PENJUALAN
last_month_bestHour = pd.DataFrame(last_month
    .groupby(pd.Grouper(key='time', freq='1H')).sum()['terjual']
    # jam xx.59 masuk ke perhitungan xx.00
    )

last_month_bestHour.plot(title='Grafik Penjualan Akhir Bulan Per Jam')
plt.xlabel('Jam')
plt.ylabel('Penjualan')
plt.show()
last_month_bestHour.sort_values(by='terjual', inplace=True, ascending=False)
print(last_month_bestHour.head())   # tanggal tercetak -> tanggal asli saat ini | perhatikan jam saja

print('Waktu penjualan tertinggi di jam',
    str(last_month_bestHour.index[0])[6:12], '-',
    str(last_month_bestHour.index[0]+timedelta(minutes=59))[6:12],
    'dengan', last_month_bestHour['terjual'][0], 'penjualan.'
    )