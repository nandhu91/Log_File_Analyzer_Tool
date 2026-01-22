Log File Analyzer Tool (Flask)

A Python Flask–based web application that analyzes large server log files and generates actionable insights for IT Operations.
It efficiently parses logs, handles corrupted entries, identifies HTTP errors, highlights top IP addresses causing issues, and visualizes results using charts.

 Features

 Upload .log or .txt server log files

 Efficient processing for large log files

 Graceful handling of corrupted/invalid log entries

 HTTP error code frequency analysis (4xx, 5xx)

 Top 5 IP addresses generating the highest errors

 Visualizations using Matplotlib

 Option to analyze multiple files without restarting the app

 Clean, professional, full-page UI
 
 Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS

Data Processing: Pandas, Regular Expressions

Visualization: Matplotlib

Project Structure
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

Install Dependencies
pip install -r requirements.txt
pip install flask pandas matplotlib

Run the Application
python app.py

Open in Browser
http://127.0.0.1:5000/

Run Test Cases
python -m unittest tests/test_cases.py

Output

Summary Cards

Total Requests

Total Errors

Corrupted Lines

Tables

Error Code Frequency

Top 5 IP Addresses

Graphs

HTTP Error Code Distribution

IP Address Error Distribution



