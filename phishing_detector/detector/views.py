from django.shortcuts import render
from .models import SearchHistory
import joblib
import os
from django.conf import settings

from tokenizer import make_tokens

model_path = os.path.join(settings.BASE_DIR, 'phishing_model.pkl')

try:
    model = joblib.load(model_path)
    print("Model loaded successfully!")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

def predict_phishing(url: str) -> dict:
    if not model:
        return {
            "result": "Error",
            "score": 0,
            "reasons": ["ML model not loaded"],
            "color": "gray"
        }
    prediction = model.predict([url])[0]
    probabilities = model.predict_proba([url])[0]

    confidence = round(max(probabilities) * 100, 2)

    if prediction == "phishing":
        return {
            "result": "Phishing",
            "score": confidence,
            "reasons": [
                "Suspicious URL patterns detected",
                f"Confidence: {confidence}%"
            ],
            "color": "red"
        }

    return {
        "result": "Legitimate",
        "score": confidence,
        "reasons": [
            "URL structure appears safe",
            f"Confidence: {confidence}%"
        ],
        "color": "green"
    }


def home(request):
    context = {}
    
    if request.method == 'POST':
        url_input = request.POST.get('url_input')
        
        prediction = predict_phishing(url_input)
        
        SearchHistory.objects.create(
            url=url_input,
            result=prediction['result'],
            confidence_score=prediction['score']
        )
        
        context = {
            'url': url_input,
            'prediction': prediction,
            'show_result': True
        }
        
    return render(request, 'index.html', context)