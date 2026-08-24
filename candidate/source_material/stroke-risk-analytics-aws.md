# 🩺 Stroke Risk Analytics on AWS

End-to-end AWS data pipeline + Grafana dashboard for stroke risk analysis with fully reproducible deployment.

![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20Glue%20%7C%20Athena%20%7C%20EC2-orange)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-F46800)
![Status](https://img.shields.io/badge/Status-Reproducible%20%7C%20Deployment%20Paused-blue)


## 📚 Table of Contents
- [Project Status](#-project-status)
- [Overview](#-overview)
- [Quick Demo Guide](#-quick-demo-guide)
- [Architecture](#️-architecture)
- [Key Features](#️-key-features)
- [Skills Demonstrated](#-skills-demonstrated)
- [Dashboard](#-dashboard)
- [My Contribution](#-my-contribution)
- [Repository Structure](#-repository-structure)
- [Documentation](#-documentation)


## 🟦 Project Status
The live deployment is currently paused to reduce hosting costs.

However, this repository provides:
- Full architecture documentation
- Step-by-step deployment guide
- Grafana dashboard export (JSON)
- Screenshots of all dashboard views

The system can be fully reproduced by following the deployment guide.

## 📌 Overview
This project builds a cloud-native data pipeline for analyzing stroke risk factors from healthcare data.

It demonstrates how raw healthcare data can be transformed into actionable insights through a scalable, serverless architecture.

The system integrates AWS services (S3, Glue, Athena) with Grafana to enable interactive exploration of stroke risk factors.

The analysis is based on the [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) from Kaggle (Fedesoriano), which contains demographic, lifestyle, and clinical features for stroke risk prediction.

## 🌐 Quick Demo Guide
To quickly explore this project (no setup required):

1. View dashboard screenshots → [screenshots](./screenshots)
2. Check the architecture diagram → see the Architecture section
3. Explore deployment steps → [deployment guide](./docs/deployment_guide.md)
4. Import the dashboard into Grafana → [grafana JSON](./dashboards/grafana_dashboard.json)


## 🏗️ Architecture
The system follows a cloud-based data pipeline architecture:

![Architecture](screenshots/aws_pipeline_architecture.png)

**Pipeline flow:**
- Raw data ingestion into S3 (`raw/`)
- ETL processing using AWS Glue
- Schema inference via Glue Crawler
- SQL-based querying using Amazon Athena
- Visualization via Grafana (hosted on EC2)

Designed with a modular and decoupled architecture, enabling independent scaling of storage, processing, and visualization layers.

## ⚙️ Key Features
- Scalable cloud data lake architecture (raw & curated zones)
- Automated ETL pipeline with AWS Glue
- Serverless querying using Amazon Athena
- Interactive and filterable Grafana dashboards
- Multi-dimensional stroke risk analysis

## 🧠 Skills Demonstrated
- Design of cloud-native data architectures on AWS
- Development of ETL pipelines and data transformation workflows
- Serverless data analytics using Athena
- Dashboard design for data-driven decision making
- Translating analytical results into interpretable and actionable insights

## 📊 Dashboard

![Dashboard](screenshots/dashboard.png)

The dashboard includes four analytical modules:

### (A) Dataset Overview & Summary Metrics
Provides a high-level summary of the dataset, including:
- Total record count  
- Average BMI and glucose level  
- Overall stroke rate  
- Demographic distributions (gender, residence, work type, smoking status, age)

![Section 1](screenshots/section_1.png)

### (B) Stroke vs. Non-Stroke Comparison
Side-by-side comparison between stroke and non-stroke populations:
- Demographics  
- Health conditions  
- Lifestyle characteristics  
- Distribution differences across groups  

![Section 2](screenshots/section_2.png)


### (C) Stroke Risk by Individual Factor
Examines how each variable independently affects stroke prevalence:
- Highlights high-risk subgroups  
- Enables quick identification of potential risk factors  

![Section 3](screenshots/section_3.png)

### (D) Interactive Stroke Risk Scenario Explorer
A multi-factor analysis tool with 10 configurable filters.
**Filters:** gender, age group, hypertension, heart disease, ever married, work type, residence type, smoking status, BMI category, glucose level group

Includes:
- **Overall Stroke Summary** — baseline metrics  
- **Scenario Outcome** — filtered results  
- **Age Distribution** — helps identify confounding effects  

Supports “what-if” analysis for combined risk factors.

![Section 4](screenshots/section_4.png)

## 🚀 My Contribution
Independently designed and implemented a production-style end-to-end cloud analytics pipeline:
- S3 data lake architecture (raw / curated layers)
- AWS Glue ETL pipeline and schema design
- Athena-based analytical queries
- Grafana dashboard design and deployment on EC2
- Exploratory analysis of stroke risk factors

## 📁 Repository Structure
```
├── dashboards/                 # exported Grafana dashboard (can be imported into Grafana)
│   └── grafana_dashboard.json
├── docs/                       # documentation and report materials
│   ├── deployment_guide.md     # step-by-step AWS setup instructions
│   ├── report.pdf              # full project report
│   └── images/                 # images used in documentation (e.g., deployment guide)
├── glue/                       # AWS Glue ETL script for data transformation
│   └── stroke_raw_to_curated.py
├── screenshots/                # dashboard visuals used in README
└── README.md                   # project overview and documentation entry point
```

## 📚 Documentation
- 📄 [Full report](docs/report.pdf)
- 🔁 [Deployment guide](docs/deployment_guide.md)
