
import pandas as pd
import numpy as np #unused
import matplotlib.pyplot as plt
import seaborn as sns

import os
os.chdir(r"C:\Hogwarts\advanced_analytics")

car = pd.read_csv("Cars93.csv")
print(car.info())

cts = car['Type'].value_counts()
cts.plot(kind='bar')
plt.show()

#Matplotlib
plt.bar(cts.index, cts)
plt.show()

#Seaborn
cts_s = cts.reset_index()
cts_s.columns = ['Type','Count']
sns.barplot(data=cts_s , x='Type', y='Count')
plt.show()

cts_s = cts.reset_index()
cts_s.columns = ['Type','Count']
sns.barplot(data=cts_s , x='Count', y='Type')
plt.show()

