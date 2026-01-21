import pandas as pd

def analyze_logs(logs):
    df = pd.DataFrame(
        logs,
        columns=["Timestamp", "IP", "Method", "Status"]
    )

    df["Status"] = df["Status"].astype(int)

    total_valid_requests = len(df)

    error_df = df[df["Status"] >= 400]
    total_errors = len(error_df)

    error_rate = round((total_errors / total_valid_requests) * 100, 2) if total_valid_requests > 0 else 0

    return {
        "total_valid_requests": total_valid_requests,
        "total_errors": total_errors,
        "error_rate": error_rate,
        "error_counts": error_df["Status"].value_counts().sort_index(),
        "top_ips": error_df["IP"].value_counts().head(5)
    }

