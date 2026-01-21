import random
from datetime import datetime, timedelta
import os

# Configuration
NUM_LINES = 50000
LOG_DIR = "logs"
OUTPUT_FILE = os.path.join(LOG_DIR, "server.log")

methods = ["GET", "POST", "PUT", "DELETE"]
status_codes = [200, 200, 200, 404, 404, 403, 500]

start_time = datetime.now()

def random_ip():
    return f"192.168.1.{random.randint(1, 254)}"

# ✅ Create logs folder if not exists
if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)

with open(OUTPUT_FILE, "w") as file:
    for i in range(NUM_LINES):
        timestamp = start_time + timedelta(seconds=i)
        ip = random_ip()
        method = random.choice(methods)
        status = random.choice(status_codes)

        file.write(
            f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} "
            f"{ip} {method} {status}\n"
        )

print(f"{NUM_LINES} log entries generated in {OUTPUT_FILE}")
