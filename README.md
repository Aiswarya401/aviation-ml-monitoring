Aviation ML Monitoring Dashboard

Overview

The Aviation ML Monitoring Dashboard is a machine learning-powered web application that classifies aviation-related documents and monitors model predictions in real time.

Built using FastAPI, Scikit-learn, Pandas, HTML, and CSS, the system not only predicts document categories but also logs prediction activity for monitoring and analysis.

---
Features

- Aviation document classification using Machine Learning
- FastAPI-based prediction endpoint
- Real-time prediction monitoring
- Prediction history tracking
- Total prediction counter
- User-friendly web dashboard
- CSV-based logging system

---
Categories Supported

The model can classify aviation-related text into categories such as:

- Engine
- Fuel
- Avionics
- Navigation
- Communication

---
Technologies Used

- Python
- FastAPI
- Scikit-learn
- Pandas
- HTML
- CSS
- Joblib

---
Project Structure

aviation-ml-monitoring/

├── app.py

├── train.py

├── dataset.csv

├── model.pkl

├── logs.csv

├── templates/

│ └── index.html

└── static/

└── style.css

---
How It Works

1. User enters aviation-related text.
2. The trained machine learning model predicts the category.
3. The prediction is displayed on the dashboard.
4. The input and prediction are stored in a log file.
5. Recent predictions and monitoring statistics are displayed.

---
Example

Input:

Aircraft engine overheating during takeoff

Prediction:

Engine

---
Monitoring Features

The dashboard tracks:

- Total predictions made
- Recent prediction history
- Prediction logs stored in CSV format

This helps monitor model usage and prediction activity over time.

---
Learning Outcomes

Through this project, I gained experience in:

- Natural Language Processing (NLP)
- Machine Learning model deployment
- FastAPI web development
- Prediction monitoring
- Data logging and analytics
- Frontend and backend integration

---
Future Improvements

- Cloud deployment
- Database integration
- User authentication
- Interactive analytics dashboard
- Model performance monitoring
- File upload support

---

Author

Aiswarya S

Electronics and Computer Engineering Student

Interested in Aviation Technology, Avionics, Artificial Intelligence, and Software Development.
