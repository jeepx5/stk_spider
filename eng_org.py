import pandas as pd
import re

pattern = u'(.+)'

df = pd.read_csv('eng_org.csv')
print(df.head(3))
#df['rateNum']=df['rateNum'].str.replace('na', '0')
df['meanprice']=df['meanprice'].str.replace('￥', '')

df['group']=df['shop'].str.replace(r'(\(.+)', '')
df['group']=df['group'].str.replace(r'(.s+)', '')
df_ft=df[df['meanprice']!='na']
df_ft.dropna(axis=0)
df_ft['meanprice']=df_ft['meanprice'].astype('int')
grouped = df_ft.groupby(df['group'])
exlst=list(df_ft.group)

grouped.count().to_csv('org_count.csv')
grouped.mean().to_csv('org_mean.csv')
grouped.describe().to_csv('org_describe.csv')
print(grouped.describe())
