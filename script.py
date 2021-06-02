# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:31:40 2021

@author: TAC
"""

from glob import glob
import pandas as pd
import numpy as np
data=[]
acc=[]

language='Spanish'

for csv in glob('submissions/{}/*.csv'.format(language)):
    acc.append(np.round(float(csv.split('_')[1][0:-4]),3))
    data.append(pd.read_csv(csv).iloc[:,-1])
    
mean=np.average(data,axis=0,weights=acc)
mean=np.where(mean>0.5,1,0)

unique, counts = np.unique(mean, return_counts=True)
print(dict(zip(unique, counts)))


df=pd.read_csv(csv)
df.type=mean
import os 
os.makedirs('submissions/{}/output'.format(language))

for row in df.index:
    xml = []
    xml.append('<author id="{}"'.format(df.loc[row,'author-id']))
    xml.append('lang="{}"'.format(df.loc[row,'lang']))
    xml.append('type="{}"'.format(df.loc[row,'type']))
    xml.append('/>')
    x='\n'.join(xml)
    myfile = open("submissions/{}/output/{}.xml".format(language,df.loc[row,'author-id']), "w")
    myfile.write(x)
    myfile.close()