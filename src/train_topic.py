import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from preprocess import clean
from topic_mapper import get_topic

df = pd.read_csv("../data/S08_question_answer_pairs.txt", sep="\t")

df = df[[
    "Question",
    "ArticleTitle"
]]

df.columns = ["question","subject"]

df["topic"] = df["subject"].apply(get_topic)

df = df.drop_duplicates(subset=["question"])


df["clean_question"] = df["question"].apply(clean)

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
X = vectorizer.fit_transform(df["clean_question"])
y = df["topic"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print(classification_report(y_test, pred))
