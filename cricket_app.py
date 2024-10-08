from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
model = pickle.load(open('cricket_model.pkl', 'rb'))

# Define a function for one-hot encoding
def one_hot_encode(data):
    # One-hot encode the batting and bowling teams
    return pd.get_dummies(data, columns=['batting_team', 'bowling_team'], drop_first=True)

@app.route('/')
def home():
    return render_template('cricket_index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get features from the form
    batting_team = request.form['batting_team']
    bowling_team = request.form['bowling_team']
    overs = float(request.form['overs'])  # Ensure this is a float
    wickets = int(request.form['wickets'])  # Ensure this is an integer

    # Create a DataFrame for the input features
    features = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'overs': [overs],
        'wickets': [wickets]
    })

    # One-hot encode the features
    features_encoded = one_hot_encode(features)

    # Make sure to align the columns with the model
    model_columns = model.feature_names_in_  # Get feature names from the model
    features_encoded = features_encoded.reindex(columns=model_columns, fill_value=0)

    # Predict the score
    prediction = model.predict(features_encoded)

    # Convert prediction to an integer
    predicted_score = int(prediction[0])  # Convert to an integer to remove decimals

    # Render the prediction in the template with the prediction text
    return render_template('prediction.html', prediction_text=f'Predicted Score: {predicted_score}')

if __name__ == '__main__':
    app.run(debug=True)
