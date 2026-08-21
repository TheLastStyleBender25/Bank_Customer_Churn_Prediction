# Bank Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a bank customer is likely to churn.

The project covers the complete practical ML workflow — from data exploration and preprocessing to model selection, hyperparameter tuning, threshold optimization, and deployment as a FastAPI REST API.

## 🚀 Live API

**API:** https://bank-customer-churn-prediction-ej0c.onrender.com/

**Swagger Documentation:** https://bank-customer-churn-prediction-ej0c.onrender.com/docs

The API is deployed on Render and provides an interactive Swagger UI for testing predictions.

> Note: The free Render instance may take some time to respond after a period of inactivity because the service can spin down when idle.

---

## 🎯 Project Objective

Customer churn is an important problem for banks because retaining existing customers is generally more valuable than acquiring new ones.

The objective of this project is to build a classification model that predicts whether a customer is likely to leave the bank.

The target variable is:

- `0` → Customer stays
- `1` → Customer exits

---

## 🧠 Machine Learning Workflow

The project follows a practical ML workflow:

```text
Raw Dataset
     ↓
Exploratory Data Analysis
     ↓
Feature Selection
     ↓
Train / Test Split
     ↓
Numerical & Categorical Preprocessing
     ↓
Baseline Model
     ↓
Multiple ML Models
     ↓
Hyperparameter Tuning
     ↓
Model Evaluation
     ↓
Threshold Optimization
     ↓
Final Gradient Boosting Model
     ↓
Model Serialization
     ↓
FastAPI REST API
     ↓
Render Deployment
