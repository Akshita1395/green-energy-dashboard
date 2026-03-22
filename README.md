# 🌍 Green Future Analytics Dashboard

An interactive data analytics dashboard that analyzes global renewable energy trends and carbon emissions, with predictive modeling for future emissions.

---

## 📌 Project Overview

This project focuses on understanding the relationship between renewable energy adoption and greenhouse gas emissions using real-world global datasets.

It includes:
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Interactive dashboard visualization
- Machine learning-based prediction

---

## 🚀 Features

- 📊 Interactive dashboard with country-level filtering
- 📈 CO₂ emissions and renewable energy trend analysis
- 🔗 Relationship visualization between renewable energy and emissions
- 💡 Data-driven insights (top renewable country, highest emissions)
- 🤖 Predictive model using Linear Regression

---

## 🛠️ Tech Stack

- Python
- Pandas
- Plotly
- Scikit-learn
- Streamlit

---

## 📂 Project Structure
energy-dashboard/
│
├── app.py
├── requirements.txt
├── data/
│ └── cleaned_energy.csv
│ └── energy_data.csv
└── notebook/
└── eda.ipynb

---

## 📊 Key Insights

- Iceland has the highest renewable energy adoption globally.
- China contributes the highest carbon emissions among countries.
- Renewable energy adoption has increased over time.
- Increasing renewable energy share may help reduce emissions.

---

## 🔮 Machine Learning

A Linear Regression model is used to predict carbon emissions based on:
- Renewable energy share
- Year

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Deployment

This project can be deployed using Streamlit Community Cloud.

## 📌 Future Improvements
Add more advanced ML models
Improve UI with dark mode
Add global comparison dashboards
