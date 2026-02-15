import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import clean

df = pd.read_csv("../data/S08_question_answer_pairs.txt", sep="\t")

df = df[[
    "Question",
    "ArticleTitle",
    "DifficultyFromQuestioner",
    "ArticleFile"
]]

df.columns = ["question","subject","difficulty","topic"]

df["clean_question"] = df["question"].apply(clean)

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))

X = vectorizer.fit_transform(df["clean_question"])

print("Shape of feature matrix:", X.shape)
print("Sample vector:")
print(X[0])
