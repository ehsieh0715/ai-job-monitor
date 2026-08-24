# 🤖 AI vs Human Text Detection

NLP project for distinguishing AI-generated and human-written academic abstracts using sparse lexical features and embedding-based classifiers.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Task](https://img.shields.io/badge/Task-Text%20Classification-purple)
![Methods](https://img.shields.io/badge/Methods-Classical%20NLP%20%7C%20Embeddings-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

**Binary Classification | NLP | Supervised Learning**

## 🚀 Highlights

- Developed and evaluated two end-to-end text classification pipelines:
  - Sparse lexical models (CountVectorizer / TF-IDF)
  - Embedding-based models (Word2Vec / Sentence-BERT)

- Benchmarked linear, kernel, and ensemble classifiers

- Achieved **91.89% accuracy** and **97.57% ROC-AUC** with the best model

- Estimated AI-generated proportions in unseen corpora as a corpus-level detection task

- Found that sparse lexical features outperformed dense embeddings on this task

## 🌐 Quick Access

- 📓 [Part 1 – Classical Text Classification](notebooks/01_classical_text_classification.ipynb)  
- 📄 [Part 1 – HTML Report](notebooks/01_classical_text_classification.html)
- 📓 [Part 2 – Embedding and Ensemble Models](notebooks/02_embedding_and_ensemble_models.ipynb)  
- 📄 [Part 2 – HTML Report](notebooks/02_embedding_and_ensemble_models.html)


## 📌 Overview
This project investigates whether academic abstracts can be classified as AI-generated or human-written using supervised machine learning.

The work is organized into two parts:

- **Part 1:** Classical NLP feature extraction and machine learning baselines  
- **Part 2:** Embedding-based approaches and advanced classifier comparison

In addition to document-level classification, the project also estimates the proportion of AI-generated documents in two unseen text corpora.

## 📋 Table of Contents

- [Methodology Overview](#-methodology-overview)
- [Key Results](#-key-results)
- [Main Findings](#-main-findings)
- [Skills Demonstrated](#-skills-demonstrated)
- [Dataset](#-dataset)
- [Repository Structure](#-repository-structure)
- [Environment](#️-environment)
｀
## 🧠 Methodology Overview

### Part 1: Sparse Feature-Based Models

The first notebook evaluates sparse text representations and classical classifiers.

**Feature extraction**
- CountVectorizer  
- TfidfVectorizer

**Classifiers**
- MultinomialNB  
- ComplementNB  
- BernoulliNB  
- k-Nearest Neighbors  
- Decision Tree  
- Logistic Regression  
- SGDClassifier

A stratified three-way split was used:

- 50% training  
- 20% validation  
- 30% testing

Evaluation focuses on:

- Accuracy  
- ROC-AUC  
- AI precision, recall, and F1-score  
- Human precision, recall, and F1-score

This metric design is important because false positives and false negatives carry different risks in AI authorship detection.


### Part 2: Embedding-Based Models

The second notebook extends the baseline by evaluating dense text representations.

**Embeddings**
- Word2Vec  
- Sentence-BERT embeddings

**Downstream classifiers**
- Logistic Regression  
- RidgeClassifier  
- LinearSVC  
- SGDClassifier  
- HistGradientBoostingClassifier  
- XGBoost  
- LightGBM

A two-stage strategy was used for Word2Vec:

1. Embedding representation selection using Logistic Regression as a controlled baseline  
2. Downstream classifier benchmarking on the selected representation

For BERT-based experiments, an initial stratified sample was used for efficient model comparison, followed by retraining selected configurations on the full dataset.


## 📊 Key Results

### Classical NLP Pipeline (Best Model)

**CountVectorizer + LogisticRegression (saga)**

- Accuracy: **91.89%**  
- ROC-AUC: **97.57%**  
- AI F1-score: **93.53%**


### Embedding Pipeline (Best Model)

**Word2Vec + LinearSVC**

- Accuracy: **87.41%**  
- Macro F1: **86.54%**


### Corpus-Level Estimates

| Model | Test A | Test B |
|------|--------|--------|
| Classical model | 27.1% | 6.2% |
| Embedding model | 31.5% | 9.0% |

Both approaches consistently suggest **Test A contains more AI-generated content than Test B**.

These percentages should be interpreted as model-based estimates rather than ground truth.


## 🔍 Main Findings

1. Sparse lexical features outperformed dense embeddings, suggesting stylometric patterns were highly predictive.

2. Word2Vec outperformed the tested sentence-transformer embeddings on this task.

3. Both pipelines consistently estimated more AI-generated content in Test A than Test B, though these should be interpreted as directional model-based estimates.

## 🧠 Skills Demonstrated

- Natural Language Processing (NLP)
- Feature Engineering for Text Data
- Supervised Classification
- Model Evaluation & Benchmarking
- Embedding-Based Representation Learning
- Reproducible Experiment Design

## 📂 Dataset

Includes:

- Labeled training corpus of academic abstracts  
- Two unlabeled test corpora for corpus-level estimation

> Dataset was provided as part of academic coursework.

## 📁 Repository Structure

```text
ai-human-text-detection/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   ├── ai_human_text.csv
│   │   ├── test_Abst_A.csv
│   │   └── test_Abst_B.csv
│   └── interim/                  # model outputs and corpus-level estimates
│       ├── best_sample_results.csv
│       └── word2vec_500_best_results.csv
└── notebooks/
    ├── 01_classical_text_classification.ipynb
    ├── 01_classical_text_classification.html
    ├── 02_embedding_and_ensemble_models.ipynb
    └── 02_embedding_and_ensemble_models.html
```

## ⚙️ Environment

Main libraries used include:

- pandas  
- numpy  
- matplotlib  
- scikit-learn  
- gensim  
- xgboost  
- lightgbm  
- sentence-transformers

Install dependencies with:

```bash
pip install -r requirements.txt
```
