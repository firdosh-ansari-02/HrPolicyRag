"""
Shared logger used by every module in the application.

All modules use this file to create their logger so that:
- Logs have a consistent format
- Each execution gets its own log file
- Logs are organized by Year / Month / Day
"""

import logging
import os
from datetime import datetime


# ---------------------------------------------------------
# 1. Get current date/time
# ---------------------------------------------------------

now = datetime.now()

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")


# ---------------------------------------------------------
# 2. Create date-based log directory
# ---------------------------------------------------------

LOGS_DIR = os.path.join(
    "logs",
    year,
    month,
    day
)

os.makedirs(LOGS_DIR, exist_ok=True)


# ---------------------------------------------------------
# 3. Create one log file for this application run
# ---------------------------------------------------------

RUN_LOG_FILE = os.path.join(
    LOGS_DIR,
    f"run_{timestamp}.log"
)


# ---------------------------------------------------------
# 4. Configure logging
# ---------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,

    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    ),

    handlers=[
        logging.FileHandler(
            RUN_LOG_FILE,
            encoding="utf-8"
        ),

        logging.StreamHandler()
    ]
)


# ---------------------------------------------------------
# 5. Logger factory
# ---------------------------------------------------------

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)