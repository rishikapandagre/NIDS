from threading import Thread

from Backend.app import create_app
from Backend.socket_handler import socketio
from Backend.sniffer import start_sniffer


# =========================
# CREATE APPLICATION
# =========================

app = create_app()


# =========================
# VMNET8 CAPTURE INTERFACE
# =========================

CAPTURE_INTERFACE = (
    r"\Device\NPF_{DBF981C3-3587-4B37-B551-7A76C5231ACE}"
)


# =========================
# START PACKET SNIFFER
# =========================

def start_packet_sniffer():

    # Give the background thread
    # access to Flask application context
    with app.app_context():

        start_sniffer(
            interface=CAPTURE_INTERFACE
        )


# =========================
# START NIDS
# =========================

if __name__ == "__main__":

    print("=" * 50)
    print("Starting NIDS Server...")
    print("=" * 50)

    # Start sniffer in background thread
    sniffer_thread = Thread(
        target=start_packet_sniffer,
        daemon=True
    )

    sniffer_thread.start()

    # Start Flask + Socket.IO server
    socketio.run(
        app,
        host="127.0.0.1",
        port=5000,
        debug=False
    )