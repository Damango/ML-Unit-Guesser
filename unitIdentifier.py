import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
dataset = pd.read_csv('units.csv')

X = dataset.iloc[:, 3].values
y = dataset.iloc[:, [0, 1, 2, 4]].values
# print(X)
# print(y)


ohe = OneHotEncoder()

ct = ColumnTransformer(
    transformers=[('Type', OneHotEncoder(), [0])], remainder="passthrough")


otherCt = ColumnTransformer(
    transformers=[('Element', OneHotEncoder(), [7])], remainder="passthrough")


y = ct.fit_transform(y)
y = otherCt.fit_transform(y)


# print(y)


x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)


print(y_test)


regressor = LinearRegression()
regressor.fit(y_train, x_train)

print(regressor.predict(y_test))
