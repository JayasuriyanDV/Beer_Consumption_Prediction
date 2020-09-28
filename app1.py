from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('BeerConsumption_random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method =='POST':
        MedTemp= float(request.form['MedTemp'])
        MinTemp= float(request.form['MinTemp'])
        MaxTemp= float(request.form['MaxTemp'])
        Precipitation= float(request.form['Precipitation'])
        EndofWeek= request.form['EndofWeek']
        if EndofWeek == 1:
            EndofWeek=1
        else:
            EndofWeek=0
        
            
        prediction=model.predict([[MedTemp,MinTemp,MaxTemp,Precipitation,EndofWeek]])
    
        output=round(prediction[0],2)
    
        if output<0:
            return render_template('index.html',prediction_text= "Sorry")
        else:
            return render_template('index.html',prediction_text="Your Beer Consumption is {}".format(output))
    else:
        return render_template('index.html')
    

if __name__=="__main__":
    app.run(debug=True)

    