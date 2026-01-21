from flask import Flask, render_template, request, redirect
import os
import logging
import matplotlib.pyplot as plt

from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from logger_config import setup_logger
from log_parser import parse_logs
from analyzer import analyze_logs

# -----------------------------
# Flask App Configuration
# -----------------------------
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Windows-safe upload folder creation
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

setup_logger()
logging.info("Log File Analyzer application started")

# -----------------------------
# Utility Function
# -----------------------------
def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

# -----------------------------
# Routes
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    """
    Upload page for log/txt file
    """
    if request.method == "POST":
        file = request.files.get("logfile")

        if not file or file.filename == "":
            return "No file selected"

        if not allowed_file(file.filename):
            return "Only .log or .txt files are allowed"

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        logging.info(f"File uploaded: {file.filename}")
        return redirect(f"/report?file={file.filename}")

    return render_template("index.html")


@app.route("/report")
def report():
    """
    Analyze uploaded log file and show report
    """
    filename = request.args.get("file")
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    if not os.path.exists(filepath):
        return "File not found"

    # Parse logs
    logs, total_lines, corrupted = parse_logs(filepath)

    # Analyze logs
    result = analyze_logs(logs)

    # Generate error distribution chart
    plt.figure()
    result["error_counts"].plot(kind="bar")
    plt.xlabel("HTTP Error Code")
    plt.ylabel("Count")
    plt.title("HTTP Error Code Frequency Distribution")
    plt.tight_layout()
    plt.savefig("static/error_chart.png")
    plt.close()

    logging.info("Log analysis completed successfully")

    return render_template(
        "report.html",
        total_lines=total_lines,
        corrupted=corrupted,
        total_valid_requests=result["total_valid_requests"],
        total_errors=result["total_errors"],
        error_rate=result["error_rate"],
        error_counts=result["error_counts"],
        top_ips=result["top_ips"]
    )

# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
