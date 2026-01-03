import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from tokenizer import make_tokens 

print("1. Loading dataset...")
try:
    data = pd.read_csv('phishing_data.csv')
    
    data.rename(columns={'url': 'url', 'status': 'label'}, inplace=True)
    
except FileNotFoundError:
    print("ERROR: 'dataset_phishing.csv' not found.")
    exit()

X = data['url']
y = data['label']

print("2. Building pipeline...")
pipeline = make_pipeline(
    TfidfVectorizer(tokenizer=make_tokens, token_pattern=None), 
    LogisticRegression(max_iter=1000) 
)

print(f"3. Training model on {len(data)} URLs...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline.fit(X_train, y_train)

score = pipeline.score(X_test, y_test)
print(f"4. Model trained! Accuracy: {score * 100:.2f}%")

joblib.dump(pipeline, 'phishing_model.pkl')
print("5. Model saved as 'phishing_model.pkl'")