## Log File Analyzer Tool for IT Operations

# #Overview
The Log File Analyzer Tool is a Python-based Flask web application designed to analyze large-scale server log files used in IT Operations.
It processes log files efficiently, handles corrupted entries safely, identifies HTTP error trends, detects top IP addresses generating errors, and visualizes insights through charts.

This project demonstrates real-world log analysis automation using Python and Flask.

 ## Features

 Upload .log or .txt server log files

 Efficient processing for large log files

 Graceful handling of corrupted/invalid log entries

 HTTP error code frequency analysis (4xx, 5xx)

 Top 5 IP addresses generating the highest errors

 Visualizations using Matplotlib

 Option to analyze multiple files without restarting the app

 Clean, professional, full-page UI
 
 ## Tech Stack

 Backend: Python, Flask

 Frontend: HTML, CSS

 Data Processing: Pandas, Regular Expressions

 Visualization: Matplotlib

## Project Structure

 log_file_analyzer/
 │
 ├── app.py                  
 ├── analyzer_utils.py       
 ├── requirements.txt        
 │
 ├── templates/
 │   ├── index.html         
 │   └── report.html         
 │
 ├── static/
 │   ├── error_chart.png     
 │   └── ip_error_chart.png  
 │
 ├── uploads/               
 └── tests/
    └── test_cases.py

 ## Log File Format

 The application expects log entries in the following format:

 Timestamp IP_Address Request_Method Status_Code

 ## Example:
 2026-01-21 10:01:15 192.168.1.10 GET 404

 2026-01-21 10:02:20 192.168.1.25 POST 500

 ## Install Dependencies

 pip install -r requirements.txt

 pip install flask pandas matplotlib

 ## Run the Application

 python app.py

 ## Open in Browser
 http://127.0.0.1:5000/

 ## Run Test Cases

 python -m unittest tests/test_cases.py

 ## Output

 ## Summary Cards

 Total Requests

 Total Errors

 Corrupted Lines

 Tables

 Error Code Frequency

 Top 5 IP Addresses

 Graphs

 HTTP Error Code Distribution

 IP Address Error Distribution

 ## Learning Outcomes

This project demonstrates:

Efficient parsing of large files in Python

Regex-based real-world data validation

Data aggregation using Pandas

Visual analytics using Matplotlib

Flask-based web application development

Robust exception handling

Writing modular, testable Python code

Unit testing backend logic

## Use Cases

IT Operations monitoring

Server error analysis

Log analytics automation

Academic projects and evaluations

Python & Flask learning projects



