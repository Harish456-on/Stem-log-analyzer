import re


def analyze_logs(file_path):
    suspicious = 0

    with open(file_path, 'r') as file:
        logs = file.readlines()

    for line in logs:
        if "failed" in line.lower() or "error" in line.lower():
            print(f"[ALERT] {line.strip()}")
            suspicious += 1

    print(f"\nTotal suspicious events: {suspicious}")


if __name__ == "__main__":
    path = input("Enter log file path: ")
    analyze_logs(path)