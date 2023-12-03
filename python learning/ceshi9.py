from sklearn.datasets import load_iris
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import LabelEncoder


breast_cancer = load_breast_cancer()
iris = load_iris()
data = breast_cancer['data']
df = pd.DataFrame(iris['data'], columns=list(iris['feature_names']))
# target = breast_cancer['target']
# # print(data.shape)
# # print(target.shape)
# all_datas = np.c_[data, target]
# all_datas_df = pd.DataFrame(all_datas, columns=list(breast_cancer['feature_names'])+['target'])
# # print(all_datas_df)
# all_datas_df['target'] = all_datas_df['target'].replace(all_datas_df['target'].unique(), breast_cancer['target_names'])
# # print(all_datas_df)
# data_train, data_test, target_train, target_test = train_test_split(data, target, random_state=40, test_size=0.25)
# print(data_test, data_train)
# print(list(breast_cancer.keys()))
labelEncoder = LabelEncoder()
print(df.select_dtypes(include='float').columns)
df['sepal length (cm)'] = pd.cut(df['sepal length (cm)'], bins=[4, 5, 6, 7, 8])
df_n = pd.get_dummies(df['sepal length (cm)'])
print(df_n)

