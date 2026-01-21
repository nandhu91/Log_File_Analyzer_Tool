import re
import pandas as pd

LOG_PATTERN = re.compile(
    r"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s"
    r"(\d+\.\d+\.\d+\.\d+)\s"
    r"(GET|POST|PUT|DELETE)\s"
    r"(\d{3})"
)

def parse_logs(file_path):
    valid_logs = []
    total_lines = 0
    corrupted = 0

    with open(file_path, "r") as file:
        for line in file:
            total_lines += 1
            match = LOG_PATTERN.match(line.strip())
            if match:
                valid_logs.append(match.groups())
            else:
                corrupted += 1

    return valid_logs, total_lines, corrupted

def analyze_logs(logs):
    df = pd.DataFrame(
        logs,
        columns=["Timestamp", "IP", "Method", "Status"]
    )

    df["Status"] = df["Status"].astype(int)
    error_df = df[df["Status"] >= 400]

    return {
        "total_valid_requests": len(df),
        "total_errors": len(error_df),
        "error_counts": error_df["Status"].value_counts().sort_index(),
        "top_ips": error_df["IP"].value_counts().head(5)
    }

