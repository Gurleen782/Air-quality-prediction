# Machine Learning-Based Air Quality Prediction and Pollution Anomaly Analysis

A machine learning project that estimates PM2.5 concentration using environmental and meteorological parameters and identifies unusually high pollution levels through statistical anomaly detection.

## 🚀 Live Demo

[Open Air Quality Prediction App](https://air-quality-prediction-ml-project.streamlit.app/)

## 📌 Project Overview

Air pollution is a major environmental concern. Monitoring air quality and identifying unusually high pollution levels can help in understanding pollution patterns.

This project uses machine learning regression models to estimate PM2.5 concentration and the Interquartile Range (IQR) method to detect unusually high PM2.5 readings.

## ✨ Features

- PM2.5 concentration estimation.
- Comparison of four machine learning regression models.
- Pollution anomaly detection using the IQR method.
- Analysis of air quality patterns across monitoring stations and seasons.
- Interactive web application built with Streamlit.

## 📊 Dataset

**Beijing Multi-Site Air Quality Dataset (UCI)**

- 12 monitoring stations
- Original records: 420,768
- Records after preprocessing: 412,029
- Time period: March 2013 – February 2017

## 🛠️ Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Joblib

## 🤖 Machine Learning Models

Four regression algorithms were implemented and compared:

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 16.96 | 24.61 | 0.9129 |
| Polynomial Regression | 14.46 | 22.66 | 0.9261 |
| Decision Tree | 14.42 | 24.75 | 0.9119 |
| Random Forest | 12.37 | 20.15 | 0.9416 |

**Best Model: Random Forest Regression**

## 🔍 Anomaly Detection

The IQR method was used to identify unusually high PM2.5 readings.

- Detection threshold: 247.5 µg/m³
- Anomalies detected: 19,142
- Percentage of anomaly records: 4.65%

## 📂 Project Structure

```text
Air-quality-prediction/
│
├── Air_Quality_Prediction.ipynb
├── app.py
├── air_quality_model.pkl
├── anomaly_threshold.pkl
└── requirements.txt
```

## ⚠️ Limitations

- The model is trained on historical Beijing air quality data and has not been validated for Indian locations.
- PM2.5 estimation uses supplied environmental measurements; it does not forecast future pollution.

## 👩‍💻 Author

**Gurleen Kaur**
