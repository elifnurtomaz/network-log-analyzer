# Network Log Analyzer

A simple Python-based network log analyzer developed as a cybersecurity learning project.

## Features

- Reads network log files
- Counts total log entries
- Analyzes network protocols (TCP, UDP, ICMP)
- Counts ACCEPT and DENY actions
- Finds the most common source and destination IP addresses
- Displays the top 3 source and destination IPs

## Sample Log Format

```text
192.168.1.5 -> 8.8.8.8 TCP 80 ACCEPT
```

## Example Output

```text
========================================
NETWORK LOG ANALYZER
========================================

Total log entries: 8

Protocol Statistics
TCP: 5
UDP: 2
ICMP: 1

Action Statistics
ACCEPT: 5
DENY: 3
```

## Technologies

- Python 3
- Counter (collections)

## Project Structure

```
network-log-analyzer/
│
├── analyzer.py
├── sample.log
├── README.md
├── requirements.txt
└── .gitignore
```

## Future Improvements

- CSV support
- Report generation
- Data visualization
- Command-line arguments
- Suspicious activity detection

## Screenshot

![Program Output](images/output.png)