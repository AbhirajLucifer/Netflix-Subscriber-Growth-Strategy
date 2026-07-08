# Netflix Subscriber Growth Strategy & Analytics Optimizer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end data science and mathematical optimization pipeline designed to counter slowing streaming subscriber growth. This framework ingests behavioral user metrics, segments users into high-impact strategic personas using **K-Means Clustering**, and applies a **Constrained Linear Programming** model to maximize Average Revenue Per User (ARPU) under explicit capital expenditure limits.

Inspired by subscription growth modeling frameworks targeted to achieve **+15% growth** and a **3.2x ROI** profile over a 24-month horizon.

---

## 📊 Business Context & Strategy
As core streaming markets near peak saturation, traditional pricing increases lose efficacy, leading to industry-wide churn inflation (e.g., reaching **3.8% quarterly churn**)[cite: 1]. To reverse this trend, this repository implements code tailored around three strategic growth levers[cite: 1]:

1. **AI Personalized Bundles:** ML-driven recommendation and feature packaging[cite: 1].
2. **Regional Content Expansion:** Capturing untapped emerging market cohorts[cite: 1].
3. **Student & Family Flexible Pricing:** Reducing churn in price-sensitive demographics[cite: 1].

### Targeted Strategic Personas
Our engine segments users into four distinct programmatic profiles to feed specialized onboarding and retention pipelines[cite: 1]:
* **Budget Student:** High price sensitivity, moderate streaming hours, single profile[cite: 1].
* **Family Household:** Multi-user shared profiles, high streaming volume, moderate local content[cite: 1].
* **Urban Professional:** Low price sensitivity, premium ad-free tiers, low local content[cite: 1].
* **Emerging Market Viewer:** Local-language content preference, high streaming hours[cite: 1].

---

## 🛠️ Architecture & Technical Core

The system is built as a self-contained pipeline partitioned into three sequential stages:

```text
[ Synthetic Subscriber Base ]
              │
              ▼
  ┌───────────────────────┐
  │ 1. Feature Scaler     │ ──► Standardizes variance across skewed behavioral fields
  └───────────┬───────────┘
              ▼
  ┌───────────────────────┐
  │ 2. K-Means Clustering │ ──► Automatically segments the user base into 4 Core Personas
  └───────────┬───────────┘
              ▼
  ┌───────────────────────┐
  │ 3. SciPy Optimization │ ──► Constrained LP algorithm maximizes total ARPU
  └───────────────────────┘
