import threading

from flask import (
    Flask,
    jsonify,
    send_from_directory
)
from sqlalchemy import func
from .config import Config
from .database import (
    db,
    init_database
)
from .models import Alert
from .socket_handler import socketio
from .sniffer import start_sniffer
from flask_cors import CORS


def create_app():

    # ==============================
    # CREATE FLASK APP
    # ==============================

    app = Flask(
        __name__,
        static_folder="../Frontend",
        static_url_path=""
    )
    CORS(app)


    # ==============================
    # CONFIGURATION
    # ==============================

    app.config.from_object(
        Config
    )


    # ==============================
    # DATABASE
    # ==============================

    init_database(app)


    # ==============================
    # SOCKET.IO
    # ==============================

    socketio.init_app(app)


    # ==============================
    # START PACKET SNIFFER
    # ==============================

    def run_sniffer():

        with app.app_context():

            start_sniffer()


    sniffer_thread = threading.Thread(

        target=run_sniffer,

        daemon=True
    )


    sniffer_thread.start()


    print(
        "[SYSTEM] Packet sniffer thread started"
    )


    # ==============================
    # FRONTEND ROUTE
    # ==============================

    @app.route("/")
    def index():

        return send_from_directory(

            "../Frontend",

            "index.html"
        )


    # ==============================
    # HEALTH CHECK
    # ==============================

    @app.route("/api/health")
    def health():

        return jsonify({

            "status": "healthy",

            "packet_capture": "active",

            "database": "connected"
        })


    # ==============================
    # GET ALERTS
    # ==============================

    @app.route("/api/alerts")
    def get_alerts():

        alerts = (

            Alert.query

            .order_by(
                Alert.timestamp.desc()
            )

            .limit(100)

            .all()
        )


        return jsonify([

            alert.to_dict()

            for alert in alerts

        ])


    # ==============================
    # GET STATISTICS
    # ==============================

    @app.route("/api/stats")
    def get_stats():

        total_alerts = (
            Alert.query.count()
        )


        active_threats = (

            Alert.query.filter_by(
                status="ACTIVE"
            ).count()

        )


        total_attacks = (
            Alert.query.count()
        )


        top_attacker = (
            get_top_attacker()
        )


        return jsonify({

            "total_alerts":
                total_alerts,

            "total_attacks":
                total_attacks,

            "active_threats":
                active_threats,

            "top_attacker":
                top_attacker
        })


    # ==============================
    # CHART DATA
    # ==============================

    @app.route("/api/chart-data")
    def chart_data():

        alerts = Alert.query.all()


        attack_types = {}

        attackers = {}

        attacks_over_time = {}


        for alert in alerts:


            # Attack Types
            attack_types[
                alert.attack_type
            ] = (

                attack_types.get(
                    alert.attack_type,
                    0
                )

                + 1
            )


            # Top Attackers
            attackers[
                alert.source_ip
            ] = (

                attackers.get(
                    alert.source_ip,
                    0
                )

                + 1
            )


            # Attacks Over Time
            time_key = (

                alert.timestamp.strftime(
                    "%H:%M"
                )

            )


            attacks_over_time[
                time_key
            ] = (

                attacks_over_time.get(
                    time_key,
                    0
                )

                + 1
            )


        return jsonify({

            "attack_types":
                attack_types,

            "top_attackers":
                attackers,

            "attacks_over_time":
                attacks_over_time
        })


    return app


# ==================================
# GET TOP ATTACKER
# ==================================

def get_top_attacker():

    result = (

        Alert.query.with_entities(

            Alert.source_ip,

            func.count(
                Alert.source_ip
            )

        )

        .group_by(
            Alert.source_ip
        )

        .order_by(

            func.count(
                Alert.source_ip
            ).desc()

        )

        .first()
    )


    if result:

        return result[0]


    return "N/A"