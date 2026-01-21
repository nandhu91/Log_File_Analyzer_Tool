from flask import Flask, render_template, request, redirect
import os
import matplotlib.pyplot as plt

from analyzer_utils import parse_logs, analyze_logs

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if not exists (Windows-safe)
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

# ---------------- UPLOAD PAGE ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("logfile")
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            return redirect(f"/report?file={file.filename}")

    return render_template("index.html")

# ---------------- REPORT PAGE ----------------
@app.route("/report")
def report():
    filename = request.args.get("file")
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    logs, total_lines, corrupted = parse_logs(filepath)
    result = analyze_logs(logs)

    # Error code chart
    plt.figure()
    result["error_counts"].plot(kind="bar")
    plt.xlabel("HTTP Error Code")
    plt.ylabel("Count")
    plt.title("HTTP Error Code Frequency Distribution")
    plt.tight_layout()
    plt.savefig("static/error_chart.png")
    plt.close()

    # IP address chart
    plt.figure()
    result["top_ips"].plot(kind="bar")
    plt.xlabel("IP Address")
    plt.ylabel("Error Count")
    plt.title("Top IP Addresses Generating Errors")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/ip_error_chart.png")
    plt.close()

    return render_template(
        "report.html",
        total_lines=total_lines,
        corrupted=corrupted,
        **result
    )

if __name__ == "__main__":
    app.run(debug=True)
