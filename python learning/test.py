import pandas as pd


def aaa(x):
    a = x.split('|')
    if "建" in a[1]:
        return True
    else:
        return False


df = pd.read_excel(r'C:\Users\yzwei\Downloads\长沙二手房_230821_1692604744.xlsx')
ind = df[df['houseInfo'].apply(aaa)].index
new = df.iloc[ind]
ind_1 = list(set(df.index)-set(ind))
old = df.iloc[ind_1]
n = pd.pivot_table(new, index='area', aggfunc='size')
o = pd.pivot_table(old, index='area', aggfunc='size')
a = pd.DataFrame(data=[n, o],index=['new', 'old']).T
a.fillna(0, inplace=True)
print(a)

