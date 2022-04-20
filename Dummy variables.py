#one hot encoding
import pandas as pd
import numpy as np
data1=pd.read_csv('F:/Assignments/Assignment 4 data pre processing/DataSets/animal_category.csv')
data1.dtypes
data1.info
data1.describe()

#now creating dummy variables, it converts non numeric data to numeric data in terms of 0's and 1's 
data2=pd.get_dummies(data1)
data1.drop(['Index'],axis=1,inplace=True)

#one hot encoding
from sklearn.preprocessing import OneHotEncoder  #here one hot encoding is using to create instances
enc= OneHotEncoder(handle_unknown='ignore')
enc_data1=pd.DataFrame(enc.fit_transform(data1).toarray())  #here array is converted to dataframe
enc_data1

#label encoding
from sklearn.preprocessing import LabelEncoder
labelencoder= LabelEncoder()
x=data1.iloc[:,0:4]  #input
y=data1['Types'] #output
data1.columns

x['Animals']=labelencoder.fit_transform(x['Animals']) 
x['Types']=labelencoder.fit_transform(x['Types'])  #in this two the non numeric data is converted to numeric in binary form

#label encoding of y
y=labelencoder.fit_transform(y)
y=pd.DataFrame(y)

data2=pd.concat([x,y],axis=1)
data2.columns
data2=data2.rename(columns={0:'Type1'})
data2






