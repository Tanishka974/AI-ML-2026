### 2. ML2_heartattack_pred.ipynb
**Logistic Regression Model for Heart Attack Prediction**

This project focuses on **binary classification** to predict the likelihood of a heart attack based on various medical indicators and patient health metrics.

#### Features Used:
- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Serum Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Resting Electrocardiographic Results (restecg)
- Maximum Heart Rate Achieved (thalach)
- Exercise Induced Angina (exang)
- ST Segment Depression (oldpeak)
- ST Segment Slope (slope)
- Number of Major Vessels (ca)
- Thalassemia Status (thal)

#### Project Workflow:
1. **Data Loading** - Loaded heart disease dataset with 303 records and 14 features
2. **Data Exploration** - Analyzed dataset structure and checked for missing values
3. **Train-Test Split** - Divided data into 80% training and 20% testing sets
4. **Model Training** - Trained a Logistic Regression model with 1000 max iterations
5. **Model Evaluation** - Evaluated performance using multiple classification metrics

#### Key Learnings:
- Understanding classification problems vs. regression problems
- How to work with binary classification and probability predictions
- Model evaluation metrics for classification (accuracy, precision, recall, F1-score)
- Confusion matrix interpretation for understanding true/false positives and negatives
- Importance of balanced evaluation metrics in healthcare predictions

#### Model Performance:
- Accuracy: 88.52%
- Precision: 87.88%
- Recall: 90.63%
- F1-Score: 89.23%

#### Technologies Used:
- Python
- Pandas (data manipulation)
- Scikit-learn (machine learning and metrics)
- Matplotlib/Seaborn (visualization)