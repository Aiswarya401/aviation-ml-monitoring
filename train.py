
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


data = pd.read_csv("dataset.csv")


X = data["text"]
y = data["label"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])


model.fit(X_train, y_train)


predictions = model.predict(X_test)


accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy:.2f}")


joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")


sample = ["Aircraft engine showing abnormal vibration"]
result = model.predict(sample)

print("Prediction:", result[0])