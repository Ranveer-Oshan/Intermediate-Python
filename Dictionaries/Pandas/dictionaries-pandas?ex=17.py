# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])


# Print out observations for Australia and Egypt
print(cars.iloc[[1,6]])
