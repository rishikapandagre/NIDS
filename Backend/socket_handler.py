from flask_socketio import SocketIO


socketio = SocketIO(

    cors_allowed_origins="*",

    async_mode="threading"
)


def emit_alert(alert):

    socketio.emit(
        "new_alert",
        alert
    )


def emit_system_status(status):

    socketio.emit(
        "system_status",
        status
    )