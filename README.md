# 🚀 SpaceX Falcon 9 First Stage Landing Prediction
### IBM Applied Data Science Capstone Project
**Author:** Gautam825406 | **GitHub:** [github.com/Gautam825406](https://github.com/Gautam825406)

![SpaceX](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/SpaceX_logo_black.svg/1200px-SpaceX_logo_black.svg.png)

---

## 📋 Project Overview

SpaceX advertises Falcon 9 rocket launches at **$62 million** per launch, while other providers charge **$165 million or more**. The key reason for this cost saving is that SpaceX reuses the **first stage** of the rocket. By predicting whether the first stage will land successfully, we can estimate the cost of a launch — which is valuable for companies that want to bid against SpaceX.

This project uses **real SpaceX launch data** to build a machine learning classification model that predicts whether the Falcon 9 first stage will land successfully.

---

## 🎯 Objectives

- Collect and wrangle SpaceX launch data from multiple sources
- Perform exploratory data analysis (EDA) using visualizations and SQL
- Build interactive visual dashboards using Folium and Plotly Dash
- Train and evaluate multiple machine learning classification models
- Identify the best model for predicting landing success

---

## 📁 Project Structure

```
ds-capstone-spacex/
│
├── 📓 jupyter-labs-spacex-data-collection-api.ipynb
│       └── Data collection using SpaceX REST API
│
├── 📓 jupyter-labs-webscraping.ipynb
│       └── Data collection using BeautifulSoup web scraping
│
├── 📓 labs-jupyter-spacex-Data_wrangling-v2.ipynb
│       └── Data wrangling, cleaning, and training label creation
│
├── 📓 jupyter-labs-eda-dataviz-v2.ipynb
│       └── EDA with Matplotlib & Seaborn visualizations
│
├── 📓 jupyter-labs-eda-sql-coursera_sqllite.ipynb
│       └── EDA using SQL queries on SQLite database
│
├── 📓 lab_jupyter_launch_site_location.ipynb
│       └── Interactive maps using Folium
│
├── 🐍 spacex_dash_app.py
│       └── Interactive dashboard using Plotly Dash
│
├── 📓 SpaceX_Machine_Learning_Prediction_Part_5.ipynb
│       └── ML model training, GridSearchCV, evaluation
│
└── 📄 README.md
```

---

## 🗂️ Datasets Used

| Dataset | Source | Description |
|---------|--------|-------------|
| SpaceX Launches | SpaceX REST API v4 | Rocket launch records since 2010 |
| Wikipedia Scrape | Wikipedia — List of Falcon 9 launches | Historical launch table |
| dataset_part_1.csv | IBM Cloud Object Storage | Cleaned API data |
| dataset_part_2.csv | IBM Cloud Object Storage | Data with Class labels |
| dataset_part_3.csv | IBM Cloud Object Storage | One-hot encoded features |
| spacex_launch_geo.csv | IBM Cloud Object Storage | Launch data with coordinates |
| spacex_launch_dash.csv | IBM Cloud Object Storage | Dashboard dataset |
| Spacex.csv | IBM Cloud Object Storage | SQL analysis dataset |

---

## 🔬 Methodology

### 1. Data Collection
- **SpaceX REST API** — Called `/v4/launches`, `/v4/rockets`, `/v4/launchpads`, `/v4/payloads`, `/v4/cores` endpoints
- **Web Scraping** — Used `requests` + `BeautifulSoup4` to scrape the Wikipedia Falcon 9 launch history table

### 2. Data Wrangling
- Identified and handled missing values (`PayloadMass`: 5 nulls, `LandingPad`: 26 nulls)
- Filtered only Falcon 9 launches (removed Falcon 1)
- Created binary **Class** label: `1 = Successful landing`, `0 = Failed landing`
- Applied One-Hot Encoding on `Orbit`, `LaunchSite`, `LandingPad`, `Serial` → **83 total columns**

### 3. Exploratory Data Analysis
- Flight number vs launch site scatter plots
- Payload mass vs orbit type analysis
- Success rate by orbit type bar charts
- Launch success yearly trend line chart
- **10 SQL queries** covering: unique sites, payload stats, success rates, rankings

### 4. Interactive Visual Analytics
- **Folium Maps**: Site markers, color-coded success/failure clusters, proximity lines to coastline/highway/city
- **Plotly Dash Dashboard**: Pie chart by site, payload scatter plot, dropdown + slider filters

### 5. Machine Learning
- Features standardized using `StandardScaler`
- 80/20 train-test split (`random_state=2`)
- **GridSearchCV** with 10-fold cross-validation for all models

---

## 🤖 Machine Learning Models

| Model | Test Accuracy | CV Score | Best Parameters |
|-------|:---:|:---:|---|
| Logistic Regression | 83.3% | 84.6% | C=0.01, penalty=l2 |
| Support Vector Machine | 83.3% | 84.8% | kernel=rbf, C=1.0 |
| **Decision Tree** ✅ | **83.3%** | **87.5%** | criterion=gini, max_depth=8 |
| K-Nearest Neighbors | 83.3% | 84.6% | n_neighbors=7 |

> ✅ **Best Model: Decision Tree** — Highest cross-validation score (87.5%) and most interpretable model.

---

## 📊 Key Findings

| Finding | Detail |
|---------|--------|
| 📈 Success Rate Growth | Improved from 0% (2010) to ~100% (2020) |
| 📍 Best Launch Site | KSC LC-39A — highest success rate (~82%) |
| 🌍 Best Orbit | GEO, HEO, SSO — 100% success rate |
| ⚠️ Hardest Orbit | GTO — only ~52% success rate |
| 🏋️ Payload Impact | Heavier payloads slightly reduce landing success |
| 🚫 VAFB SLC-4E | No launches with payload > 10,000 kg |
| 💰 Cost Saving | Successful recovery saves ~$103M per launch |

---

## ⚙️ Installation & Setup

### Prerequisites
```bash
Python 3.8+
Jupyter Notebook or JupyterLab
```

### Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn \
            requests beautifulsoup4 folium dash plotly \
            ipython-sql sqlalchemy
```

### Clone the Repository
```bash
git clone https://github.com/Gautam825406/ds-capstone-spacex.git
cd ds-capstone-spacex
```

### Run Notebooks
Open Jupyter and run each notebook in order (1 → 8):
```bash
jupyter notebook
```

### Run the Dash Dashboard
```bash
python spacex_dash_app.py
# Open browser: http://127.0.0.1:8050
```

---

## 🖥️ Dashboard Features

The Plotly Dash app (`spacex_dash_app.py`) includes:

- **Site Dropdown** — Filter by launch site or view all sites
- **Pie Chart** — Success counts per site (or success vs failure for selected site)
- **Payload Slider** — Filter launches by payload mass range (0 – 10,000 kg)
- **Scatter Plot** — Payload Mass vs Outcome, colored by Booster Version

---

## 🗺️ Folium Map Features

The Folium notebook (`lab_jupyter_launch_site_location.ipynb`) includes:

- 📌 Circle markers for all 4 launch sites
- 🟢🔴 Color-coded success/failure markers with popup info
- 🔗 Proximity lines: site → coastline, highway, railway, nearest city
- 📦 Marker clusters for zoomed-out view

---

## 📈 Results Summary

```
╔══════════════════════════════════════════════╗
║         FINAL MODEL RESULTS                  ║
║  All 4 models achieved 83.3% test accuracy   ║
║  Best CV Score: Decision Tree (87.5%)        ║
║  Recommended: Decision Tree Classifier       ║
╚══════════════════════════════════════════════╝
```

---

## 🏆 Course Information

| | |
|---|---|
| **Course** | IBM Applied Data Science Capstone |
| **Platform** | Coursera |
| **Certificate** | IBM Data Science Professional Certificate |
| **Author** | Gautam825406 |
| **GitHub** | github.com/Gautam825406/ds-capstone-spacex |

---

## 📜 License

This project is created for educational purposes as part of the IBM Data Science Professional Certificate on Coursera.

Data sourced from SpaceX API and Wikipedia. Course materials © IBM Corporation.

---

## 🙏 Acknowledgements

- **IBM Skills Network** for the course structure and datasets
- **SpaceX** for the public launch API
- **Coursera** for the learning platform
- Instructors: Joseph Santarcangelo, Nayef Abou Tayoun

---

*⭐ If you found this project useful, please give it a star on GitHub!*
