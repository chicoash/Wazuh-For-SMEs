import os
import re
import requests
import json
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

# load .env that sits next to this script
load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

def get_secret(name: str) -> str:
    val = os.getenv(name)
    if not val:
        raise RuntimeError(f"{name} is missing")
    return val

# User-defined variables
api_url = "https://<replacethis>.sentinelone.net/web/api/v2.1/threats?limit=10" # change url
# api_key = "<API_KEY>" # uncomment this line to use API directly
api_key = get_secret("API_KEY")
log_file_path = "/var/log/sentinelone.json"
custom_timestamp = "2025-08-01T00:00:00" #Enter your preferred timestamp within the quotes using the format 2023-01-01T00:00:00


def get_last_timestamp(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                match = re.search(r'"createdAt":\s*"([^"]+)"', last_line)
                if match:
                    last_created_at = match.group(1)
                    last_timestamp = datetime.strptime(last_created_at, "%Y-%m-%dT%H:%M:%S.%fZ").isoformat()
                    return last_timestamp
                else:
                    return None
            else:
                return None
    except FileNotFoundError:
        return None

def get_logs(start_timestamp):
    headers = {
        'Authorization': f'ApiToken {api_key}',
        'Content-Type': 'application/json'
    }

    # Construct query parameters
    params = {}
    if start_timestamp:
        params['createdAt__gt'] = start_timestamp

    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch logs: {response.status_code}")
        return None

def main():
    # Get the last timestamp from the log file
    last_timestamp = get_last_timestamp(log_file_path)
    if last_timestamp:
        print(f"Last timestamp in log file: {last_timestamp}")
    else:
        print("Log file is empty or doesn't exist.")

    if custom_timestamp:
        # If custom timestamp is specified, check the log file first
        last_timestamp_from_file = get_last_timestamp(log_file_path)
        if last_timestamp_from_file:
            start_timestamp = last_timestamp_from_file
            print(f"Using last timestamp from log file: {start_timestamp}")
        else:
            start_timestamp = custom_timestamp
            print(f"Using custom timestamp: {start_timestamp}")
    else:
        start_timestamp = last_timestamp
        if last_timestamp:
            print(f"Using last timestamp from log file: {start_timestamp}")
        else:
            print("No last timestamp found in log file.")
            start_timestamp = None  # Reset start timestamp to None if neither custom nor file timestamp available

    # Query the SentinelOne API for logs since the start timestamp
    logs = get_logs(start_timestamp)

    if logs:
        # Write the logs to the local log file
        with open(log_file_path, 'a') as file:
            for log in logs['data']:
                file.write(json.dumps(log))
                file.write('\n')
        print(f"Logs written to {log_file_path}")
    else:
        print("No logs fetched.")

if __name__ == "__main__":
    main()