"""
DATA SCIENCE 29THOCT 2021
DATA PREPROCESSING
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:25:44 2021

@author: DELL
"""
#analyse, predict -- model --
#Input:data --> (m) --> output :prediction
list1=[12,23,34,45]
list2=[45,67,65,54]
list1+list2
a=[]
a.append(1)
## Libraries -- Numpy Numerical Python,

## array -- list, math oper possible, 1d, 2d, 3d

import numpy as np
import pandas as pd



a1=np.array([11,34,78,90,42],dtype="int64") ## 1D array
a3=np.array([['a1','a2',1,2,3],['b1','b2',4,5,6],['c1','c2',7,8,9]])
a4 = np.array([[[11,12,13],[21,22,23],[31,32,33]],
              [[101,102,103],[201,202,203],[301,302,303]],
              [[911,912,913],[921,922,923],[931,932,933]],
              [[811,712,13],[91,90,63],[931,932,933]]])


"""
##Fetching---
1) 1D -- same as list
2) 2D -- a2[r,c]
3) 3S -- a3[s,r,c]
"""
a1+a1
a1*5
a1/4
"""
a3*a3 --- element multiplication
a3@a3 --- matrix multiplication
"""
a3.ndim
a3.size
a3.shape
a3.reshape(4,4)


## 00000000000000000000000000000000001011
## 00000000000000000000000000000000010000

## Empty array
a2=np.array()


##not a number -- NaN
n=np.NaN

## Random Functions
a=np.random.randn(5) ## 1 arg == size , normalized data -- -ve, +ve
a.mean()

np.random.random(5) ## 1 arg == size, 0 -1
np.random.randint(500,600,20) ## 3 arg -- low, high, size
np.random.uniform(10,20,100)
aa=np.random.normal(size=100)
aa.mean()
plt.plot(aa)

#Task -- find corelation between randomly generated data
data1 = np.random.random(100)
data2 =data1 +np.random.randint(10,50,100)

np.corrcoef(data1,data2)


"""
## Pandas

## Series -- similar to array, index the row, can be feed as a col to df
## Dataframes -- excel col names, row names
series -- col of df
dict() -- row col mapp
list()  -- col of df
arrays   -- col of df

## Load the dataset -- import , pre-processing
## View
## data cleaning
## filling the missing value
## Merging
## Duplicate

## Corel
## plot -- pandas for plotting

"""

#==================================PANDAS===============================================
s1=pd.Series(a, index=['id1','id2','id3','id4','id5'])
s2=pd.Series(a1, index=['id1','id2','id3','id4','id6'])

df1=pd.DataFrame([s1,s2])

## Empty DF
df2=pd.DataFrame()
df2['alpha']=s1 ## Adding a col with name alpha, data feed is s1
df2['beta']=s2  ## Adding a col with name beta, data feed is s2

df21=pd.DataFrame()
df21['col1']=a
df21['col2']=a1


# DF using Dict -- key is col, val are rows
df3=pd.DataFrame({'Emp_name':['anuroop','Amyra','Arnav','Arush','Adit'],
                  'Emp_age':[28,29,18,32,24]},
                 index=['id1','id2','id3','id4','id5'])
df3['Emp_dept']=['HR','HR','Admin','HR','HR']

## Fetching the data
df3['Emp_name']
df3[['Emp_name','Emp_dept']]

df3.loc['id1'] #-- label locing of rows
df3.iloc[0] #-- integer locing of row
df3[['Emp_name','Emp_dept']].loc[['id1','id2']]


## row merging
## col merg
## concat -- default for row , columnwise
## axis =0 -- row
## axis =1, column
## merge -- default for col -- requires a common col
## on- takes common col of two,..dfs

df1 =pd.DataFrame({'a':[1,2,3,4],'b':[11,12,13,14]},
                  index=[80,81,82,83])
df11 =pd.DataFrame({'a':[21,22,23,24],'b':[11,12,13,14]})
df2 =pd.DataFrame({'c':[21,22,23,24],'d':[11,12,13,14]})
df21 =pd.DataFrame({'a':[1,12,3,14],'c':[21,22,23,24],'d':[11,12,13,14]})
df3 = pd.DataFrame({'e':[1,2,3,4],'f':[11,12,13,14]},
                    index=[80,83,85,87])

concat([df1, df2])
concat([df1, df2], axis=1)
concat([df1, df11])
concat([df1, df11], axis=1)


merge(df1, df2) # no common col --error
merge(df1, df2, on=df1.index) ## wrong way

## common col == a
merge(df1, df21) ## only common rows of both df
merge(df1, df21, how='left')
## give all rows of left , if data is missing, fill NaN
merge(df1, df21, how='right')
## give all rows of right , if data is missing, fill NaN
merge(df1, df21, how='inner') # default value of how

raw_df=pd.merge(df1,df21,how='outer') ## give all rows of both df

## Missing Value Tratment
## find nan value
raw_df.isnull()
raw_df.isnull().sum()
raw_df.isna().sum()

## Drop, replace
raw_df.dropna() ## null value rows, are droped
raw_df.dropna(axis=1)
raw_df[['a','b']].dropna(axis=1)

## Replace--
raw_df.fillna(89) ## random way
raw_df['b'].fillna(raw_df['b'].mean()) ## filling specific col with specific val

raw_df.fillna(method='ffill')
raw_df.fillna(method='bfill', inplace=True)

## inplace =True is saving back into original df


## Ex -- data load, view, missing, fill remove, concat-merge, duplicates
## wrong values -- fill, remove
## data reconcillation --

## ready for model building











