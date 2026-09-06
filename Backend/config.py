import os


BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


DATABASE_PATH = os.path.join(
    BASE_DIR,
    "Database",
    "nids.db"
)


class Config:

    SECRET_KEY = "nids-secret-key-change-this"

    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{DATABASE_PATH}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


# ==================================
# DETECTION CONFIGURATION
# ==================================

# Port Scan Detection
PORT_SCAN_THRESHOLD = 10
PORT_SCAN_TIME_WINDOW = 10


# Traffic Spike Detection
PACKETS_PER_SECOND_THRESHOLD = 100


# Suspicious IP Watchlist
SUSPICIOUS_IPS = {
    "10.10.10.50",
    "192.168.1.200",
}


# Alert Deduplication Window
ALERT_COOLDOWN = 10