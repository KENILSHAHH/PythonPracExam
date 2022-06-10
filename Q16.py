#this code will not run until you have the csv file and the pandas module installed in your local machine

import pandas as pd
  
# Reading the CSV file
df = pd.read_csv("Iris.csv")
  
# Printing top 5 rows
df.head()