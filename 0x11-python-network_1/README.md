# 0x11. Python - Network #1

This project focuses on working with HTTP requests in Python, using both the `urllib` package and the `requests` library.

## Tasks

### 0. What's my status? #0

* File: `0-hbtn_status.py`
* Description: Python script that fetches https://alx-intranet.hbtn.io/status using the `urllib` package.
* The script displays the body of the response with the following requirements:
  - Must use a `with` statement
  - Must display the type, content, and UTF-8 content of the response

### 1. Response header value #0

* File: `1-hbtn_header.py`
* Description: Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
* Usage: `./1-hbtn_header.py <URL>`
* You must use `urllib` and `sys` packages
* The value of the X-Request-Id is different for each request

### 2. POST an email #0

* File: `2-post_email.py`
* Description: Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8).
* Usage: `./2-post_email.py <URL> <email>`
* You must use `urllib` and `sys` packages
* You don't need to check arguments passed to the script (number or type)

### 3. Error code #0

* File: `3-error_code.py`
* Description: Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
* Usage: `./3-error_code.py <URL>`
* You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
* You must use `urllib` and `sys` packages

### 4. What's my status? #1

* File: `4-hbtn_status.py`
* Description: Python script that fetches https://alx-intranet.hbtn.io/status
* You must use the package `requests`
* You are not allowed to import packages other than `requests`
* The body of the response must be display like the previous example (tabulation before -)

### 5. Response header value #1

* File: `5-hbtn_header.py`
* Description: Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
* Usage: `./5-hbtn_header.py <URL>`
* You must use the packages `requests` and `sys`
* You are not allowed to import other packages than `requests` and `sys`
* The value of this variable is different for each request

### 6. POST an email #1

* File: `6-post_email.py`
* Description: Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response.
* Usage: `./6-post_email.py <URL> <email>`
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`

### 7. Error code #1

* File: `7-error_code.py`
* Description: Python script that takes in a URL, sends a request to the URL and displays the body of the response.
* Usage: `./7-error_code.py <URL>`
* If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`

### 8. Search API

* File: `8-json_api.py`
* Description: Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
* Usage: `./8-json_api.py <letter>`
* The letter must be sent in the variable `q`
* If no argument is given, set `q=""`
* If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
* Otherwise:
  - Display `Not a valid JSON` if the JSON is invalid
  - Display `No result` if the JSON is empty
* You must use the package `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`

### 9. My GitHub!

* File: `10-my_github.py`
* Description: Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
* Usage: `./10-my_github.py <username> <password>`
* You must use Basic Authentication with a personal access token as password to access to your information (only `read:user` permission is needed)
* The first argument will be your username
* The second argument will be your password (in your case, a personal access token as password)
* You must use the package `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`

### 10. Time for an interview! (Advanced)

* File: `100-github_commits.py`
* Description: Python script that takes 2 arguments in order to solve the following challenge:
  - The first argument will be the `repository name`
  - The second argument will be the `owner name`
  - You must use the packages `requests` and `sys`
  - You are not allowed to import packages other than `requests` and `sys`
  - You don't need to check arguments passed to the script (number or type)
* The script should print 10 commits (from the most recent to oldest) of the repository by the user:
  - Format: `<sha>: <author name>` (one per line)
* Usage: `./100-github_commits.py <repository> <owner>`
