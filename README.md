# Clinical Trial Analytics Dashboard

## Project Overview

This project is an end-to-end data analytics solution designed to simulate and analyze clinical trial data. It demonstrates how raw data can be transformed into meaningful insights using Python, PostgreSQL and Power BI.

The dashboard provides insights into enrollment trends, dropout patterns and site performance across multiple clinical trials.

---

## Tech Stack

* **Python** – Data generation and preprocessing
* **PostgreSQL** – Relational database design and querying
* **Power BI** – Interactive dashboard and visualization

---

## Project Structure

```
Clinical_Trial_Project/
│
├── data/               # Generated CSV datasets
├── scripts/            # Python scripts for data generation & insertion
├── sql/                # SQL scripts for schema and analysis
├── dashboard/          # Power BI dashboard file (.pbix)
├── requirements.txt    # Python dependencies
└── README.md
```

---

## Key Features

* Synthetic clinical trial dataset generation using Python
* Relational database design with PostgreSQL
* Automated data insertion pipeline
* Advanced SQL queries for analytics
* Interactive Power BI dashboard

---

## Dashboard Insights

The dashboard provides:

* **Enrollment Trend Analysis** (monthly trends across trials)
* **Dropout Analysis** (reasons and distribution by trial)
* **Site Performance** (top-performing sites based on enrollments)
* **Key KPIs:**

  * Total Enrollments
  * Total Dropouts
  * Dropout Rate
  * Enrollment Percentage
  * Adverse Events Count

---

## Dashboard Preview

(Add your screenshot here)

---

## How to Run the Project

### 1. Generate Data

```bash
python scripts/data_generation.py
```

### 2. Insert Data into PostgreSQL

```bash
python scripts/insert_data.py
```

### 3. Create Tables

Run:

```sql
sql/create_tables.sql
```

### 4. Open Dashboard

Open the `.pbix` file in Power BI Desktop:

```
dashboard/Clinical_Trial_Dashboard.pbix
```

---

## Key Learnings

* Data modeling and relational database design
* Writing advanced SQL queries (window functions, aggregations)
* Building interactive dashboards in Power BI
* Designing KPIs and business metrics
* End-to-end data pipeline development

---

## Future Improvements

* Add real-world dataset integration
* Implement automated ETL pipeline

---

## Author

**Mounika Teppola**
Master’s in Data Science
University of Maryland, College Park
