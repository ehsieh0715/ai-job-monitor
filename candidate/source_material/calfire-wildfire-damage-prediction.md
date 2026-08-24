# 🔥 California Wildfire Damage Prediction

End-to-end machine learning pipeline for predicting wildfire-induced structural damage using real-world data, with a focus on data quality, feature engineering, and model interpretability.

**Binary Classification | Tabular Data | Imbalanced Dataset**

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-EDA-orange)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-yellow)
![Model](https://img.shields.io/badge/Model-Random%20Forest-brightgreen)
![Task](https://img.shields.io/badge/Task-Binary%20Classification-purple)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 🚀 Highlights
- Built an end-to-end machine learning pipeline for wildfire damage prediction
- Developed a data quality and feature engineering workflow for noisy real-world data
- Reduced features from **151 → 45** while maintaining model performance
- Achieved **F1 ≈ 0.891** with an interpretable Random Forest model
- Combined EDA and modeling insights for risk factor analysis

## 🌐 Quick Access
Key project outputs:
- 📄 [Data Quality Report (EDA Summary)](reports/Data%20Quality%20Report.pdf)
- 🧹 [Data Quality Plan (Cleaning Strategy)](reports/Data%20Quality%20Plan.pdf)
- 📊 [View Data Preparation & EDA](notebooks/01_data_preparation.html)
- 🤖 [View Modeling Results](notebooks/02_modeling_and_evaluation.html)

## 📌 Overview
This project analyzes wildfire damage data from the California Department of Forestry and Fire Protection (CAL FIRE) and builds a structured pipeline to predict structure damage severity under wildfire conditions.

The task is formulated as a binary classification problem, identifying whether a structure is "Destroyed (>50%)".

This project demonstrates how data quality, exploratory analysis, and machine learning can be combined into a structured analytics workflow for real-world decision support.


## 📚 Table of Contents
- [Key Features](#️-key-features)
- [Key Results](#-key-results)
- [Data Quality & EDA Outputs](#-data-quality--eda-outputs)
- [Modeling Results](#-modeling-results)
- [Skills Demonstrated](#-skills-demonstrated)
- [Repository Structure](#-repository-structure)
- [How to Run](#️-how-to-run)
- [Future Work](#-future-work)

## ⚙️ Key Features
- End-to-end ML pipeline (data → features → model → evaluation)
- Data quality pipeline for handling real-world dataset issues
- EDA-driven feature engineering and selection
- Model optimization with feature reduction (~70%)
- Interpretable modeling using Random Forest

## 📊 Key Results
- Final model: **Random Forest (F1 ≈ 0.891)**
- Reduced features from **151 → 45 (~70% reduction)**
- Maintained performance with improved interpretability
- Identified key risk factors through EDA and feature analysis

## 📄 Data Quality & EDA Outputs

This project includes detailed data quality analysis and cleaning strategies:

-  [Data Quality Report](reports/Data%20Quality%20Report.pdf): identifies key issues such as missing values, high cardinality, inconsistent formatting, and long-tail distributions  
-  [Data Quality Plan](reports/Data%20Quality%20Plan.pdf): documents feature-level decisions for cleaning, imputation, and transformation  

These reports capture the reasoning behind data preprocessing and feature engineering decisions, ensuring transparency and reproducibility.

### EDA Insights

EDA and modeling reveal that:
- Mobile homes show significantly higher destruction rates
- Structural and material features interact with environmental factors
- Temporal features contribute strongly due to interaction effects

This highlights the importance of combining statistical analysis with model-based interpretation.


## 🤖 Modeling Results

### Model Comparison (Test Set)

| Model               | Accuracy | Precision | Recall | F1-score | AUC |
|---------------------|----------|-----------|--------|----------|-----|
| Baseline (Always 1) | 0.579    | 0.579     | 1.000  | 0.733    | —   |
| Linear Regression   | 0.819    | 0.855     | 0.826  | 0.840    | —   |
| Logistic Regression | 0.822    | 0.894     | 0.785  | 0.836    | 0.91|
| Random Forest       | 0.836    | 0.861     | 0.853  | 0.857    | 0.92|

All results are evaluated on a held-out test set, where Random Forest achieves the best balance across precision, recall, and F1-score and is selected for further optimization.

### Final Model & Optimization

We further optimized Random Forest through feature selection:

- Full model: **151 features → F1 ≈ 0.893**
- Reduced model: **45 features → F1 ≈ 0.891**

The final model is **Random Forest (v4-2, 45 features)**:
- Reduces feature count by ~70%
- Maintains nearly identical performance
- Improves efficiency and interpretability

This demonstrates that feature selection enables significant model simplification without sacrificing predictive performance, making the model more suitable for real-world deployment.

### EDA vs Model Insights

EDA captures individual feature effects, while the model captures interactions, highlighting complementary perspectives in understanding wildfire damage risk.

## 🧠 Skills Demonstrated
- Data Cleaning & Validation
- Exploratory Data Analysis (EDA)
- Feature Engineering & Selection
- Machine Learning (Classification Models)
- Reproducibility & Pipeline Design

## 📁 Repository Structure 
The project follows a standard data science workflow:

```
calfire-wildfire-damage-prediction/
│
├── data/
│   ├── raw/                  # Original datasets
│   │   ├── cal-wildfires-23224143.csv
│   │   └── CAL FIRE Administrative Units.csv
│   │
│   ├── interim/              # Intermediate data
│   │   └── fixed_address.csv
│   │
│   └── processed/            # Cleaned datasets
│       ├── cal_wildfires_cleaned.csv
│       ├── cal_wildfires_standardized.csv
│       └── cal_wildfire_final_features.csv
│
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 01_data_preparation.html        # Full data quality analysis
│   ├── 02_modeling_and_evaluation.ipynb
│   └── 02_modeling_and_evaluation.html # Full modeling & evaluation
│
├── reports/
│   ├── Data Quality Report.pdf         
│   └── Data Quality Plan.pdf           
│
├── requirements.txt                   # Python dependencies
├── .gitignore
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/ehsieh0715/calfire-wildfire-damage-prediction.git
cd calfire-wildfire-damage-prediction
```
### 2. Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run analysis

You can explore the project in two ways:
- Open HTML notebooks (recommended for viewing results):
    - notebooks/01_data_preparation.html
	- notebooks/02_modeling_and_evaluation.html
- Or run Jupyter notebooks:
```bash
jupyter lab
```

## 🔮 Future Work
- Explore advanced models (XGBoost, LightGBM)
- Improve spatial features (GIS-based analysis)
- Handle class imbalance with more advanced techniques
