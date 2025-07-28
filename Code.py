import pandas as pd
import os
import matplotlib.pyplot as plt

print(os.getcwd())


def load_data(file_path):
    df = pd.read_csv(file_path, index_col=0)
    return df

x = load_data('helen_2015_2024_v2.csv')
#print(x.describe())
print(x.isnull().sum()) 
print(x.columns)

plt.figure(figsize=(10, 5))
plt.title('Energy requirement over time')
plt.plot(x.index, x['dh_MWh'], color='green')
plt.xlabel('Date')
plt.ylabel('Energy (MWh)')
plt.grid(True)
plt.show()


'''
Working code:
df=pd.read_csv('helen_2015_2024_v2.csv', index_col=0)
print(df.head())
'''
