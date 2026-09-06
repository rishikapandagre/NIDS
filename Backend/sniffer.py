from datetime import datetime

from scapy.all import (
    sniff,
    IP,
    TCP,
    UDP
)

from .analyzer import traffic_analyzer
from .detector import run_detection
from .alert_engine import create_alert


# ==================================
# EXTRACT PACKET FEATURES
# ==================================

def extract_packet_features(packet):

    if IP not in packet:

        return None


    packet_data = {

        "src_ip": packet[IP].src,

        "dst_ip": packet[IP].dst,

        "src_port": None,

        "dst_port": None,

        "protocol": "OTHER",

        "packet_length": len(packet),

        "timestamp": datetime.now(),

        "tcp_flags": None
    }


    # TCP Packet
    if TCP in packet:

        packet_data["src_port"] = (
            packet[TCP].sport
        )

        packet_data["dst_port"] = (
            packet[TCP].dport
        )

        packet_data["protocol"] = "TCP"

        packet_data["tcp_flags"] = str(
            packet[TCP].flags
        )


    # UDP Packet
    elif UDP in packet:

        packet_data["src_port"] = (
            packet[UDP].sport
        )

        packet_data["dst_port"] = (
            packet[UDP].dport
        )

        packet_data["protocol"] = "UDP"


    return packet_data


# ==================================
# PROCESS PACKET
# ==================================

def process_packet(packet):

    try:

        packet_data = extract_packet_features(
            packet
        )


        if not packet_data:

            return


        # Step 1: Analyze traffic
        traffic_analyzer.process_packet(
            packet_data
        )


        # Step 2: Run detection engine
        alerts = run_detection(

            packet_data,

            traffic_analyzer
        )


        # Step 3: Create alerts
        for alert in alerts:

            create_alert(alert)


    except Exception as error:

        print(
            f"[SNIFFER ERROR] {error}"
        )


# ==================================
# START SNIFFER
# ==================================

def start_sniffer(interface=None):

    print("[SNIFFER] Packet capture started")
    print(f"[SNIFFER] Interface: {interface}")

    sniff(
        iface=interface,
        prn=process_packet,
        store=False
    )