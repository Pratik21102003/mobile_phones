import numpy as np
import pandas as pd
df=pd.read_excel("phones.xlsx")
df1=df
has_5g=[]
has_blast=[]
has_nfc=[]
processor_name=[]
core=[]
power=[]
ram=[]
rom=[]
rom1=[]
energy=[]
fast=[]
size=[]
resolution=[]
Front_camera=[]
l=[]
l1=[]
back=[]
df['sim']=df['sim'].str.strip()
has_5g=df1['sim'].str.contains('5G').replace(True,1).replace(False,0)
df1.insert(7,"has_5g",has_5g)
has_blast=df1['sim'].str.contains('IR Blaster').replace(True,1).replace(False,0)
df1.insert(9,"has_IR_Blaster",has_blast)
has_nfc=df1['sim'].str.contains('NFC').replace(True,1).replace(False,0)
df1.insert(8,"has_nfc",has_nfc)
df1.drop(['sim'],axis=1,inplace=True)
df['processor']=df['processor'].str.strip()
for i in df1['processor'].str.split(","):
   try:
     processor_name.append(i[0])
   except:
       processor_name.append(np.nan)
   try:
     core.append(i[1])
   except:
       core.append(np.nan)
x=[]
df1.insert(11,"processor_name",processor_name) 
df1.insert(12,"core",core)
df1['core']=df1['core'].str.replace('Octa Core Processor','Octa Core')
df1['core']=df1['core'].str.replace('Hexa Core Processor','Hexa Core')
df1['core']=df1['core'].str.replace('Nine Cores','others')
df1['core']=df1['core'].str.replace('Nine Core','others')
df1['core']=df1['core'].str.replace('Nine-Cores','others')
df1['core']=df1['core'].str.replace('Deca Core Processor','others')
temp=df1[(df1['core']==' 1.6 GHz Processor')|(df1['core']==' 1.3 GHz Processor')|(df1['core']==' 1.4 GHz Processor')|(df1['core']==' 2 GHz Processor')]
for i in temp['processor'].str.split(","):
  x.append(i[0])
df1.loc[temp.index,temp.columns[12]]=x
df1['core']=df1['core'].str.strip()
for i in df1['processor'].str.replace('\u2009','').str.split(","):
  try:
     power.append(i[-1])
  except:
       power.append(np.nan)
df1.insert(13,"power",power)
df1['power'].str.replace('others',' ')
df1.drop(['processor'],axis=1,inplace=True)
df1['ram'].str.strip().str.split(',')
for i in df1['ram'].str.strip().str.replace('MB','GB').str.replace('\u2009GB RAM',"").str.split(','):
  try:
     ram.append(i[0])
  except:
    ram.append(np.nan)
  try:
    rom.append(i[-1])
  except:
    rom.append(np.nan)
df1.insert(14,'ram(GB)',ram)
df1['ram(GB)'].replace('256 GB inbuilt','NaN',inplace=True)
df1['ram(GB)'].replace('64 GB inbuilt','NaN',inplace=True)
df1['ram(GB)'].replace('NaN',np.nan,inplace=True)
df1.insert(15,'rom',rom)
for i in df1['rom'].str.split('\u2009'):
     rom1.append(i[0])
df1.insert(14,'Rom',rom1)
df1.drop(['ram'],axis=1,inplace=True)
df1.drop(['rom'],axis=1,inplace=True)
fast=df1['battery'].str.contains('Fast').replace(True,1).replace(False,0)
df1.insert(16,'Fast Charging',fast)
for i in df1['battery'].str.split('mAh'):
  try:
    energy.append(i[0])
  except:
    energy.append(np.nan)
df1.insert(15,'Energy',energy)
df1.drop(['battery'],axis=1,inplace=True)
for i in df1['display'].str.split(' '):
  try:
    size.append(i[0])
  except:
    size.append(np.nan)
  try:
    resolution.append(i[2])
  except:
    resolution.append(np.nan)
df1.insert(17,'Screen Size',size)
df1.insert(18,'resolution',resolution)
df1['resolution']=df1['resolution'].str.replace(',',"")
df1.drop(['display'],axis=1,inplace=True)
df1['card']=df1['card'].str.contains('Not').replace(True,0).replace(False,1)
for i in df1['camera'].str.split('&'):
  try: 
     Front_camera.append(i[1])
  except:
     Front_camera.append(np.nan)
df1.insert(19,'Front_camera',Front_camera)
for i in df1['camera'].str.split('MP'):
  l.append (i[-2])
df1.insert(20,'Backcamera',l)
for i  in df1['Backcamera'].str.split('&'):
  back.append(i[0])
df1.insert(21,'Back_camera',back)
df1.drop(['Backcamera'],axis=1,inplace=True)
df1.drop(['camera'],axis=1,inplace=True)
df1.to_excel('done.xlsx',sheet_name='one')
df1.to_csv('Phones(cleaned).csv')