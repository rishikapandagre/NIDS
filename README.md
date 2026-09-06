# NIDS
Network Intrusion Detection System

---

# Network Intrusion Detection System (NIDS)

A real-time Network Intrusion Detection System designed to monitor network traffic, analyze suspicious activity, detect potential attacks, and generate security alerts through an interactive dashboard.

The project combines packet sniffing, traffic analysis, rule-based detection, alert management, and a web-based visualization interface to provide a practical implementation of core Intrusion Detection System concepts.

---

## Overview

Network security requires continuous monitoring of traffic to identify malicious or suspicious behavior. This project implements a lightweight Network Intrusion Detection System capable of capturing network packets and analyzing them for indicators of potential attacks.

The system processes network activity in real time and identifies patterns associated with common network threats such as port scanning and abnormal traffic behavior.

Detected threats are processed through an alert engine and displayed on a centralized dashboard.

---

## Features

* Real-time network packet monitoring
* Network traffic analysis
* Rule-based intrusion detection
* Port scan detection
* Suspicious activity identification
* Threat confidence scoring
* Attack source tracking
* Destination IP monitoring
* Centralized alert generation
* Active threat monitoring
* REST API integration
* Real-time dashboard visualization
* Attack statistics and analytics
* Backend and frontend separation
* Modular and extensible architecture

---

<img width="1897" height="887" alt="Screenshot 2026-09-06 154906" src="https://github.com/user-attachments/assets/54f13e9e-4f2b-4390-b807-259dca4e6f0d" />
<img width="1887" height="887" alt="Screenshot 2026-09-06 155124" src="https://github.com/user-attachments/assets/a4bbc0ae-606b-441a-84aa-57f7ba11a63d" />
<img width="1892" height="865" alt="Screenshot 2026-09-06 155400" src="https://github.com/user-attachments/assets/8da9f39d-d3ca-427f-a264-5fc1c45f258c" />
<img width="1826" height="488" alt="Screenshot 2026-09-06 155432" src="https://github.com/user-attachments/assets/a10379f4-48a5-4dcb-b20c-a5b04a389189" />
<img width="1813" height="462" alt="Screenshot 2026-09-06 155507" src="https://github.com/user-attachments/assets/4aced161-eb04-4a5d-8e51-c4d9a2fb71ea" />


## System Architecture

```text
                    Network Traffic
                           |
                           v
                    +--------------+
                    |   Sniffer    |
                    +--------------+
                           |
                           v
                    +--------------+
                    | Packet Parser|
                    +--------------+
                           |
                           v
                    +--------------+
                    |   Analyzer   |
                    +--------------+
                           |
                           v
                    +--------------+
                    |   Detector   |
                    +--------------+
                           |
                    +------+------+
                    |             |
                    v             v
             Attack Detected   Normal Traffic
                    |
                    v
             +--------------+
             | Alert Engine |
             +--------------+
                    |
                    v
             +--------------+
             |   Database   |
             +--------------+
                    |
                    v
             +--------------+
             | REST API /   |
             | Socket Layer |
             +--------------+
                    |
                    v
             +--------------+
             |  Dashboard   |
             +--------------+
```

---

## Project Structure

```text
NIDS/
│
├── Backend/
│   │
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── analyzer.py
│   ├── detector.py
│   ├── alert_engine.py
│   ├── socket_handler.py
│   ├── sniffer.py
│   └── app.py
│
├── Frontend/
│   │
│   ├── index.html
│   │
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── dashboard.js
│
├── requirements.txt
│
└── README.md
```

---

## Backend Components

### `config.py`

Contains application configuration and system-level settings.

This may include:

* Database configuration
* Detection thresholds
* Network interface settings
* Application configuration

---

### `database.py`

Handles database initialization and communication.

Responsibilities include:

* Connecting to the database
* Storing attack records
* Retrieving historical alerts
* Managing threat-related data

---

### `models.py`

Defines the data structures used throughout the application.

Typical attack information includes:

```json
{
    "attack_type": "PORT_SCAN",
    "confidence": 0.9,
    "destination_ip": "192.x.x.x",
    "details": "10 unique ports accessed within 10 seconds",
    "source_ip": "192.x.x.x"
}
```

---

### `analyzer.py`

Processes captured packets and extracts relevant network information.

The analyzer may inspect:

* Source IP address
* Destination IP address
* Source port
* Destination port
* Protocol
* Packet frequency
* Connection behavior

---

### `detector.py`

Contains the intrusion detection logic.

The detector analyzes network activity and identifies suspicious patterns based on predefined rules and thresholds.

Example detection scenario:

```text
Multiple ports accessed
        +
Short time interval
        +
Same source IP
        =
Possible Port Scan
```

---

### `alert_engine.py`

Responsible for generating and managing security alerts.

The alert engine processes detected threats and assigns relevant information such as:

* Attack type
* Confidence score
* Source address
* Destination address
* Detection details
* Timestamp

