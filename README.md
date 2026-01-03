# Phishing Website Detection System



## Abstract
This project is a web-based application designed to detect phishing websites in real-time using Machine Learning. By analyzing the linguistic and structural features of a URL, the system classifies it as **Legitimate** or **Phishing**. [cite_start]The backend is powered by **Django** and a **Logistic Regression** model trained on a dataset of over 11,000 URLs[cite: 4, 26].

## Features
* [cite_start]**Real-time URL Analysis**: Instantly predicts if a URL is safe or malicious[cite: 9].
* [cite_start]**ML-Based Engine**: Uses TF-IDF Vectorization and Logistic Regression for high accuracy[cite: 26].
* [cite_start]**Visual Verdicts**: Displays clear **Green (Safe)** or **Red (Phishing)** indicators[cite: 21].
* [cite_start]**Search History**: Automatically logs all scanned URLs and their results to the database[cite: 34].
* [cite_start]**Responsive Interface**: Built with Bootstrap for use on desktop and mobile[cite: 22].

## Tech Stack
* [cite_start]**Backend**: Python, Django
* **Machine Learning**: Scikit-Learn, Pandas, Numpy, Joblib
* [cite_start]**Frontend**: HTML, CSS, Bootstrap
* [cite_start]**Database**: SQLite (Default) 
* **Dataset**: 11,430 Labeled URLs (Legitimate vs Phishing)


⚙️ Installation & Setup
1. Clone the Repository
Download the project files to your local machine.

2. Create a Virtual Environment
Bash

python -m venv .venv
# Activate on Windows:
.venv\Scripts\activate
# Activate on Mac/Linux:
source .venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Train the Model
Before running the server, you must generate the trained model file (phishing_model.pkl).

Bash

python train_model.py
Output: "Model saved as 'phishing_model.pkl'"

5. Setup Database
Run migrations to create the SearchHistory table.

Bash

python manage.py makemigrations
python manage.py migrate
6. Run the Server
Bash

python manage.py runserver
Open your browser and navigate to: http://127.0.0.1:8000/

How It Works
Input: The user enters a URL (e.g., http://secure-login.update-info.com).

Tokenization: The system uses tokenizer.py to break the URL into keywords: ['secure', 'login', 'update', 'info', 'com'].

Vectorization: TF-IDF converts these words into numerical importance scores.

Prediction: The loaded Logistic Regression model calculates the probability of the URL being phishing.


Output: The result (Phishing/Legitimate) and confidence score are displayed to the user.

Dataset Information
The model was trained on a balanced dataset containing 11,430 records:

50% Phishing

50% Legitimate

Source: Kaggle Phishing URL Dataset