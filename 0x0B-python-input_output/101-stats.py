#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- Input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>
- Prints statistics every 10 lines and on keyboard interruption (CTRL + C).
"""

import sys

total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """
    Function to print the statistics (total file size and status code counts).
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            total_file_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1
        except Exception:
            pass

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
