import joblib
from preprocess import clean
from topic_mapper import get_topic
from urgency_mapper import get_urgency

# load trained models
subject_model = joblib.load("../models/subject_model.pkl")
difficulty_model = joblib.load("../models/difficulty_model.pkl")

vectorizer = joblib.load("../models/vectorizer.pkl")

while True:
    q = input("\nEnter question: ")

    cleaned = clean(q)
    vect = vectorizer.transform([cleaned])

    subject = subject_model.predict(vect)[0]
    difficulty = difficulty_model.predict(vect)[0]
    topic = get_topic(subject)
    urgency = get_urgency(q)

    print("\nPrediction:")
    print("Subject:", subject)
    print("Topic:", topic)
    print("Difficulty:", difficulty)
    print("Urgency:", urgency)
