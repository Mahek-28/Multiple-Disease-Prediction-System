
# 🧠 Multiple Disease Prediction System

A machine learning-powered web app built with **Streamlit** to predict the likelihood of two common diseases:

- **Diabetes**
- **Heart Disease**

This application enables users to enter health parameters and receive instant predictions using trained machine learning models.

---

## 📂 Project Structure
Multiple-Disease-Prediction-System/
│
├── multiple_disease_pred.py # Main Streamlit app
├── diabetes_model.sav # Trained model for diabetes
├── heart_model.sav # Trained model for heart disease
├── requirements.txt # List of Python dependencies
└── README.md # Project overview


---

## 📦 Features

- Simple and interactive UI using **Streamlit**
- Sidebar navigation with `streamlit-option-menu`
- Real-time prediction based on user inputs
- ML models trained with **scikit-learn**
- Easy to extend and customize

---

## 🧪 Models Used

- `diabetes_model.sav`: Predicts diabetes from features like glucose level, BMI, age, pregnancies, etc.
- `heart_model.sav`: Predicts heart disease based on cholesterol, resting blood pressure, max heart rate, and more.

All models are saved using `pickle` and are trained on well-known public datasets.

---

## 🔧 Installation and Setup

### 1. Clone the Repository

```bash

git clone https://github.com/Mahek-28/Multiple-Disease-Prediction-System.git
cd Multiple-Disease-Prediction-System

### 2. Install Required Libraries
pip install -r requirement.txt

### 3. Run the Streamlit App
streamlit run multiple_disease_pred.py

## 🎥 Image of UI-Interface
<img width="1905" height="907" alt="diabetes prediction" src="https://github.com/user-attachments/assets/7118ff25-c908-4e45-ba47-56870f0729f0" />

<img width="1901" height="913" alt="Heart Disease Prediction" src="https://github.com/user-attachments/assets/2bffcd56-8227-42b1-b5c3-b4a383192f8d" />


