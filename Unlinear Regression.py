import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('china_gdp.csv')
print(df.tail(10))
plt.figure(figsize=(10,10))
x_data,y_data=(df['Year'].values,df['Value'].values)
plt.plot(x_data,y_data,'r*',label='Gross Domestic Product in China')
plt.legend(loc='best')
plt.ylabel('GDP')
plt.xlabel('Year')
plt.show()
def yPredict(x,Beta_1,Beta_2):
    y=1/(1+np.exp(-Beta_1*(x-Beta_2)))
    return y
xdata=x_data/max(x_data)
ydata=y_data/max(y_data)
from scipy.optimize import curve_fit
popt,pcov=curve_fit(yPredict,xdata,ydata)
print('Beta1=%.4f, Beta2=%.4f' % (popt[0],popt[1]))
x=np.linspace(1960,2015,55)
x=x/max(x)
y=yPredict(x,*popt)
plt.figure(figsize=(10,10))
plt.plot(xdata,ydata,'ro',label='data')
plt.plot(x,y,'b*',label='fit')
plt.legend(loc='best')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.show()