"""
import pandas as pd
Date Nov 24th
# import the file
titanic = pd.read_excel(r"/Users/purnimagebhardt/Downloads/titanic3.xls")

#view the data
titanic.head()
titanic.tail()
titanic.info()
titanic.describe()
titanic.count()
titanic.min()
titanic['pclass'].unique()
titanic['pclass'].nunique()
titanic['pclass'].value_counts()
titanic['gender'].value_counts()
pd.crosstab(titanic['pclass'],titanic['gender'])
gr=titanic.groupby(by='pclass')
gr.get_group(1)

#missing values
titanic.isna().sum()
titanic.isnull().sum()

#drop na
titanic.dropna()#drop all the rows where missing values were there
titanic.dropna(axis=1)

#fillna
titanic['age'].fillna('0',inplace=True)
#titanic['age'].fillna(method="ffill",inplace=True)
titanic.drop(['cabin','boat','body','home.dest'],axis=1,inplace=True)
titanic.dropna(inplace=True)
#wrong values cleaing
titanic['age'].loc[titanic['age']=='AAAA'] = 0
#df[key]or df[list of keys]
titanic[0:]
#single col
titanic['parch']
titanic.fare
#multiple col
titanic[['pclass','age','fare']]
#singlerow
titanic.iloc[0:5]
titanic.iloc[10,15,100]
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 16:39:44 2021

@author: DELL
"""

# C:\Users\DELL\Downloads\titanic3.xls

# Pandas --
# File Loading, Analysis data, Missing Data, Fill Missing Values, Unique Values
# Data Fetching -- Column, Multiple column, row, multiple row
# Matplotlib plots
# line -- plt.plot
# multiline
# scatter -- plt.scatter
# bar -- plt.bar, plt.barh
# histogram -- plt.histogram
# pie -- plt.pie

import pandas as pd
import matplotlib.pyplot as plt
from numpy import*

# import the file
titanic=pd.read_excel(r"/Users/purnimagebhardt/Downloads/titanic3.xls")

#View The data
titanic.head()
titanic.tail()
titanic.info()
titanic.describe()
titanic.count()
titanic.min()
titanic['pclass'].unique()
titanic['pclass'].nunique()
titanic['pclass'].value_counts()
titanic['gender'].value_counts()
pd.crosstab(titanic['pclass'],titanic['gender'])
gr=titanic.groupby(by='pclass')
gr.get_group(1)

# Missing Values
titanic.isna().sum()
titanic.isnull().sum()

#  drop na
titanic.dropna() # drop all the rows where missing values were there
titanic.dropna(axis=1)

# fillna
titanic['age'].fillna(0,inplace=True)
# titanic['age'].fillna(method="ffill",inplace=True)
titanic.drop(['cabin','boat','body','home.dest'],axis=1,inplace=True)
titanic.dropna(inplace=True)

# wrong values cleaning
titanic['age'].loc[titanic['age']=='AAAA'] = 0

# df[key] or df[list of keys]
titanic[0:]
#  Single col
titanic['parch']
titanic.fare
# multiple col
titanic[['pclass','age','fare']]
# single row
titanic.iloc[0]
# Multiple rows
titanic.iloc[0:5]
titanic.iloc[[10,15,100]]

# barplot of survived and not survived
# histogram of age
# pclasswise fare -- line graph
# corelation plot

titanic.info()
titanic.drop('name',axis=1,inplace=True)

## Pandas plot
titanic['survived'].value_counts().plot(kind='barh')

plt.bar(['non-survived','survived'],titanic['survived'].value_counts())

aa=pd.crosstab(titanic['survived'], titanic['gender'])

plt.bar(['non-survived','survived'],
        aa['male'],width=0.6,color='skyblue',label='males')
plt.bar(['non-survived','survived'],
        aa['female'],width=0.3,color='purple',label='females')
plt.legend()

aa.plot(kind="bar")

plt.hist(titanic['age'],bins=50)

plt.plot(titanic['fare'],c=titanic['pclass'])

import seaborn as sn
sn.scatterplot(titanic['age'],titanic['fare'],hue=titanic['pclass'])
sn.pairplot(titanic[['fare','pclass','age','gender']])














