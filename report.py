def print_report(results):
    """Print analysis results to the terminal."""

    print("=" * 40)
    print("NETWORK LOG ANALYZER")
    print("=" * 40)

    print(f"\nTotal log entries: {results['total_logs']}")

    print("\nProtocol Statistics")
    for protocol, count in results["protocol_counter"].items():
        print(f"  {protocol}: {count}")

    print("\nAction Statistics")
    for action, count in results["action_counter"].items():
        print(f"  {action}: {count}")

    print(
        f"\nMost common source IP: "
        f"{results['source_ip_counter'].most_common(1)[0][0]}"
    )

    print(
        f"Most common destination IP: "
        f"{results['destination_ip_counter'].most_common(1)[0][0]}"
    )

    print("\nTop Source IPs")
    for ip, count in results["source_ip_counter"].most_common(3):
        print(f"  {ip}: {count}")

    print("\nTop Destination IPs")
    for ip, count in results["destination_ip_counter"].most_common(3):
        print(f"  {ip}: {count}")

    print("\nSuspicious Activity")

    found = False

    for ip, count in results["denied_ips"].items():
        if count >= 3:
            print(f"WARNING: {ip} has {count} denied connections.")
            found = True

    if not found:
        print("No suspicious activity detected.")

    print("\nAnalysis completed successfully.")


def save_report(results, filename):
    """Save analysis results to a text file."""

    with open(filename, "w") as report:

        report.write("NETWORK LOG ANALYSIS REPORT\n")
        report.write("=" * 40 + "\n\n")

        report.write(f"Total log entries: {results['total_logs']}\n\n")

        report.write("Protocol Statistics\n")
        for protocol, count in results["protocol_counter"].items():
            report.write(f"{protocol}: {count}\n")

        report.write("\nAction Statistics\n")
        for action, count in results["action_counter"].items():
            report.write(f"{action}: {count}\n")

        report.write(
            f"\nMost common source IP: "
            f"{results['source_ip_counter'].most_common(1)[0][0]}\n"
        )

        report.write(
            f"Most common destination IP: "
            f"{results['destination_ip_counter'].most_common(1)[0][0]}\n"
        )