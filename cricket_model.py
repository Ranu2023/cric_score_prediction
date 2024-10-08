from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# # Load the model
model = pickle.load(open('cricket_model.pkl', 'rb'))

# Define a function for one-hot encoding
def one_hot_encode(data):
    # Assuming 'batting_team' and 'bowling_team' are the categorical features
    return pd.get_dummies(data, columns=['batting_team', 'bowling_team'], drop_first=True)

@app.route('/')
def home():
    return render_template('cricket_index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get features from the form
    batting_team = request.form['batting_team']
    bowling_team = request.form['bowling_team']
    # Add other features as needed
    overs = float(request.form['overs'])  # Make sure this is a float
    wickets = int(request.form['wickets'])  # Make sure this is an integer

    # Create a DataFrame for the input features
    features = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'overs': [overs],
        'wickets': [wickets]
    })

    # One-hot encode the features
    features_encoded = one_hot_encode(features)

    # Make sure the model receives the same feature set it was trained on
    features_encoded = features_encoded.reindex(columns=model.feature_importances_.index, fill_value=0)

    # Predict the score
    prediction = model.predict(features_encoded)

    return f'Predicted Score: {prediction[0]}'

if __name__ == '__main__':
    app.run(debug=True)
