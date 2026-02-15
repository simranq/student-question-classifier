import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from preprocess import clean
import joblib

df = pd.read_csv("../data/S08_question_answer_pairs.txt", sep="\t")

df = df[[
    "Question",
    "DifficultyFromQuestioner"
]]

df.columns = ["question","difficulty"]
df = df.dropna(subset=["difficulty"])


df["clean_question"] = df["question"].apply(clean)

vectorizer = joblib.load("../models/vectorizer.pkl")
X = vectorizer.transform(df["clean_question"])

y = df["difficulty"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print(classification_report(y_test, pred))

joblib.dump(model,"../models/difficulty_model.pkl")
joblib.dump(vectorizer,"../models/vectorizer.pkl")
