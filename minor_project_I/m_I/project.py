import numpy as np
import pandas as pd
import math
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix



breast_cancer_data = pd.read_csv("data.csv")
df=breast_cancer_data.drop('Unnamed: 32',axis=1)
df.drop('id',axis=1,inplace=True)




labelencoder_Y = LabelEncoder()
df.iloc[:,0] = labelencoder_Y.fit_transform(df.iloc[:,0].values)


X=df.drop('diagnosis',axis=1)
Y=df['diagnosis']
x_scale=MinMaxScaler().fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(x_scale, Y, test_size = 0.25, random_state = 0)



forest=rf(n_estimators=10,criterion='entropy',random_state=0)
forest.fit(X_train,Y_train)



conf_mat = confusion_matrix(Y_test,forest.predict(X_test))
print(conf_mat)
TP = conf_mat[0][0]
TN = conf_mat[1][1]
FN = conf_mat[1][0]
FP = conf_mat[0][1]
accuracy = (TP + TN)/(TP + TN + FN + FP)
print("Testing Accuracy = ", accuracy*100)