from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from geopy.geocoders import Nominatim

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

soil_data = [{'temperature': 20.87974371, 'humidity': 82.00274423, 'ph': 6.502985292}, {'temperature': 21.77046169, 'humidity': 80.31964408, 'ph': 7.038096361}, {'temperature': 23.00445915, 'humidity': 82.3207629, 'ph': 7.840207144}, {'temperature': 26.49109635, 'humidity': 80.15836264, 'ph': 6.980400905}, {'temperature': 20.13017482, 'humidity': 81.60487287, 'ph': 7.628472891}, {'temperature': 23.05804872, 'humidity': 83.37011772, 'ph': 7.073453503}, {'temperature': 22.70883798, 'humidity': 82.63941394, 'ph': 5.70080568}]



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
    # print()
    # geolocator = Nominatim(user_agent="geoapiExercises")
    
    # print( 'location',geolocator.geocode(f'{location[0]}, India').state)
    return render_template('result.html', result = res, path = f'assets/img/{res}.jpg', rainfall = rainfall)