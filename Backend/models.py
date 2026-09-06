from datetime import datetime

from .database import db


class Alert(db.Model):

    __tablename__ = "alerts"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    source_ip = db.Column(
        db.String(45),
        nullable=False
    )


    destination_ip = db.Column(
        db.String(45),
        nullable=True
    )


    attack_type = db.Column(
        db.String(100),
        nullable=False
    )


    severity = db.Column(
        db.String(20),
        nullable=False
    )


    timestamp = db.Column(
        db.DateTime,
        default=datetime.now,
        nullable=False
    )


    status = db.Column(
        db.String(20),
        default="ACTIVE"
    )


    details = db.Column(
        db.Text,
        nullable=True
    )


    confidence = db.Column(
        db.Float,
        default=0.0
    )


    def to_dict(self):

        return {

            "id": self.id,

            "source_ip": self.source_ip,

            "destination_ip": self.destination_ip,

            "attack_type": self.attack_type,

            "severity": self.severity,

            "timestamp": (
                self.timestamp.isoformat()
                if self.timestamp
                else None
            ),

            "status": self.status,

            "details": self.details,

            "confidence": self.confidence
        }