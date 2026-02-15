import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import clean

df = pd.read_csv("../data/S08_question_answer_pairs.txt", sep="\t")

df["clean_question"] = df["Question"].apply(clean)

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
vectorizer.fit(df["clean_question"])

joblib.dump(vectorizer, "../models/vectorizer.pkl")

print("Vectorizer trained and saved.")
