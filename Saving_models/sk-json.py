#pip install sklearn-json

import sklearn_json as skljson

file_name = "abc.json"
skljson.to_json(model, file_name)

deserialized_model = skljson.from_json('abc.json')
