# 🎓 Student Question Classifier AI

An intelligent Natural Language Processing system that analyzes student questions and automatically predicts:

✔ Subject  
✔ Topic  
✔ Difficulty Level  
✔ Urgency  

> Built using Machine Learning, NLP pipelines, and modular AI system design.

---

## 🌍 Problem Statement

Students often submit questions without specifying context, urgency, or difficulty level. This creates inefficiencies in academic support systems.

This project solves that by automatically analyzing questions and routing them intelligently so they can be:

- assigned to the right tutor
- prioritized based on urgency
- answered with appropriate complexity

This simulates how real ed-tech AI systems operate at scale.

---

## 🚀 Features

- Intelligent NLP preprocessing pipeline
- Multi-model prediction system
- Rule-based urgency detection
- Topic inference engine
- Real-time prediction interface (Streamlit)
- Modular architecture for scalability

---

## 🏗 System Architecture

```
User Question
      ↓
Preprocessing
      ↓
Vectorization (TF-IDF)
      ↓
ML Models
 ├── Subject Classifier
 └── Difficulty Classifier
      ↓
Logic Engines
 ├── Topic Mapper
 └── Urgency Detector
      ↓
Final Prediction Output
```

---

## 🧠 Models Used

| Task | Model |
|-----|------|
Subject Classification | Logistic Regression |
Difficulty Classification | Logistic Regression |
Vectorization | TF-IDF |
Urgency Detection | Rule-Based NLP |
Topic Detection | Rule Mapping |

---

## 🧹 Data Processing Steps

- Loaded dataset
- Parsed TSV format
- Selected relevant columns
- Removed null labels
- Removed duplicate questions
- Cleaned text (lowercase, punctuation removal, stopwords removal)

---

## 📊 Performance

**Difficulty Model Accuracy:** ~88%  
**Subject Model Accuracy:** ~61% *(after duplicate removal — realistic performance)*  
**Topic Model Accuracy:** ~79%

---

## ⚠️ Limitations

Due to limited dataset size and large number of subject classes, subject prediction accuracy is constrained. Increasing dataset size would significantly improve performance and generalization.

**Environment:** Python 3.10+

---

## 🔮 Future Improvements

- Transformer models (BERT)
- Larger dataset
- Context-aware difficulty prediction
- Tutor recommendation system
- API deployment
- Confidence score output

---

## ▶️ How To Run

Install dependencies:

```
pip install -r requirements.txt
```

Train models:

```
python src/train_vectorizer.py
python src/train.py
python src/train_subject.py
```

Run interface:

```
streamlit run app.py
```

---

## 📥 Dataset

Dataset is not included due to size limitations.

Download here:  
https://www.kaggle.com/datasets/rtatman/questionanswer-dataset

After downloading:

```
1. Extract ZIP
2. Move file into → data/
3. Rename file → S08_question_answer_pairs.txt
```

---

## 📁 Project Structure

```
project/
│
├── models/
├── data/
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── train_subject.py
│   ├── topic_mapper.py
│   ├── urgency_mapper.py
│   └── predict.py
│
└── app.py
```

---

## 🏁 Final Outcome

This project demonstrates the complete lifecycle of a real NLP system:

- data handling
- preprocessing
- feature engineering
- modeling
- evaluation
- deployment interface

**This is not just a model — it is a complete AI system.**

---

## 👩‍💻 Author

**Simran Qureshi**  
Computer Science Student | Aspiring AI Engineer
