import numpy as np
import pandas as pd

df = pd.DataFrame({
    "id": [1001, 1002, 1003, 1004, 1005, 1006],
    "date": pd.date_range('20130102', periods=6),
    "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
    "age": [23, 44, 54, 32, 34, 32],
    "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
    "price": [1200, np.nan, 2133, 5433, np.nan, 4432]
})

df1 = pd.DataFrame({
    "id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "gender": ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
    "pay": ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y'],
    "m-point": [10, 12, 20, 40, 40, 40, 30, 20]
})

df.set_index('date', inplace=True)
df['price'].fillna(df['price'].mean(), inplace=True)
df['city'] = df['city'].str.strip().str.lower().str.capitalize()
df['price'] = df['price'].astype(int)
df.rename(columns={'category': 'category-size'}, inplace=True)
df['city'].replace('sh', 'Shanghai', inplace=True)

df = df.merge(df1, on='id', how='outer')
df['age'].fillna(df['age'].mean(), inplace=True)
df['price'].fillna(df['price'].mean(), inplace=True)
df.set_index('id', inplace=True)
df.sort_values(by='id', inplace=True)
df.dropna(inplace=True)
df2 = df['category-size']
df3 = pd.DataFrame([x.split('-') for x in df2], columns=['category', 'size'], index=df.index)
print(type(df3))
print(type(df))
print(df3)
print(df)
df = df.join(df3)
print(df)