---

### `socket_handler.py`

Manages communication between the backend and connected clients.

This enables real-time updates between the detection engine and the dashboard.

---

### `sniffer.py`

Captures network packets for analysis.

The packet sniffer acts as the entry point for network traffic monitoring.

Captured traffic is forwarded to the analyzer and detection engine.

---

### `app.py`

Main backend application entry point.

Responsibilities include:

* Starting the Flask application
* Registering API routes
* Initializing backend components
* Connecting the detection system
* Serving system statistics

---

## Frontend

The frontend provides a centralized security dashboard for monitoring network activity and detected threats.

### Dashboard Capabilities

* Total attack count
* Active threat count
* Total alerts
* Top attacker identification
* Attack history
* Real-time threat updates
* Security event visualization

Example system statistics:

```json
{
    "active_threats": 1,
    "top_attacker": "192.x.x.x",
    "total_alerts": 1,
    "total_attacks": 1
}
```

---

## API Integration

The frontend communicates with the backend using REST APIs.

Example backend configuration:

```javascript
const API_BASE_URL = "http://127.0.0.1:5000";
```

The API provides access to:

* Security alerts
* Attack records
* Active threats
* System statistics
* Detection history

---

## Detection Capabilities

The system is designed to detect suspicious network behavior.

Current detection capabilities include:

### Port Scanning

Detects when a single source attempts to access multiple destination ports within a defined time window.

Example:

```text
Source IP: 192.x.x.x

Ports accessed:

22
23
80
139
445
3306
5432
8080
```

If the number of unique ports exceeds the configured threshold within a short period, the activity is flagged as a potential port scan.

---

## Technology Stack

### Backend

* Python
* Flask
* Socket-based communication
* Network packet analysis libraries
* SQL database integration

### Frontend

* HTML5
* CSS3
* JavaScript

### Security Testing Environment

The project can be tested in an isolated laboratory environment using:

* Kali Linux
* Metasploitable
* Nmap
* Scapy
* hping3
* Wireshark

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/NIDS.git
```

```bash
cd NIDS
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

#### Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Navigate to the backend directory:

```bash
cd Backend
```

Start the application:

```bash
python app.py
```

The backend server will start on:

```text
http://127.0.0.1:5000
```

Open the frontend dashboard through your preferred development server or browser configuration.

---

## Testing

The system should be tested only in an authorized and isolated environment.

A recommended lab setup:

```text
+------------------+
|   Kali Linux     |
| Attack Simulator |
+--------+---------+
         |
         |
         v
+------------------+
|      Network     |
|     Traffic      |
+--------+---------+
         |
         v
+------------------+
|       NIDS       |
| Detection Engine |
+--------+---------+
         |
         v
+------------------+
|   Web Dashboard  |
+------------------+
```

Testing tools may include:

* Nmap for network scanning simulation
* Scapy for custom packet generation
* hping3 for packet-based traffic testing
* Wireshark for packet inspection

Only perform security testing against systems you own or have explicit permission to test.

---

## Example Detection Flow

```text
1. Network packet is captured
          |
          v
2. Packet information is extracted
          |
          v
3. Traffic behavior is analyzed
          |
          v
4. Detection rules are applied
          |
          v
5. Suspicious activity is identified
          |
          v
6. Alert is generated
          |
          v
7. Alert is stored
          |
          v
8. Dashboard receives update
```

---

## Future Improvements

Potential future enhancements include:

* Machine learning-based anomaly detection
* DDoS attack detection
* Brute-force attack detection
* ARP spoofing detection
* SQL injection traffic pattern detection
* DNS tunneling detection
* Advanced packet classification
* Threat severity levels
* IP reputation checking
* Automated threat response
* Firewall integration
* Email notifications
* WebSocket-based real-time updates
* Geographic IP visualization
* Threat intelligence integration
* Advanced analytics and reporting

---

## Security Considerations

This project is intended for educational, research, and authorized security testing purposes.

The system should only be deployed on networks where monitoring is permitted.

Do not use network security testing tools against systems without explicit authorization.

---

## Learning Objectives

This project demonstrates practical concepts in:

* Network security
* Intrusion detection systems
* Packet analysis
* Network monitoring
* Cybersecurity engineering
* Backend development
* REST APIs
* Real-time dashboards
* Threat detection logic
* Security event management

---

## Project Status

**Status: Active Development**

The project is being developed incrementally, with core backend components and detection functionality implemented and additional detection capabilities planned.

---

## Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Commit your changes
5. Push to your branch
6. Create a Pull Request

---

## License

This project is intended for educational and research purposes.

Consider adding an appropriate open-source license such as the MIT License.

---

## Disclaimer

This project is developed for educational purposes and authorized security research.

The author is not responsible for misuse of the software or techniques associated with network security testing.

All testing should be performed in controlled environments or against systems where explicit permission has been granted.
