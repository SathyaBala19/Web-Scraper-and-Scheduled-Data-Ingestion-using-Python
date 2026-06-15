# Web-Scraper-and-Scheduled-Data-Ingestion-using-Python

## Project Overview

This project demonstrates how to build a simple web scraping and scheduled data ingestion pipeline using Python.

The application extracts data from a website, processes the information, stores it in CSV format, and can be scheduled to run automatically using Cron (Linux/macOS) or Task Scheduler (Windows).

This project is designed for beginners who want to learn:

- Web Scraping
- Data Collection
- Data Ingestion
- Data Storage
- Automation
- Scheduling Jobs
- Python Project Structure

---

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- Pandas
- Cron / Task Scheduler

---

## Project Structure

```text
web-scraper-scheduled-ingestion/
│
├── scraper.py
├── data/
├── logs/
├── requirements.txt
└── README.md
```

---

## Features

* Fetch webpage content using Requests
* Parse HTML using BeautifulSoup
* Extract required information
* Store scraped data in CSV format
* Create logs for monitoring
* Automate execution through scheduling
* Beginner-friendly project structure

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/web-scraper-scheduled-ingestion.git
cd web-scraper-scheduled-ingestion

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Required Libraries

Install manually if needed:

```bash
pip install requests
pip install beautifulsoup4
pip install pandas
```

---

## Running the Project

Execute:

```bash
python scraper.py
```

The scraped data will be stored inside the data folder.

---

## Sample Workflow

1. Send request to target website
2. Download webpage content
3. Parse HTML structure
4. Extract required data
5. Clean and validate records
6. Save results to CSV
7. Generate execution logs
8. Schedule automated execution

---

## Learning Outcomes

By completing this project, you will understand:

* HTTP Requests
* HTML Parsing
* CSS Selectors
* Data Extraction
* CSV Data Storage
* Exception Handling
* Logging
* Automation Scheduling
* Basic Data Engineering Concepts

---

## Future Enhancements

* Store data in SQL Database
* Incremental Data Loading
* API Integration
* Email Notifications
* Airflow Scheduling
* Docker Containerization
* Cloud Deployment
* Data Visualization Dashboard

---

## Author

Sathya Bala B

B.Tech Artificial Intelligence and Data Science

Karpagam College of Engineering

Coimbatore, Tamil Nadu
