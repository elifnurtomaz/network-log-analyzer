import sys

from parser import read_logs, parse_logs
from analyzer import analyze_logs
from report import print_report, save_report


if len(sys.argv) > 1:
    log_file = sys.argv[1]
else:
    log_file = "logs/sample.log"


logs = read_logs(log_file)

parsed_logs = parse_logs(logs)

results = analyze_logs(parsed_logs)

print_report(results)

save_report(results, "reports/report.txt")

print("\nReport saved to reports/report.txt")