from collections import defaultdict, deque
from datetime import datetime


class TrafficAnalyzer:

    def __init__(self):

        # Ports accessed by each IP
        self.ip_ports = defaultdict(
            lambda: deque()
        )

        # Packet timestamps per IP
        self.ip_packets = defaultdict(
            lambda: deque()
        )

        # Protocol statistics
        self.protocol_distribution = defaultdict(int)

        # Connection history
        self.connection_history = defaultdict(
            lambda: deque(maxlen=100)
        )


    def process_packet(self, packet):

        src_ip = packet.get("src_ip")

        dst_port = packet.get("dst_port")

        protocol = packet.get("protocol")

        timestamp = packet.get("timestamp")


        if not src_ip:
            return


        # Store accessed ports
        if dst_port is not None:

            self.ip_ports[src_ip].append(
                (dst_port, timestamp)
            )


        # Store packet timestamps
        self.ip_packets[src_ip].append(
            timestamp
        )


        # Protocol distribution
        if protocol:

            self.protocol_distribution[
                protocol
            ] += 1


        # Connection history
        self.connection_history[
            src_ip
        ].append(packet)


    def get_recent_ports(
        self,
        ip,
        time_window
    ):

        now = datetime.now()

        recent_ports = set()

        packets = self.ip_ports[ip]


        while packets:

            port, timestamp = packets[0]

            if (
                now - timestamp
            ).total_seconds() > time_window:

                packets.popleft()

            else:
                break


        for port, timestamp in packets:

            recent_ports.add(port)


        return recent_ports


    def get_packets_per_second(
        self,
        ip
    ):

        now = datetime.now()

        packets = self.ip_packets[ip]


        while packets:

            timestamp = packets[0]

            if (
                now - timestamp
            ).total_seconds() > 1:

                packets.popleft()

            else:
                break


        return len(packets)


    def get_protocol_distribution(self):

        return dict(
            self.protocol_distribution
        )


# Global analyzer instance
traffic_analyzer = TrafficAnalyzer()