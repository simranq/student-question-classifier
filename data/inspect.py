import pandas as pd

df = pd.read_csv("S08_question_answer_pairs.txt", sep="\t")

print("\nCOLUMNS:")
print(df.columns)

print("\nFIRST 2 ROWS:")
print(df.head(2))

print(df.columns.tolist())

df = df[[
    "Question",
    "ArticleTitle",
    "DifficultyFromQuestioner",
    "ArticleFile"
]]

df.columns = ["question","subject","difficulty","topic"]

print(df.head())
