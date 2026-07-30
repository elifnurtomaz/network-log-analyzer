from collections import Counter

LOG_FILE = "sample.log"


def read_logs(filename):
    with open(filename, "r") as file:
        return file.readlines()


logs = read_logs(LOG_FILE)

protocol_counter = Counter()
action_counter = Counter()
source_ip_counter = Counter()
destination_ip_counter = Counter()

for log in logs:
    parts = log.strip().split()

    source_ip = parts[0]
    destination_ip = parts[2]
    protocol = parts[3]
    port = parts[4]
    action = parts[5]

    protocol_counter[protocol] += 1
    action_counter[action] += 1
    source_ip_counter[source_ip] += 1
    destination_ip_counter[destination_ip] += 1


print("=" * 40)
print("NETWORK LOG ANALYZER")
print("=" * 40)

print(f"\nTotal log entries: {len(logs)}")

print("\nProtocol Statistics")
for protocol, count in protocol_counter.items():
    print(f"  {protocol}: {count}")

print("\nAction Statistics")
for action, count in action_counter.items():
    print(f"  {action}: {count}")

print(f"\nMost common source IP: {source_ip_counter.most_common(1)[0][0]}")

print(f"Most common destination IP: {destination_ip_counter.most_common(1)[0][0]}")
print("\nTop Source IPs")
for ip, count in source_ip_counter.most_common(3):
    print(f"  {ip}: {count}")

print("\nTop Destination IPs")
for ip, count in destination_ip_counter.most_common(3):
    print(f"  {ip}: {count}")

print("\nAnalysis completed successfully.")