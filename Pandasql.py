import pandas as pd 
from pandasql import sqldf

df = pd.read_csv('Order_v3.csv', encoding='latin1')

query = 'select orderType , sum(quantity) Suma from df group by orderType'

result = sqldf(query)

print(result)

print(df.groupby('orderType')['quantity'].sum())


