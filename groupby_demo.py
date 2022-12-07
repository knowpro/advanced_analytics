import pandas as pd

import os
os.chdir(r"C:\Hogwarts\advanced_analytics")

car = pd.read_csv("Cars93.csv")
print(car.head(6))
print(car.columns)

# Group By

no_bags = car[car["AirBags"] == 'None']
car.groupby('AirBags')['Price'].mean()


