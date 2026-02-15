import streamlit as st
import joblib
import sys
import os

sys.path.append("src")

from preprocess import clean
from topic_mapper import get_topic
from urgency_mapper import get_urgency

# Load models
subject_model = joblib.load("models/subject_model.pkl")
difficulty_model = joblib.load("models/difficulty_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

st.set_page_config(page_title="Student Question Classifier", page_icon="🎓")

st.title("🎓 Student Question Classifier")
st.write("Enter a question and the system will analyze it.")

question = st.text_area("Enter your question:")

if st.button("Analyze"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        cleaned = clean(question)
        vect = vectorizer.transform([cleaned])

        subject = subject_model.predict(vect)[0]
        difficulty = difficulty_model.predict(vect)[0]
        topic = get_topic(subject)
        urgency = get_urgency(question)

        st.success("Prediction Results")

        col1, col2 = st.columns(2)

        col1.metric("Subject", subject)
        col2.metric("Difficulty", difficulty)

        col1.metric("Topic", topic)
        col2.metric("Urgency", urgency)
