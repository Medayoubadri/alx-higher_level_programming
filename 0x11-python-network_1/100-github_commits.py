#!/usr/bin/python3
"""
Python script that lists 10 commits (from the most recent to oldest)
of a repository by a specific user.
"""
import requests
import sys


if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    params = {'per_page': 10}
    r = requests.get(url, params=params)

    commits = r.json()
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
