#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
