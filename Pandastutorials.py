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
################################################################################################################################################
#nov2nd
import pandas as pd

mtcars = pd.read_csv(r"/Users/purnimagebhardt/Downloads/mtcars.csv")#r-means regular expression
"""
print(mtcars.columns)
print(mtcars.index)
mtcars.info()
mtcars.describe()
print(mtcars.isnull().sum())

mtcars.head(2)
mtcars.tail(2)
mtcars.rename({"Unamed: 0":"carModels"},axis=1,inplace=True)
mtcars.count()

mtcars.gear.value_counts()
mtcars[["gear","carb"]].value_counts()
pd.crosstab(mtcars.gear,mtcars.carb)
#drop
mtcars.drop(['wt','vs'],axis=1,inplace=True)
##MISSING VALUES
##Duplicates
##Conditional Access
"""
#08Nov21
print(mtcars['mpg'])#col fetching
print(mtcars.iloc[7:10])#row fetching,integerlocation is used iloc
print("\n",mtcars[['mpg','gear']].iloc[7:10])

mtcars.rename({"Models":"carModels"},axis=1,inplace=True)
##mtcars[boolean mask]
print("Boolean mask",mtcars.mpg>19)##boolean mask
#task


print("%%%%%%%%%\n",mtcars[(mtcars.mpg>19) & (mtcars.gear==5)])
print("@@@@@@@@@\n",mtcars[['carModels','hp','drat','cyl']][mtcars.cyl==8])
print("*********\n",mtcars[['carModels','hp','drat','cyl']][mtcars.cyl==8].count())
pd.crosstab(mtcars.cyl,mtcars.gear)

#09Nov21
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
# import seaborn as sns

#df and series -- can be plotted using pandas
#hist, boxplot, bargraph, pie, scatter, line -- pandas, matplot
#heatmaps,pairplots, counterplots,distplots -- seaborn

df = pd.DataFrame(np.random.rand(10,4),columns=list('abcd'))
#variants of bar plot
df[['a','d']].plot.bar()##method1 --df.plot.bar()
df[['a','d']].plot(kind='barh',color=['pink','purple'])##method2 --df.plot.bar()
df[['a','d']].plot(kind='barh',stacked=True)
df[['a','d']].plot(kind='bar',stacked=True)

df3 = pd.DataFrame({"a":np.random.rand(1000),
                    "b":np.random.rand(1000)+1,
                    "c":np.random.rand(1000)-1,
                    "d":np.random.rand(1000)+1.5})

df3.a.plot.hist()
##Inference we understand here is 1000, 0-1,85 --120
df3.a.plot.hist(bins=200)
df3.plot.hist(bins=50,alpha=0.5)

col = {'boxes':'green','medians':'red','whiskers':'blue','caps':'blue'}
df3.boxplot(color=col)
##Inference -- statistical plot, comparison between different features
##median, min , max , quantites, outliers
df3.describe()

df3.plot(kind='scatter',x='a',y='d')
days=pd.Series([12,15,20,23,17,20,11])
days.plot(kind= 'pie')

mtcars.cyl.value_counts().plot(kind='pie',autopct='%1.2f%%')

"""
1. Plot count plot for gears - bar, pie
2. hp vs mpg -- kind = ?
3. stacked , grouped plot for cyl , carb -- matrix
4. range of mpg of cars -- kind=?
5. compare mpg of cars using boxplot nased on their carbs
5. hint use .boxplot(by=carb)
"""

mtcars.plot(kind='scatter',x='mpg',y='hp',hue='')
##########################################################################################################################################
#Datascience Nov22nd and 23rd
import pandas as pd
import matplotlib.pyplot as plt
mt = pd.read_csv(r"/Users/purnimagebhardt/Downloads/mtcars.csv")
#data --
#continuoous -- regression
#categorical -- classification
#checking if data is continuous or not
mt.info()
mt.cyl.unique()
mt.drat.nunique()#to check if n unique values
mt.hp.unique()
mt.gear.unique()

#Find Correlation positive or negative ,the more positive the better in most instances

c = mt[['mpg','hp']].corr()

plt.scatter(mt.mpg,mt.hp,label='correaltion is {}.format(c.iloc[0,1])')
plt.plot(mt.mpg,mod.predict(mt[['mpg']]),label='Prediction')
plt.xlabel('Mileage')
plt.ylabel('HorsePower')
plt.legend()
plt.grid()

##what is regression - plotting of continuous set of values
##y = m*x+c

##input -- mileage
##output -- hp
from sklearn.linear_model import LinearRegression

mod = LinearRegression()
mod.fit(mt[['hp','drat','disp']],mt[['mpg']])#fitting the line is the training process to help in prediction
mod.predict([[66,4,78]])
mod.score(mt[['hp','drat','disp']] , mt[['mpg']])

mod1 = LinearRegression()
mod1.fit(mt[['hp','drat']],mt[['mpg']])#fitting the line is the training process to help in prediction
mod1.predict([[66,4]])
mod1.score(mt[['hp','drat']] , mt[['mpg']])

mod2 = LinearRegression()
mod2.fit(mt[['hp']],mt[['mpg']])#fitting the line is the training process to help in prediction
mod2.predict([[66]])
mod2.score(mt[['hp']] , mt[['mpg']])

plt.scatter(mt.hp,mt.mpg,markers='D',c='red',label='corealtion is{}'.format(c.iloc[0,1]))
plt.plot(mt.hp,mod.predict(mt[['hp','drat','disp']]),'ko',label='Prediction by Mod')
plt.plot(mt.hp,mod1.predict(mt[['hp','drat']]),'g>',label='Prediction by Mod1')
plt.plot(mt.hp,mod2.predict(mt[['hp']]),'b-',label='Prediction by Mod2')
plt.xlabel('Horsepower')
plt.ylabel('Mileage')
plt.legend()
plt.grid()


############################################################################################################################################################################

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

