from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("Model_random_forsest_diabetes.pkl")
scaler = joblib.load("scaler_diabetes.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        pregnancies = float(request.form["Pregnancies"])
        glucose = float(request.form["Glucose"])
        blood_pressure = float(request.form["BloodPressure"])
        skin_thickness = float(request.form["SkinThickness"])
        insulin = float(request.form["Insulin"])
        bmi = float(request.form["BMI"])
        diabetes_pedigree = float(request.form["DiabetesPedigreeFunction"])
        age = float(request.form["Age"])

        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                                insulin, bmi, diabetes_pedigree, age]])

        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)[0]

        if prediction == 1:
            result = "Terindikasi berisiko diabetes"
        else:
            result = "Tidak terindikasi diabetes"

        return render_template("index.html", hasil=result)

    except Exception as e:
        return render_template("index.html", hasil=f"Terjadi error: {e}")

if __name__ == "__main__":
    app.run(debug=True)