import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


# house = pd.read_excel(r'C:\Users\yzwei\Downloads\长沙二手房_230821_1692604744.xlsx')
# imputer = SimpleImputer(missing_values=np.NaN, strategy='mean')
# house[['totalPrice']] = imputer.fit_transform(house[['totalPrice']])
# columns = house.select_dtypes(include='float').columns
# # print(house['totalPrice'])
# print(house[columns])

a = pd.DataFrame([[['a', 'b', 'c']], [['a', 'b', 'c']]])
print(a.iloc[0, 0])
