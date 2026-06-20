import pandas as pd
import string
import nltk
import gradio as gr

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def preprocess(text):
    stop_words = set(stopwords.words('english'))
    # Step 1: handle missing
    if not isinstance(text, str):
        return ""

    # Step 2: lowercase
    text = text.lower()

    # Step 3: remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Step 4 & 5: tokenize and remove stopwords
    tokens = text.split()
    tokens = [token for token in tokens if token not in stop_words]

    # Step 6: return joined string
    return " ".join(tokens)

def predict_sentiment(review):
    cleaned_review = preprocess(review)
    print(f"Cleaned Review: {cleaned_review}")  # Debugging statement
    # Load the saved model
    nb_model_path = r'models\naive_bayes_model.pkl'
    lr_model_path = r'models\logistic_regression_model.pkl'
    nb_model = joblib.load(nb_model_path)
    lr_model = joblib.load(lr_model_path)
    
    # Predict sentiment
    nb_prediction = nb_model.predict([cleaned_review])[0]
    nb_confidence = nb_model.predict_proba([cleaned_review]).max()  # Get the confidence score

    lr_prediction = lr_model.predict([cleaned_review])[0]
    lr_confidence = lr_model.predict_proba([cleaned_review]).max()  # Get the confidence score

    print(f"Naive Bayes Prediction: {nb_prediction}, Confidence: {nb_confidence}")  # Debugging statement
    print(f"Logistic Regression Prediction: {lr_prediction}, Confidence: {lr_confidence}")  # Debugging statement

    return nb_prediction, nb_confidence, lr_prediction, lr_confidence

ui = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=4, placeholder="Enter a product review here..."),
    outputs=[
        gr.Label(num_top_classes=1, label="Predicted Sentiment(Naive Bayes)"),
        gr.Textbox(label="Confidence Score(Naive Bayes)"),
        gr.Label(num_top_classes=1, label="Predicted Sentiment (Logistic Regression)"),
        gr.Textbox(label="Confidence Score (Logistic Regression)")
    ],
    title="Amazon Product Review Sentiment Analysis",
    description="Enter a product review to predict its sentiment (Positive or Negative) along with the confidence score."
)

ui.launch(share=True)