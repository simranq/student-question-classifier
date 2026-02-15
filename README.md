# 🎓 Student Question Classifier AI

An intelligent NLP system that analyzes student questions and automatically predicts:

✔ Subject  
✔ Topic  
✔ Difficulty Level  
✔ Urgency  

Built using Machine Learning + NLP pipeline engineering.

---

## 🚀 Project Overview

Students often ask questions without specifying context, urgency, or difficulty. This system automatically classifies incoming questions so they can be:

- routed to the correct tutor
- prioritized by urgency
- answered with appropriate complexity

This simulates real-world AI routing systems used in ed-tech platforms.

---

## 🧠 Core Features

✨ Text preprocessing pipeline  
✨ Multi-model prediction system  
✨ Rule-based urgency detection  
✨ Topic inference engine  
✨ Real-time prediction UI (Streamlit)  
✨ Modular ML architecture  

---

## 🏗 System Architecture
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


---

## 📊 Models Used

| Task | Model |
|-----|------|
Subject Classification | Logistic Regression |
Difficulty Classification | Logistic Regression |
Vectorization | TF-IDF |
Urgency Detection | Rule-based NLP |
Topic Detection | Mapping Engine |

---

## 🧹 Data Processing Steps

✔ Loaded dataset  
✔ Parsed TSV format  
✔ Selected relevant columns  
✔ Removed null labels  
✔ Removed duplicate questions  
✔ Cleaned text (lowercase, punctuation removal, stopwords removal)  

---

## 📈 Performance

### Difficulty Model
Accuracy ≈ **88%**

### Subject Model
Accuracy ≈ **61%**  
(After duplicate removal — realistic performance)

### Topic Model
Accuracy ≈ **79%**

---

## ⚠️ Limitations

Due to limited dataset size and large number of subject classes, subject prediction accuracy is constrained. Increasing dataset size would significantly improve performance and generalization.

---

## 🔮 Future Improvements

- Transformer models (BERT)
- Larger dataset
- Context-aware difficulty prediction
- Tutor recommendation engine
- Deployment API

---

## ▶️ How To Run

Install dependencies:


pip install -r requirements.txt


Train models:


python src/train_vectorizer.py
python src/train.py
python src/train_subject.py


Run UI:


streamlit run app.py


---

## 📁 Project Structure



project/
│
├── models/
├── data/
├── src/
│ ├── preprocess.py
│ ├── train.py
│ ├── train_subject.py
│ ├── topic_mapper.py
│ ├── urgency_mapper.py
│ └── predict.py
│
└── app.py


---

## 🏁 Final Outcome

This project demonstrates a complete real-world NLP pipeline including:

- data handling
- preprocessing
- feature engineering
- modeling
- evaluation
- deployment interface

It is not just a model — it is a full AI system.

---

## 👩‍💻 Author

**Simran Qureshi**  
Computer Science Student | Aspiring AI Engineer

