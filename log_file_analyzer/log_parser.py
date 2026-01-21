import re
import logging

LOG_PATTERN = re.compile(
    r"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s"
    r"(\d+\.\d+\.\d+\.\d+)\s"
    r"(GET|POST|PUT|DELETE)\s"
    r"(\d{3})"
)

def parse_logs(file_path):
    valid_logs = []
    corrupted = 0
    total_lines = 0

    with open(file_path, "r") as file:
        for line in file:
            total_lines += 1
            match = LOG_PATTERN.match(line.strip())
            if match:
                valid_logs.append(match.groups())
            else:
                corrupted += 1
                logging.warning(f"Corrupted entry skipped: {line.strip()}")

    return valid_logs, total_lines, corrupted
