from flask import Flask, render_template, request
from joblib import load

# Load the saved model and vectorizer
loaded_model, loaded_vectorizer = load("SVC_models.joblib")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form['news_content']

        # Transform the input using the loaded vectorizer
        transformed_text = loaded_vectorizer.transform([news_text])

        # Make prediction
        prediction = loaded_model.predict(transformed_text)[0]

        # Map the result
        result = "FAKE News ❌" if prediction == 0 else "REAL News ✅"
        return render_template('index.html', prediction_text=result)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
