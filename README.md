## Amazon Review Classification App

#### Project Overview: 
This project develops a machine learning model to predict the review sentiment based on previous review sentiment.

#### The project includes:
1. Exploratory Data Analysis (EDA)
2. Feature selection
3. Model training and evaluation
4. Hyperparameter experimentation
5. Model comparison
6. Deployment using Gradio


## Dataset

#### Dataset Features

| Feature | Description |
|----------|-------------|
| **reviewText** | Review written by customer |
| **Positive** | Sentiment of the review |

## Dataset Summary:
- Total Records: 20,000
- Missing Values: None
- Positive Review    15,233
- Negative Review     4,767

## Exploratory Data Analysis (EDA)
#### Key Findings
Top Positive Features:
       Feature  Coefficient
11225     love     8.695423
8443     great     8.376000
6092      easy     5.328070
7800       fun     4.734022
2122   awesome     4.704640
2518      best     4.639550
20737    works     4.385290
12445     nice     3.233517
1327   amazing     2.969659
3272       can     2.928717

Top Negative Features:
           Feature  Coefficient
12603          not    -7.240488
20239        waste    -5.482707
5126       deleted    -4.700820
19536  uninstalled    -4.395276
17799        sucks    -4.132285
2823        boring    -4.032898
17702       stupid    -3.963142
19778      useless    -3.671020
5742          dont    -3.584042
20776        worst    -3.561058

## Model Comparison

Naive Bayes Accuracy: 0.8333

Classification Report of Naive Bayes:
              precision    recall  f1-score   support

    Negative       0.93      0.33      0.48       958
    Positive       0.82      0.99      0.90      3042

    accuracy                           0.83      4000
   macro avg       0.88      0.66      0.69      4000
weighted avg       0.85      0.83      0.80      4000

Logistic Regression Accuracy: 0.8918

Classification Report of Logistic Regression:
              precision    recall  f1-score   support

    Negative       0.86      0.65      0.74       958
    Positive       0.90      0.97      0.93      3042

    accuracy                           0.89      4000
   macro avg       0.88      0.81      0.84      4000
weighted avg       0.89      0.89      0.89      4000


## 🏆 Best Model
After evaluating two machine learning algorithms, **Logistic Regression** was selected as the best-performing model.<br>


## Project Structure

```text
House-Price-Prediction/
│
├── data/
│   └── amazon.csv
│
├── notebooks/
│   ├── 1_eda.ipynb
│   └── 2_training.ipynb
│
├── models/
│   └── naive_bayes_model.pkl
    └── logistic_regression_model.pkl
│
├── screenshots/
│   └── gradio_interface.png
│
├── app.py
├── requirements.txt
└── README.md
```


## Gradio Web Application

The project includes a Gradio interface where users can:<br>

- Enter a review
- Classify the sentiment of that review with confidence score

#### Input Features
- Review Text

#### Output
- Predicted Sentiment
- Confidence Score

## 📸 Screenshots

#### Gradio Interface

![Gradio Interface](screenshots/gradio_interface.png)


## Installation

#### Clone the repository:
git clone https://github.com/rotoncsedu/amazon-review-sentiment-analysis <br>
cd amazon-review-sentiment-analysis

#### Install dependencies:

pip install -r requirements.txt

## Run the Application

python app.py<br>

Or launch the Gradio interface:<br>

interface.launch(share=True)

## Technologies Used
- Python
- Pandas , NumPy , Matplotlib , Seaborn
- nltk
- Scikit - learn
- Gradio

## 👨‍💻 Author

Md. Al-Imran Roton

Programmer, Begum Rokeya University, Rangpur

Machine Learning & AI Enthusiast