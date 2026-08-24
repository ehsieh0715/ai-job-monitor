# Dublin Bikes Journey Planner 🚲

Find optimal Dublin Bikes stations in real time or up to 5 days ahead.

![Role](https://img.shields.io/badge/Role-Full--Stack%20%7C%20Data-blue)
![Stack](https://img.shields.io/badge/Stack-Flask%20%7C%20MySQL%20%7C%20Google%20Maps%20API%20%7C%20Scikit--learn-orange)
![Status](https://img.shields.io/badge/Status-Completed%20%7C%20Deployment%20Paused-green)

![Demo](docs/demo.png)

A web-based system for real-time and predictive bike journey planning in Dublin, integrating live station data, weather information, and machine learning.

## 🔗 Original Project
This repository is a personal version of a collaborative university group project.

Original repository: [comp30830-group4](https://github.com/imyuanhui/comp30830-group4)

Shared with permission from the original contributors.

## 🚀 My Contribution

Role: Full-Stack Engineer (Data & System Design Focus)

- Led data pipeline and database setup, including API integration and schema design
- Built data ingestion and storage for real-time and historical bike & weather data
- Contributed to frontend development and improved UI/UX for map-based interaction and data visualization
- Designed system architecture and contributed to feature planning
- Managed sprint planning and project tracking in a 3-person team
- Authored the main project report and created architecture & sequence diagrams

## 📊 Key Results

- Developed a system for real-time and predictive bike availability using live and historical data
- Enabled journey planning up to 5 days ahead
- Integrated multiple external APIs (bike + weather + maps)
- Delivered an interactive map-based user interface with dynamic insights

## 🌟 Project Overview

This project is a full-stack web application that helps users plan bike journeys using Dublin Bikes.

It combines real-time station data, historical trends, and machine learning predictions to recommend optimal stations for both immediate and future trips.

Users can visualize station availability, explore trends, and make informed decisions based on weather and predicted demand.

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#️-technology-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#️-project-structure)
- [Additional Resources](#-additional-resources)
- [Contributors](#-contributors)
- [Notes](#-notes)

## ✨ Features

- **📍 Real-Time Station Map**  
  Interactive map showing all Dublin Bikes stations with live, color-coded bike and stand availability indicators

- **📊 Station Insights**  
  Station-level popups with current weather and 24-hour historical availability trends

- **🧭 Journey Planning (Real-Time)**  
  Suggests optimal start and destination stations based on proximity and live data

- **🔮 Future Journey Planning**  
  Plan journeys up to 5 days ahead using machine learning predictions and weather forecasts

## ⚙️ Technology Stack

- **Frontend:** HTML, CSS, JavaScript, Google Maps API  
- **Backend:** Flask (Python)  
- **Database:** MySQL  
- **APIs:** JCDecaux (Dublin Bikes), OpenWeather  
- **Machine Learning:** Scikit-learn (Linear Regression, Random Forest evaluation)

## 🚀 Getting Started

### Prerequisites
Make sure you have the following installed:

- Python 3.11
- Conda (recommended)


### Installation
Create and activate a virtual environment, then install dependencies:

```bash
conda create --name dublin_bikes python=3.11
conda activate dublin_bikes
pip install -r requirements.txt
```

### Configuration

Rename the environment file and add your API keys:
```bash
mv .env.example .env
```

Edit `.env`:

```ini
WEATHER_API_KEY=
DB_USER=root
DB_PASSWORD=
DB_PORT=3306
DB_URI=127.0.0.1
DB_NAME=bike
GOOGLE_MAPS_API_KEY=
BIKE_API_KEY=
BIKE_NAME=dublin
BIKE_STATIONS_URL=https://api.jcdecaux.com/vls/v1/stations
BASE_URL=
```

### Initialize Database
Run the script to populate initial bike and weather data:

```bash
cd backend/local_db_setup
python main.py
```

> Only required for the first-time setup

### Run

Start the backend server:

```bash
cd backend
python app.py
```

Then open: http://localhost:8000

## 🏗️ Project Structure
```bash
backend/        # Flask backend (APIs, services, ML)
  ├── routes/           # API endpoints (stations, journey, weather)
  ├── services/         # External API integration and prediction logic
  ├── machine_learning/ # Trained models and notebooks
  └── local_db_setup/   # Data collection and initialization scripts

frontend/       # Interactive map UI
docs/           # Architecture diagrams
report/         # Final report
```

## 📎 Additional Resources
- 📄 [Project Report](report/dublin_bikes_project_report.pdf)
- 📊 [Project Tracker](https://docs.google.com/spreadsheets/d/1LUCWdR2wFK8XpfDDjW2DP9k8h6U25k3L3Rhoy_vcmk0/edit?gid=1925064254#gid=1925064254)
- 🎥 [Demo Video](https://drive.google.com/file/d/1PkvOQU6m2fmazRwlxgVWh0_8SxZSFpqd/view?usp=drive_link)


## 👥 Contributors
- Wan-Hua Hsieh
- Yuanhui Xu
- Prakhar Dayal


## 📌 Notes

- Historical availability charts are based on stored demo/historical data used for visualization.
- Future journey suggestions rely on predictive estimates and may differ from real-time station availability.
