import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.chdir(r"C:\Hogwarts\advanced_analytics")

car = pd.read_csv("Cars93.csv")
print(car.info())

cts = car['Price'].value_counts()

#Seaborn
cts_s = cts.reset_index()
cts_s.columns = ['Price','Count']
sns.barplot(data=cts_s , x='Price', y='Count', bins=10)
plt.show()

# Scatter Plot

#pandas
car.plot(kind='scatter', x='EngineSize' , y='MPG.highway')
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on highway")

#Matplotlib
plt.scatter(car['EngineSize'], car['MPG.highway'])
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on highway")
plt.show()

#Seaborn

sns.scatterplot(data=car, x='EngineSize' , y='MPG.highway')
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on highway")
plt.show()

no_bags=[car['AirBags']=='none']
car['AirBags'].value_counts()

#Seaborn
sns.scatterplot(data=car, x='EngineSize' , y='MPG.highway',hue='AirBags')
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on highway")
plt.show()

sns.boxplot(y="Price",x='AirBags',data=car)
plt.show()

plt.subplot(3,3,1)
sns.histplot(data=car,x='Price', bins=8)
plt.title("Histogram")

plt.subplot(3,3,2)
sns.boxplot(y='Price', data=car)
plt.title("Box plot")


plt.subplot(3,3,3)
sns.histplot(data=car,x='Price', bins=8)
plt.title("Histogram")

plt.subplot(3,3,4)
sns.boxplot(y='Price', data=car)
plt.title("Box plot")


plt.subplot(3,3,5)
sns.histplot(data=car,x='Price', bins=8)
plt.title("Histogram")

plt.subplot(3,3,6)
sns.boxplot(y='Price', data=car)
plt.title("Box plot")

plt.subplot(3,3,7)
sns.histplot(data=car,x='Price', bins=8)
plt.title("Histogram")

plt.subplot(3,3,8)
sns.boxplot(y='Price', data=car)
plt.title("Box plot")

plt.subplot(3,3,9)
sns.histplot(data=car,x='Price', bins=8)
plt.title("Histogram")

plt.tight_layout()
plt.show()



















