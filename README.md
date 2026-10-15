# 📊 E-Commerce Sales Analysis

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?logo=microsoft-excel&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> End-to-end sales analytics project on 540,000+ e-commerce transactions — analyzing revenue, customer churn, return rates, and regional performance with Python and Excel.

---

## 📌 Project Overview

| Attribute | Details |
|-----------|---------|
| **Domain** | E-Commerce / Retail |
| **Dataset** | Online Retail (540,000+ rows) |
| **Tools** | Python, Pandas, Matplotlib, Seaborn, Excel |
| **Focus** | Revenue trends, Customer churn, Return analysis, Regional performance |

---

## 📈 Key Performance Metrics Analyzed

| Metric | Value |
|--------|-------|
| Gross vs. Net Revenue | Analyzed across all segments |
| Return Rate | 12.4% in Apparel vs. 2.1% company avg |
| Customer Churn Rate | 18% peak in Q3 (90-day inactivity model) |
| Avg Customer LTV | Calculated per cohort |
| Europe Retention | 85% (highest region) |
| Americas Retention | 45% (lowest region) |

---

## 🔍 Key Insights

- **Premium customers** account for **45% of net revenue** with avg purchase frequency of 18 days
- **Cancellations skewed** to just 3 product categories — targeted fix possible
- Preserving null CustomerIDs as "Guest Checkout" saved **25.2% of transaction records**
- Customers inactive for **>90 days** have a <5% chance of returning

---

## 📊 Analysis Modules

### 1. 🧹 Data Cleaning (`clean_data/`)
- Removed duplicates and invalid transactions
- Handled missing CustomerIDs as "Guest Checkout"
- Standardized date formats and currency fields

### 2. 📉 Revenue Analysis (`analyze_data.py`)
- Gross vs. Net Revenue by month, quarter, and year
- Revenue segmented by product category and geography
- YoY and MoM growth calculations

### 3. 👥 Customer Churn Analysis
- 90-day inactivity churn model
- Cohort analysis (Premium vs. Standard customers)
- Customer Lifetime Value (LTV) by segment

### 4. 📦 Return Rate Analysis
- Return rate by product category
- Guest vs. registered customer return comparison
- Financial impact of cancellations

---

## 📁 Project Structure

```
sales-analysis/
├── analyze_data.py             # Main analysis script
├── generate_data.py            # Data generation / augmentation
├── process_data.py             # Data processing pipeline
├── Online Retail.xlsx          # Source dataset (540K+ rows)
├── clean_data/                 # Cleaned output files
├── images/                     # Dashboard screenshots
└── README.md
```

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/dog098263-ui/sales-analysis.git
cd sales-analysis

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn openpyxl

# 3. Run analysis
python analyze_data.py
```

---

## 💡 Business Recommendations

1. **Reduce Apparel Returns** — Investigate sizing/quality issues for top 5 returned items
2. **Re-engagement campaigns** at 60-day inactivity mark (before churn point)
3. **Loyalty program** to upgrade Standard → Premium cohort customers
4. **Q1 promotions** to counteract post-holiday seasonal churn spike

---

## 👤 Author

**Aman Shakil** — [GitHub](https://github.com/dog098263-ui) · [Email](mailto:dog098263@gmail.com)

⭐ *Star this repo if you found it useful!*
