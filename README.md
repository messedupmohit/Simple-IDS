# Simple Intrusion Detection System (IDS)

## Overview
This project implements a basic Intrusion Detection System (IDS) using Python. The IDS monitors network traffic in real-time and triggers alerts when suspicious activities or potential intrusions are detected.

## Project Structure
- **ids/**: Contains the core detection logic and configuration settings for the IDS.
- **scripts/**: Includes shell scripts for managing and executing the IDS.
- **logs/**: Stores log files where detected suspicious activities are recorded.
- **main.py**: The main script to run the IDS.

## How to Run

1. **Ensure Python is installed**: Make sure Python is installed on your system.

2. **Install required dependencies**:  
   Run the following command to install the required Python package:
   ```bash
   pip install scapy
   ```

3. **Run the IDS**:  
   Use the following command to start the IDS (root privileges are required for network traffic monitoring):
   ```bash
   sudo python3 main.py
   ```

4. **Monitor Alerts**:  
   Check the `logs/ids.log` file for detection alerts using:
   ```bash
   tail -f logs/ids.log
   ```

## Configuration
To customize the IDS, modify `ids/config.py`. You can configure parameters such as suspicious IP addresses, port numbers, and other detection settings.

## License
This project is licensed under the MIT License.

