import numpy as np
import pandas as pd
df=pd.read_csv('Mobile phones.csv')
df1=df
df1.reset_index(inplace=True)
df1['price']=df1['price'].str.replace('₹','').str.replace(',','').astype('int')
temp=df1[df1['price']<3000]
df1.drop(temp.index,inplace=True)
brand_name=df1['model'].str.split(' ').str.get(0).str.lower()
df1.insert(2,'Brand_name',brand_name)
df1['model'].str.lower()
df1=df1.drop(727)
temp=df1[df1['processor'].str.contains('No Wifi')]
x=temp.iloc[:,7:].shift(-1,axis=1).values
df1.loc[temp.index,temp.columns[7:]]=x
#df1.to_excel('df2.xlsx',sheet_name='sh1')
t=df1[df1['index']==830]
x1=t.iloc[:,7:].shift(1,axis=1).values
df1.loc[t.index,t.columns[7:]]=x1
#df1.to_excel('df3.xlsx',sheet_name='sh1')
df1.drop([448,518,945],inplace=True)
tem=df1.loc[[288,130,633,797,927]]
#print(tem.iloc[:,9:])
x2=tem.iloc[:,9:].shift(1,axis=1)
df1.loc[tem.index,tem.columns[9:]]=x2
#print(df1.loc[[288,130,633,797,927]])
#df1.to_excel('df3.xlsx',sheet_name='sh1')
t1=df1[df1['camera'].str.contains("Display")]
x3=t1.iloc[:,11:].shift(-1,axis=1)
df1.loc[t1.index,t1.columns[11:]]=x3
#df1.to_excel('df4.xlsx',sheet_name='sh1')
t2=df1[df1['card'].str.contains("Android")]
x4=t2.iloc[:,12:].shift(1,axis=1)
df1.loc[t2.index,t2.columns[12:]]=x4
df1.to_excel('phones.xlsx',sheet_name='clean')