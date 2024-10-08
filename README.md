Cricket Score Prediction

Overview

The Cricket Score Prediction project aims to predict the score of a cricket match based on various features like the batting team, bowling team, overs, wickets, and current runs. This project utilizes machine learning to make accurate predictions, helping fans and analysts understand potential match outcomes.

 Features

- User-friendly web interface for inputting match details
- Machine learning model for score prediction
- Responsive design for accessibility on various devices
- Prediction results displayed clearly

Technologies Used

- Backend: Flask (Python)
- Machine Learning: Scikit-learn
- Data Handling: Pandas
- Frontend: HTML, CSS (Tailwind CSS)
- Deployment: Render
- Web Server: Gunicorn

Installation

1. Clone the repository:
  bash
   git clone [https://github.com/Ranu2023/cric_score_prediction.git]
   
   cd cricket-score-prediction

3. Install the required packages:
bash
   pip install -r requirements.txt

Now train the model and after that one file created .plk 

THEN

3. Run the application:
bash
   python cricket_app.py


4. Usage
   
Open your web browser and navigate to http://127.0.0.1:5000.

Fill in the form with the details of the match.

Click on "Predict Score" to view the predicted score.


5. Deployment
To deploy the application on Render, follow these steps:

-Push your code to GitHub.

-Create a new web service on Render and link it to your GitHub repository.

-Set the start command to:
    gunicorn cricket_app:app




License
This project is licensed under the MIT License.
