#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- Input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>
- Prints statistics every 10 lines and on keyboard interruption (CTRL + C).
"""

import sys


def print_stats(total_size, status_counts):
    """
    Prints the total file size and the count of status codes ascending order.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) >= 2:
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                total_size += file_size

                if status_code in status_counts:
                    status_counts[status_code] += 1
            except (ValueError, IndexError):
                pass

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise

print_stats(total_size, status_counts)
