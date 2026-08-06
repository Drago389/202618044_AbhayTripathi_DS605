### 📚 Books to Scrape: End-to-End Scraping & Data Pipeline

An automated data engineering pipeline that extracts book data from [Books to Scrape](https://books.toscrape.com/), cleans and preprocesses the raw outputs, performs Exploratory Data Analysis (EDA), and builds semantic visualisations. 

### 🚀 Project Overview

This repository contains a full four-stage data architecture pipeline built inside VS Code and tracked via Git. 

* **Task 1: Data Scraping** – A concurrent Scrapy spider that bypasses pagination to extract depth metrics.
* **Task 2: Data Preprocessing** – Data cleaning, feature engineering, and validation rules using Pandas.
* **Task 3: Visualisation & EDA** – 4-quadrant statistical distribution dashboards and description-based word clouds.
* **Task 4: Insights & Interpretation** – Structured analytical summary reports on marketplace anomalies.

### 📂 Repository Structure

text

├── spiders/
│   ├── __init__.py
│   └── books_spider.py          # Task 1: Scrapy Spider Engine
├── scrapy.cfg                   # Scrapy System Configuration Asset
├── raw_books.csv                # Raw Unstructured Spider Output (Target > 100 rows)
├── preprocess.py                # Task 2: Pandas Data Transformation Pipeline 
├── cleaned_books.csv            # Cleaned, Feature-Engineered Output Dataset
├── analyze_books.py             # Task 3: Matplotlib & Seaborn Visualisation Suite
├── books_structural_eda_dashboard.png   # 4-Quadrant Distribution Chart Matrix
├── descriptions_wordcloud.png   # Text-Engine Word Cloud Canvas
└── README.md                    # Main Portfolio Documentation Portal

Use code with caution.

### 🛠️ Step-by-Step Execution Guide

### 1. Installation and Setup

Clone this repository to your local computer workstation and install the verified technical library dependencies: 

bash

# Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Install required analytical tooling packages
pip install scrapy pandas numpy matplotlib seaborn wordcloud

Use code with caution.

### 2. Task 1: Extracting Raw Storefront Metadata

Execute the asynchronous Scrapy spider to crawl across 5 catalog depth tiers and extract detailed item pages: 

bash

scrapy crawl books_scraper -o raw_books.csv

Use code with caution.

### 3. Task 2: Transforming Fields & Feature Engineering

Run the preprocessing script to clean text, handle null fallbacks, convert values to numeric types, and create advanced features (value_score, recommended flags, price_band indices): 

bash

python preprocess.py

Use code with caution.

### 4. Task 3: Generating Visualizations & Statistical Summaries

Execute the analytical script to automatically output the visualization charts and print a diagnostic dataset profiling status report: 

bash

python analyze_books.py

Use code with caution.

### 📊 Core Analytical Highlights & Visual Previews

### 📈 Statistical Distribution Matrix (books_structural_eda_dashboard.png)

* **Price Flattening**: The store's pricing displays a completely uniform distribution flat layout bounded stringently between **£10.00 and £59.99** with a mean market anchor centering at **~£33.27** (σ ≈ ± £14.81).
* **Star Allocation Equality**: Review counts remain flat at exactly **0**, while rating frequencies display equal distribution spreads across all 1-to-5 tiers, pointing to a simulated environment.

### ☁️ Literary Theme Word Cloud (descriptions_wordcloud.png)

By scrubbing platform boilerplate noise words (like *book*, *novel*, *available*), the pipeline uncovers the dominant structural thematic keywords driving product descriptions: 

* 🏆 **Top Frequencies**: **"History"**, **"Life"**, **"World"**, **"Family"**, and **"Mystery"** emerge as the core semantic hooks across book descriptions.

### ⚠️ Pipeline Limitations & Data Constraints

1. **Synthetic Sandbox Constraints**: Because the source platform relies on a randomly generated dataset, real-world consumer patterns—such as a positive rating bias or supply-and-demand bulk pricing discounts—are not present.
2. **Static Stock Values**: Stock depth numbers are limited to a tight range between **1 and 22 available items**, which reflects a fixed placeholder loop rather than a responsive, changing inventory.
3. **No Written Reviews**: The lack of written customer reviews restricts the pipeline to using publisher descriptions for text mining, instead of using real customer feedback data.
