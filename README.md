# Netflix Subscriber Growth Strategy & Analytics Optimizer

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![SciPy](https://img.shields.io/badge/SciPy-Optimization-blue)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

An end-to-end **Business Analytics & Optimization** framework that combines **Machine Learning**, **Customer Segmentation**, and **Operations Research** to address slowing subscriber growth in streaming platforms.

The project automatically discovers high-value customer personas using **K-Means Clustering**, estimates customer behavior from engagement features, and optimizes strategic investment allocation using **Constrained Linear Programming** to maximize projected revenue while respecting investment constraints.

The framework models a strategic roadmap targeting:

- 📈 **+15% Subscriber Growth**
- 💰 **$4.8B Incremental Revenue**
- 📊 **3.2× Return on Investment**
- ⏳ **24-Month Implementation Horizon**

---

# Executive Summary

As streaming markets approach saturation, subscriber growth increasingly depends on **customer intelligence rather than pricing alone**.

This project simulates a consulting-style strategy by integrating data science and optimization into a single decision-support pipeline.

The framework recommends investments across three strategic initiatives:

- 🤖 AI Personalized Bundles
- 🌍 Regional Content Expansion
- 🎓 Student & Family Pricing

using behavioral subscriber analytics and mathematical optimization.

---

# Business Problem

The streaming industry is experiencing

- Slowing subscriber growth
- Rising churn
- Market saturation
- Increasing competitive pressure
- Price-sensitive emerging markets

Traditional pricing increases provide diminishing returns.

Instead, growth must come from:

- Better personalization
- Customer segmentation
- Regional expansion
- Intelligent budget allocation

---

# Solution Overview

The project builds an end-to-end analytics pipeline that

```
Subscriber Data
       │
       ▼
Feature Engineering
       │
       ▼
Behavior Standardization
       │
       ▼
K-Means Customer Segmentation
       │
       ▼
Persona Discovery
       │
       ▼
Revenue & Churn Analytics
       │
       ▼
Linear Programming Optimizer
       │
       ▼
Optimal Investment Allocation
       │
       ▼
Projected Revenue Growth
```

---

# Strategic Personas

The clustering engine automatically groups subscribers into four business personas.

| Persona | Characteristics |
|----------|----------------|
| Budget Student | High price sensitivity, moderate engagement |
| Family Household | Multiple users, shared subscriptions |
| Urban Professional | Premium users with low price sensitivity |
| Emerging Market Viewer | Strong preference for regional content |

Each persona receives a different strategic treatment during optimization.

---

# Dataset

The repository generates a realistic synthetic subscriber base including

- Monthly Watch Hours
- Session Frequency
- Device Count
- Subscription Tier
- Monthly ARPU
- Churn Probability
- Local Content Preference
- Genre Diversity
- Price Sensitivity
- Household Size
- Number of Profiles
- Country Category

The dataset is designed to mimic large-scale subscriber behavior while remaining fully reproducible.

---

# Machine Learning Pipeline

## Feature Engineering

- Missing value handling
- StandardScaler normalization
- Feature selection
- Behavioral feature encoding

---

## Customer Segmentation

Implemented using

- Scikit-Learn KMeans
- Elbow Method
- Silhouette Score
- Cluster Profiling

Outputs include

- Customer personas
- Cluster centers
- Persona distributions
- Behavioral summaries

---

# Optimization Model

After customer segmentation, a constrained optimization model determines how investment should be distributed across strategic initiatives.

Decision variables include

- AI personalization budget
- Regional content investment
- Student pricing investment

Objective

Maximize

\[
Revenue - Investment
\]

Subject to

- Total Budget ≤ \$1.5B
- Regional allocation constraints
- Technology spending limits
- Marketing limits
- Minimum initiative investment

Implemented using

- SciPy Linear Programming
- Constraint Matrix Formulation

---

# Key Results

| Metric | Value |
|---------|------|
| Current Subscribers | 238M |
| Target Subscribers | 274M |
| Subscriber Growth | +36M |
| Revenue Increase | $4.8B |
| Investment | $1.5B |
| ROI | 3.2× |
| Timeline | 24 Months |

---

# Visualizations

The project automatically generates

- Customer Persona Distribution
- Cluster Scatter Plot
- Elbow Curve
- Silhouette Analysis
- Budget Allocation
- Revenue Attribution
- ROI Projection
- Subscriber Growth Forecast

---

# Repository Structure

```
Netflix-Subscriber-Growth-Optimizer/

│
├── data/
│
├── notebooks/
│
├── src/
│   ├── preprocessing.py
│   ├── clustering.py
│   ├── optimization.py
│   ├── visualization.py
│   └── utils.py
│
├── outputs/
│
├── requirements.txt
│
├── main.py
│
└── README.md
```

---

# Tech Stack

### Programming

- Python

### Machine Learning

- Scikit-Learn
- NumPy
- Pandas

### Optimization

- SciPy
- Linear Programming

### Visualization

- Matplotlib
- Seaborn

---

# Installation

```bash
git clone https://github.com/AbhirajLucifer/Netflix-Subscriber-Growth-Optimizer.git

cd Netflix-Subscriber-Growth-Optimizer

pip install -r requirements.txt
```

---

# Usage

Run the complete analytics pipeline

```bash
python main.py
```

or explore each stage individually

```bash
jupyter notebook
```

---

# Future Work

- XGBoost Churn Prediction
- Customer Lifetime Value Estimation
- Reinforcement Learning Pricing Engine
- Streamlit Executive Dashboard
- Time-Series Subscriber Forecasting
- Multi-objective Optimization
- Monte Carlo Risk Simulation
- Recommendation System Integration

---

# Skills Demonstrated

- Business Analytics
- Strategy Consulting
- Market Segmentation
- Machine Learning
- Customer Analytics
- Financial Modeling
- Linear Programming
- Operations Research
- Data Visualization
- Optimization

---

# Author

**Abhiraj Singh**

IIT (ISM) Dhanbad

Machine Learning • Data Science • Business Analytics • Strategy Consulting
