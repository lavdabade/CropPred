from flask import Flask, render_template, request
import pandas as pd
import requests 
import json 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

data = pd.read_csv('data/weather-cleaned-data.csv')
X = data.drop('label',axis=1)
Y = data['label']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

model = RandomForestClassifier(max_depth=None,
max_features='auto',
min_samples_leaf= 1,
min_samples_split= 2,
n_estimators= 1000).fit(X_train,Y_train)

print(model.score(X_test,Y_test))


crop = ['rice', 'wheat', 'Mung Bean', 'Tea', 'millet', 'maize', 'Lentil', 'Jute', 'Coffee', 'Cotton', 'Ground Nut', 'Peas', 'Rubber', 'Sugarcane', 'Tobacco', 'Kidney Beans', 'Moth Beans', 'Coconut', 'Black gram', 'Adzuki Beans', 'Pigeon Peas', 'Chickpea', 'banana', 'grapes', 'apple', 
'mango', 'muskmelon', 'orange', 'papaya', 'pomegranate', 'watermelon']

KEY = 'C8KWK70N2FFC4P6H'
HEADER = '&results=7'


URL_T = 'https://api.thingspeak.com/channels/1657669/fields/1.json?'
URL_H = 'https://api.thingspeak.com/channels/1657669/fields/2.json?'

NEW_URL_T = URL_T + KEY + HEADER
NEW_URL_H = URL_H + KEY + HEADER
get_data_T = requests.get(NEW_URL_T).json()
get_data_H = requests.get(NEW_URL_H).json()

ft = get_data_T['feeds']
fh = get_data_H['feeds']

soil_data = []
for x,y in zip(ft,fh):
    soil_data.append({'temperature':float(x['field1']),'humidity':float(y['field2'].replace('\r\n\r\n',''))})

print('Soil data ',soil_data)


@app.route('/')
def home():
    return render_template('index.html', soil_data = soil_data)

temperature = 0
humidity = 0
for i in range(0,7):
    temperature += soil_data[i]['temperature']
    humidity += soil_data[i]['humidity']
print(temperature//7 , humidity//7 )
data = pd.read_csv('data/rainfall-cleaned.csv')


@app.route('/predict',methods=['POST'])
def predict():
    features = [x for x in request.form.values()]
    rainfall = 0
    i=0
    for (x,y) in zip(data['state'],data['district']):
        if str(x) == features[0] and str(y) == features[1]:
            rainfall = data['annual'][i]
        i += 1
    print(features)
    pred_data =np.array([temperature//7 , humidity//7, rainfall])
    pred_data = pred_data.reshape(1,-1)

    prediction = int(model.predict(pred_data))

    res = crop[prediction].capitalize()
    print('Resuly is ',res)
    return render_template('result.html', result = res, path = f'assets/img/{res}.jpg', rainfall = rainfall)