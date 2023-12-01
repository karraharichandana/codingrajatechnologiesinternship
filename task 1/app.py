from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the Naive Bayes model and TF-IDF vectorizer
loaded_nb_model = joblib.load('naivebayes.joblib')
loaded_tfidf_vectorizer = joblib.load('vectorizer1.joblib')

# Mock preprocessing function, replace with actual preprocessing logic
def preprocess_text(text):
    return text.lower()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input text from the form
    user_input = request.form['textInput']

    # Clean and preprocess the user input
    user_input_processed = preprocess_text(user_input)

    # Use the loaded TF-IDF vectorizer to transform the input text
    unseen_tfidf_features = loaded_tfidf_vectorizer.transform([user_input_processed])

    # Make predictions on the input text using the loaded Naive Bayes model
    unseen_predictions = loaded_nb_model.predict(unseen_tfidf_features)

    # Return predictions as JSON
    return jsonify({'prediction': unseen_predictions.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
