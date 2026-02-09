# 🧠 Intelligent Medical Diagnosis Assistant

A web-based **AI-powered medical diagnosis system** that predicts the risk or presence of multiple diseases using machine learning models, presented through a clean and user-friendly interface.

This project is designed to serve **both academic and real-world use cases**, demonstrating end-to-end integration of Machine Learning models with a Django web application.

---

## 🚀 Project Overview

The **Intelligent Medical Diagnosis Assistant** allows users to input relevant medical parameters and receive predictions for various diseases.  
Each disease module is powered by a trained machine learning model and integrated seamlessly into a Django backend.

The system focuses on:
- Early risk detection  
- Simple and intuitive user interaction  
- Modular and scalable design  

---

## 🩺 Supported Disease Modules

Currently implemented and working disease modules:

- ❤️ **Heart Disease**
- 🩸 **Diabetes**
- 🧪 **Kidney Disease**
- 🫁 **Lung Cancer**
- 🦋 **Thyroid Disorder**

---

## 🧠 Machine Learning Models

Each disease prediction uses a dedicated trained ML model:

| Disease        | Algorithm Used              |
|---------------|-----------------------------|
| Heart Disease | RandomForestClassifier      |
| Diabetes      | RandomForestClassifier (+ Scaler) |
| Kidney Disease| RandomForestClassifier      |
| Lung Cancer   | RandomForestClassifier      |
| Thyroid       | Logistic Regression         |

Models were trained offline and integrated using `joblib`.

---

## 🛠️ Tech Stack

### Backend
- **Python**
- **Django**
- **scikit-learn**
- **joblib**

### Frontend
- **HTML**
- **CSS**
- **JavaScript**

### Database
- **SQLite** (default Django database)

---

## ✨ Key Features

- Modular disease-wise prediction system  
- Secure form handling with CSRF protection  
- Clean UI with responsive design  
- Scalable architecture for adding future disease modules  
- Clear separation of frontend, backend, and ML logic  

---

## 🔐 Notes on Model Files (.pkl)

.pkl model files are excluded from GitHub using .gitignore

They must be placed manually in:

diagnosis/ml_models/


This is done to:

- Reduce repository size

- Avoid security risks

- Keep model ownership controlled

---

## 🌐 Deployment Status

🚧 Not deployed yet
Deployment is planned (Azure / Cloud platform) and will be updated soon.

---

## 👥 Contributors

- Navneet Nitin
Backend Development & Machine Learning Integration
🔗 https://github.com/navneet-nitin

- Ishit Singh
Frontend Development & UI Design
🔗 https://github.com/plagecy

ML integration and system design were collaboratively handled.

---

## 📌 Disclaimer

This project is intended for educational and demonstration purposes only.
It should not be used as a substitute for professional medical advice or diagnosis.

---

## ⭐ Acknowledgements

- Django Documentation

- scikit-learn Community

- Open-source datasets used for model training

Feel free to ⭐ the repository if you find this project useful!
