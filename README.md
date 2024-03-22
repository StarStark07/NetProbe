# NetProbe

This Python-based network analyzer is a tool designed to detect various types of network attacks within a specified number of packets. It utilizes the Scapy library for packet manipulation and analysis, providing flexibility and extensibility in detecting different attack patterns.

## Key Features

- Detection of multiple types of network attacks including FTP exploitation, SSH brute force, Telnet spoofing, SNMP attack, RIP attack, SMTP attack, DNS attack, and SYN packets.
- Customizable attack detection functions that examine packet headers and payloads to identify specific attack patterns.
- User-friendly interface allowing the user to specify the number of packets to analyze.
- Detailed output displaying the count of packets corresponding to each detected attack type along with the count of unknown packets.
- Color-coded output for better visibility and distinction of attack detection results.

## Usage

1. Execute the script and input the desired number of packets to scan.
2. The network analyzer will capture and analyze the specified number of packets from the network.
3. After processing the packets, it will display the count of packets corresponding to each detected attack type along with the count of unknown packets.

## Author

- Developed by Piyush Kumar ([GitHub: StarStark07](https://github.com/StarStark07))

## GitHub Repository

Visit [GitHub](https://github.com/StarStark07) to explore more projects and contributions by the author.

**Note:** This network analyzer is intended for educational and informational purposes only. It can be used to enhance understanding of network security concepts and practices.
