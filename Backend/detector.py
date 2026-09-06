from .config import (

    PORT_SCAN_THRESHOLD,

    PORT_SCAN_TIME_WINDOW,

    PACKETS_PER_SECOND_THRESHOLD,

    SUSPICIOUS_IPS
)


# ==================================
# PORT SCAN DETECTION
# ==================================

def detect_port_scan(packet, analyzer):

    src_ip = packet.get("src_ip")


    if not src_ip:
        return None


    recent_ports = analyzer.get_recent_ports(

        src_ip,

        PORT_SCAN_TIME_WINDOW
    )


    if len(recent_ports) >= PORT_SCAN_THRESHOLD:

        return {

            "source_ip": src_ip,

            "destination_ip": packet.get(
                "dst_ip"
            ),

            "attack_type": "PORT_SCAN",

            "severity": "HIGH",

            "details": (
                f"{len(recent_ports)} unique ports "
                f"accessed within "
                f"{PORT_SCAN_TIME_WINDOW} seconds"
            ),

            "confidence": 0.90
        }


    return None


# ==================================
# SUSPICIOUS IP DETECTION
# ==================================

def detect_suspicious_ip(packet):

    src_ip = packet.get("src_ip")


    if not src_ip:
        return None


    if src_ip in SUSPICIOUS_IPS:

        return {

            "source_ip": src_ip,

            "destination_ip": packet.get(
                "dst_ip"
            ),

            "attack_type": "SUSPICIOUS_IP",

            "severity": "CRITICAL",

            "details": (
                "Source IP matched suspicious "
                "IP watchlist"
            ),

            "confidence": 1.0
        }


    return None


# ==================================
# TRAFFIC SPIKE DETECTION
# ==================================

def detect_traffic_spike(packet, analyzer):

    src_ip = packet.get("src_ip")


    if not src_ip:
        return None


    packet_rate = analyzer.get_packets_per_second(
        src_ip
    )


    if packet_rate >= PACKETS_PER_SECOND_THRESHOLD:

        return {

            "source_ip": src_ip,

            "destination_ip": packet.get(
                "dst_ip"
            ),

            "attack_type": "TRAFFIC_SPIKE",

            "severity": "MEDIUM",

            "details": (
                f"{packet_rate} packets per second detected"
            ),

            "confidence": 0.75
        }


    return None


# ==================================
# RUN ALL DETECTORS
# ==================================

def run_detection(packet, analyzer):

    alerts = []


    # Port Scan
    port_scan_alert = detect_port_scan(
        packet,
        analyzer
    )

    if port_scan_alert:
        alerts.append(port_scan_alert)


    # Suspicious IP
    suspicious_ip_alert = detect_suspicious_ip(
        packet
    )

    if suspicious_ip_alert:
        alerts.append(
            suspicious_ip_alert
        )


    # Traffic Spike
    traffic_spike_alert = detect_traffic_spike(
        packet,
        analyzer
    )

    if traffic_spike_alert:
        alerts.append(
            traffic_spike_alert
        )


    return alerts