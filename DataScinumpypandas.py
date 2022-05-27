"""data sci oct 20th 21
"""
import numpy as np
"""
n = np.NaN
a = np.random.randn(5)
b=a.mean()
c=np.random.random(5)
d=np.random.randint(500,600,20)
e= np.random.uniform(10,20,100)
f=np.random.normal(size=100)
print(n,a,"\n",b,"\n",c,"\n",d,"\n",e)
"""

data1=np.random.randint(100,300,50)
data2=data1+ np.random.normal(size=50)

print(np.corrcoef(data1,data2))