import json
values = {'coef':model.coef_[0],'intercept':model.intercept_}
with open("sample.json", "w") as outfile:  
    json.dump(values, outfile) 
