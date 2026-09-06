from datetime import (
    datetime,
    timedelta
)

from .database import db
from .models import Alert
from .socket_handler import emit_alert
from .config import ALERT_COOLDOWN


# ==================================
# CHECK DUPLICATE ALERT
# ==================================

def is_duplicate(alert_data):

    cooldown_time = (
        datetime.now()
        - timedelta(
            seconds=ALERT_COOLDOWN
        )
    )


    existing_alert = Alert.query.filter(

        Alert.source_ip ==
        alert_data.get(
            "source_ip",
            "UNKNOWN"
        ),

        Alert.attack_type ==
        alert_data.get(
            "attack_type",
            "UNKNOWN"
        ),

        Alert.timestamp >= cooldown_time

    ).first()


    return existing_alert is not None


# ==================================
# CREATE ALERT
# ==================================

def create_alert(alert_data):

    if is_duplicate(alert_data):

        return None


    alert = Alert(

        source_ip=alert_data.get(
            "source_ip",
            "UNKNOWN"
        ),

        destination_ip=alert_data.get(
            "destination_ip"
        ),

        attack_type=alert_data.get(
            "attack_type",
            "UNKNOWN"
        ),

        severity=alert_data.get(
            "severity",
            "LOW"
        ),

        status="ACTIVE",

        details=alert_data.get(
            "details",
            ""
        ),

        confidence=alert_data.get(
            "confidence",
            0.0
        )
    )


    db.session.add(alert)

    db.session.commit()


    alert_dict = alert.to_dict()


    # Send real-time event
    emit_alert(alert_dict)


    print(

        f"[ALERT] "
        f"{alert.attack_type} "
        f"from {alert.source_ip}"

    )


    return alert_dict