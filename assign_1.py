
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
os.chdir(r"C:\Hogwarts\advanced_analytics")

# Reading the data into a dataframe
housing = pd.read_csv("Housing.csv")
print(housing)


# Skewness
sk = housing['price'].skew()
print("Skewness is: ",sk)


# Kurtosis
kt = housing['price'].kurtosis()
print("Kurtosis is: ",kt)


# Histogram
sns.histplot(data = housing,
             x= 'price',
             bins= 5)
plt.show()


# Scatter
sns.scatterplot(
    data = housing,
    x= 'lotsize', y= 'price',
    hue= 'airco')

plt.title("Scatter Plot")
plt.xlabel("Lot Size")
plt.ylabel("price")
plt.show()


# Boxplots
sns.boxplot(
    x= 'bedrooms',
    y= 'lotsize',
    data = housing)
plt.show()


# Sub Plots

plt.subplot(2,2,1)
sns.boxplot(
    data = housing,
    y= 'price')

plt.subplot(2,2,2)
sns.histplot( data = housing,
             x= 'price',
             bins = 5)

plt.subplot(2,2,3)
sns.scatterplot(data = housing,
                x= 'lotsize',
                y= 'price',
                hue = 'airco')

plt.subplot(2,2,4)
sns.boxplot( y= 'bathrms',
            data = housing)

plt.tight_layout()
plt.show()


# Facet grid

g= sns.FacetGrid(housing, col='bathrms')
g= g.map(plt.scatter,
         "lotsize",
         "price")
plt.show()














