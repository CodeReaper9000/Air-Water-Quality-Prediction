from flask import Flask, jsonify, request, render_template
import joblib

app = Flask(__name__)

# Load the trained models
aqi_model = joblib.load('random_forest_aqi_model.pkl')
wqi_model = joblib.load('random_forest_wqi_model.pkl')

# Route to display the home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/air_quality_prediction', methods=['GET'])
def air_quality_prediction():
    return render_template('air_quality_prediction.html')

@app.route('/water_quality_prediction', methods=['GET'])
def water_quality_prediction():
    return render_template('water_quality_prediction.html')

@app.route('/predict_aqi', methods=['POST'])
def predict_aqi():
    try:
        PM2_5 = float(request.form['PM2_5'])
        PM10 = float(request.form['PM10'])
        NO2 = float(request.form['NO2'])
        NOx = float(request.form['NOx'])
        NH3 = float(request.form['NH3'])
        CO = float(request.form['CO'])
        SO2 = float(request.form['SO2'])

        features = [PM2_5, PM10, NO2, NOx, NH3, CO, SO2]
        prediction = aqi_model.predict([features])
        aqi_value = round(prediction[0])

        if aqi_value <= 50:
            aqi_type = "Good"
            description = "Air Quality: Satisfactory, poses little or no risk. Health Impacts: No impact on health."
        elif aqi_value <= 100:
            aqi_type = "Satisfactory"
            description = "Air Quality: Acceptable, but for some pollutants, there may be a moderate health concern for a very small number of people who are unusually sensitive. Health Impacts: Minor breathing discomfort to sensitive individuals."
        elif aqi_value <= 200:
            aqi_type = "Moderate"
            description = "Air Quality: May cause breathing discomfort for people with lung diseases, like asthma, and discomfort for people with heart disease, children, and older adults. Health Impacts: Breathing discomfort to sensitive people."
        elif aqi_value <= 300:
            aqi_type = "Poor"
            description = "Air Quality: May cause breathing discomfort for most people on prolonged exposure. Health Impacts: Breathing discomfort to people on prolonged exposure and discomfort to people with heart disease."
        elif aqi_value <= 400:
            aqi_type = "Very Poor"
            description = "Air Quality: May cause respiratory illness in people on prolonged exposure. Health Impacts: Respiratory effects even in healthy people, serious impact on those with existing respiratory or heart conditions."
        elif aqi_value <= 500:
            aqi_type = "Severe"
            description = "Air Quality: Health warnings of emergency conditions. Health Impacts: Affects the entire population. Severe impacts on people with lung and heart conditions; everyone may experience serious health effects."
        else:
            aqi_type = "Hazardous"
            description = "Air Quality: Emergency conditions. Health Impacts: Serious risk to health for the entire population."

        return render_template('air_quality_prediction.html', prediction=aqi_value, type=aqi_type, description=description)
    except Exception as e:
        return render_template('air_quality_prediction.html', error=str(e))

@app.route('/predict_wqi', methods=['POST'])
def predict_wqi():
    try:
        temperature = float(request.form['temperature'])
        ph = float(request.form['ph'])
        do = float(request.form['do'])
        conductivity = float(request.form['conductivity'])
        nitrates = float(request.form['nitrates'])
        bod = float(request.form['bod'])
        total_coliform = float(request.form['total_coliform'])

        features = [temperature, ph, do, conductivity, nitrates, bod, total_coliform]
        prediction = wqi_model.predict([features])
        wqi_value = round(prediction[0])

        if wqi_value <= 25:
            wqi_category = "Excellent Water Quality"
            description = "Water is clean, healthy, and can be used for drinking with minimal treatment."
        elif wqi_value <= 50:
            wqi_category = "Good Water Quality"
            description = "Water is generally clean and suitable for most uses, including drinking with basic treatment."
        elif wqi_value <= 75:
            wqi_category = "Fair Water Quality"
            description = "Water has some pollution, may require treatment before use for drinking or other sensitive purposes."
        elif wqi_value <= 100:
            wqi_category = "Poor Water Quality"
            description = "Water is polluted and not suitable for drinking. Treatment is necessary for any use."
        else:
            wqi_category = "Very Poor or Unsuitable for Drinking"
            description = "Water is heavily polluted and dangerous for human consumption. Requires significant treatment or is unsafe for any use."

        return render_template('water_quality_prediction.html', prediction=wqi_value, category=wqi_category, description=description)
    except Exception as e:
        return render_template('water_quality_prediction.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
