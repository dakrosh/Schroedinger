import numpy as np
import pandas as pd
import os

# Example of variable
# NASDAQ_data = pd.read_csv('../Data/NASDAQ/Cocoa.csv')

# Example of if-else
# if(condition):
#     # Code
# else:
#     # Code

# Example of for loop
# for i in range(number of iterations):
#     # Code

# Example of while loop
# while(condition):
#     # Code

# Example of function
def main():
    file_path = input("Enter the path to the file: ")
    df = pd.read_csv(file_path)
    if df is not None:
        print(df)
    df['Date'] = pd.to_datetime(df['Date'])
    range_date = pd.date_range(start = df.loc['Date'].min(), end = df.loc['Date'].max())
    df.set_index(keys='Date')
    df.reindex(labels=range_date)
    df.reset_index()
        
main()
    


#create individual months and their conditions (numDays, holidays, leapYear(February), etc.)

 