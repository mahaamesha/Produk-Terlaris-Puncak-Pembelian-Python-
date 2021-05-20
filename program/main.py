# Library untuk manipulasi data
import pandas as pd

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

# convert dtype of TIME, object to int64
#df['time'] = pd.to_datetime(df['time'], format='%H:%M').dt.hour

#print(df.dtypes)
#print(df.head())

# grouping PRODUCT by TERJUAL
prod_terjual = pd.DataFrame(df.groupby('product').sum()['terjual'])
# sorting prod_terjual menurun
prod_terjual.sort_values(by=['terjual'], inplace=True, ascending=False)
print(prod_terjual[:5])

# grouping DATE by TERJUAL
date_terjual = pd.DataFrame(df.groupby('date').sum()['terjual'])
date_terjual.sort_values(by=['terjual'], inplace=True, ascending=False)
print(date_terjual[:100])

# grouping DATE setiap freq by TERJUAL
perminggu_terjual = pd.DataFrame(df.groupby(pd.Grouper(key='date', freq='1M')).sum()['terjual'])
print(perminggu_terjual)