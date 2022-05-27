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


