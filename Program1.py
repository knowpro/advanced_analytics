import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cars93=pd.read_excel("Cars93.xlsx")
print(cars93.shape)
print(cars93.columns)
print(cars93.dtypes)
print(cars93.info())

print("Mean")
cars93['Price'].mean()

print("Median")
cars93['Price'].median()

print("Mean 0.75")
cars93['Price'].mean()

print("Quantile 0.25")
cars93['Price'].quantile(q=0.25)
 
cars93['price'].quantile(q=np.array([0.25,0.5,0.75]))

cars93['price'].plot(kind='box')
plt.show()
cars93['price'].std()
cars93['price'].var()

cv = cars93['price'].std()/cars93['price'].mean()


# Kurtosis

from scipy.stats import kurtosis
kurtosis(cars93['Price'], fisher = True)
cars93['Price'].kurtosis









