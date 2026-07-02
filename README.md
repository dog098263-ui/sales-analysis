# 🛒 E-Commerce Logistics & Customer Churn Analytics

This project explores e-commerce transaction data to analyze customer purchasing behavior, identify operational inefficiencies (such as customer returns/cancellations), and track customer retention. The dataset was processed using **Power Query (M Code)**, modeled with a **Star Schema**, and visualized using **Power BI** dashboards.

---

## 📊 Project Overview

* **Domain:** E-Commerce / Retail
* **Data Size:** ~540,000+ rows of raw transaction data
* **Tools Used:**
  * Power Query (Data Cleaning & Transformation)
  * DAX (Time-intelligence & advanced measures)
  * Power BI (Visualization & Modeling)
* **Focus:** Gross vs. Net Revenue, Customer Churn, Return Rates, Product Performance, and Geographical Distribution

---

## 📊 Key Performance Metrics

* Gross vs. Net Revenue
* Return Rate (%)
* Customer Churn Rate (90-Day Inactivity)
* Average Customer Lifetime Value (LTV)
* Cancellation Financial Impact
* Active vs. Inactive Customers
* Revenue by Geography & Product Category

---

## 📊 Overall Performance Summary

| Metric              | Highest Segment | Lowest Segment |
| ------------------- | --------------- | -------------- |
| Net Revenue         | Premium Cohort  | Standard Cohort|
| Return Rate         | Apparel (12.4%) | Electronics (2.1%) |
| Churn Rate          | Q3 (18%)        | Q1 (5%)        |
| Customer Retention  | Europe (85%)    | Americas (45%) |

**Insight:** Premium customers account for 45% of net revenue with an average purchase frequency of 18 days. Returns are concentrated heavily in specific low-cost apparel items. Preserving null CustomerIDs as "Guest Checkout" preserved 25.2% of total transaction records.

**Dashboard:**

<img width="960" height="536" alt="Executive Summary Dashboard" src="PLACEHOLDER_IMAGE_URL_HERE" />

*(Note: Replace `PLACEHOLDER_IMAGE_URL_HERE` with the actual URL or relative path to your dashboard screenshot)*

---

## 📅 Category Insights & Recommendations

### 🔹 Product Returns & Cancellations

**Insights:**
* Cancellations are heavily skewed towards 3 specific product categories.
* High return rate (12.4%) in the Apparel segment compared to company average (2.1%).
* "Guest Checkouts" have a 15% higher cancellation rate than registered customers.

**Recommendations:**
1. Investigate sizing/quality issues for top 5 returned apparel items.
2. Implement stricter return policies for guest checkouts.
3. Enhance product descriptions for high-return items to set better customer expectations.

**Dashboard:**

<img width="960" height="538" alt="Product Analysis Dashboard" src="PLACEHOLDER_IMAGE_URL_HERE" />

### 🔹 Customer Churn & Cohorts

**Insights:**
* Customers with >90 days of inactivity rarely return (Churned).
* Peak churn occurs immediately after the Q4 holiday season.
* Premium-segment accounts have the lowest churn and highest LTV.

**Recommendations:**
1. Launch targeted re-engagement email campaigns at the 60-day inactivity mark.
2. Introduce a loyalty program to transition "Standard" cohort customers to "Premium".
3. Offer exclusive Q1 promotions to retain holiday shoppers.

**Dashboard:**

<img width="957" height="535" alt="Customer Churn Dashboard" src="PLACEHOLDER_IMAGE_URL_HERE" />

---

## 🚀 How to Run this Project

1. **Clone the Repository:** Copy this folder to your local machine.
2. **Open the Dataset:** The clean CSVs are saved in the `clean_data` folder.
3. **Launch Power BI:** Load the CSVs, configure the model relationships, and review the DAX measures.
