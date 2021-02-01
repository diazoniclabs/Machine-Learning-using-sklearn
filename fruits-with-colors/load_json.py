import sklearn_json as skljson
import pickle
deserialized_model = skljson.from_json('lr_model.json')
from sklearn.preprocessing import MinMaxScaler
with open('scaler.json','rb') as f:
    scaler = pickle.load(f)

deserialized_model.predict(scaler.transform([[152,6.5,8.5,0.72]]))
