import pandas as pd
df = pd.read_csv('https://storage.googleapis.com/kagglesdsdata/datasets/9590/13660/fruit_data_with_colors.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20210201%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210201T171906Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=30af8a4f1bb07bf9c4490a58dcfcf3580e901a7f19bf63ec258ee400c0d2dfea965e0c0c7e6db0ab7b57481a616fc2bc508f776c470bcc745f90df6bb0252c9482d23b30ffc99de8758d4e48fe6d38f1a044aa6b1cf2770a0799a7c7a7dfc58ebb526c60fdcb3e181e301ef5360433a8317cdaf752415863c73b9c10270dfd4bfaaf5a60c099cb13b5afd0c85c6518776bef2fbbb4115bd2c023c4db3ac1e14fe7549e5de4244bf48767830ef9fbc411e4ca97f93821027598226fc5725217cc24ed066281395826a740ec8e67beca8644aa35c523289b043597da5ebdd0122ff26226cdee3dc1d173c51c632e2dc2a88ebc032690182ceb68f3e1ecaff5904c',sep = '\t')
# Inputs and Output
x = df.iloc[:,3:7].values
y = df.iloc[:,1].values
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, random_state = 0)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train,y_train)
#pip install sklearn-json

import sklearn_json as skljson
import pickle
model_name = "lr_model.json"
scaler_name = "scaler.json"
skljson.to_json(model, model_name)

with open('scaler.json', 'wb') as f:
    pickle.dump(scaler, f)
