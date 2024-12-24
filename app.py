app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Iris Classifier API! Use the /predict endpoint to classify new data."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.json['data']  # Expecting JSON with 'data' key
        input_data_scaled = scaler.transform([input_data])
        prediction_dt = best_model.predict(input_data_scaled)[0]
        prediction_rf = rf_model.predict(input_data_scaled)[0]
        return jsonify({
            'Decision Tree Prediction': data.target_names[prediction_dt],
            'Random Forest Prediction': data.target_names[prediction_rf]
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
