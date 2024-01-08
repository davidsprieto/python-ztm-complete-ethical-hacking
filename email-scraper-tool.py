from bs4 import BeautifulSoup
import requests.exceptions
import urllib.parse
from collections import deque
import re

user_url = str(input('[+] Enter Target URL To Scan: '))
urls = deque([user_url])

scraped_urls = set()
emails = set()

count = 0
try:
    while len(urls):
        count += 1
        if count == 100:
            break
        url = urls.popleft()
        scraped_urls.add(url)

        parts = urllib.parse.urlsplit(url)
        base_url = '{0.scheme}://{0.netloc}'.format(parts)

        path = url[:url.rfind('/') + 1] if '/' in parts.path else url

        print('[%d] Processing %s' % (count, url))
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        new_emails = set(re.findall(r"[a-z0-9.\-+_]+@[a-z0-9.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, features="lxml")

        for anchor in soup.find_all("a"):
            link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            if not link in urls and not link in scraped_urls:
                urls.append(link)
except KeyboardInterrupt:
    print('[-] Closing!')

for mail in emails:
    print(mail)

# CODE EXPLANATION:
# This code is a web scraping script that scans a target URL for email addresses.
# First, it imports the necessary modules: `BeautifulSoup` from the `bs4` library for parsing HTML, `requests` for making HTTP requests,
# `requests.exceptions` for handling exceptions related to requests, `urllib.parse` for parsing URLs, and `deque` from the `collections`
# library for creating a queue.
# Next, it prompts the user to enter the target URL to scan and stores it in the `user_url` variable.
# It initializes a queue called `urls` with the user-provided URL.
# It also initializes two sets: `scraped_urls` to keep track of the URLs that have been scraped, and `emails` to store the email addresses found.
# A `count` variable is set to 0 to keep track of the number of URLs processed.
# The code then enters a `while` loop that continues as long as there are URLs in the `urls` queue. The loop is limited to 100 iterations to prevent infinite looping.
# Inside the loop, the first URL in the queue is removed using the `popleft()` method and stored in the `url` variable.
# The URL is added to the `scraped_urls` set to keep track of it.
# The `urlsplit()` function from the `urllib.parse` module is used to split the URL into its components (scheme, netloc, path, etc.). The `base_url` variable is then created by formatting the scheme and netloc components.
# The `path` variable is set to the URL up to the last slash (`/`) if there is one in the path component of the URL. Otherwise, it is set to the entire URL.
# A message is printed to indicate the current URL being processed.
# A `try-except` block is used to handle any exceptions that may occur during the HTTP request. If a `MissingSchema` or `ConnectionError` exception is raised, the loop continues to the next iteration.
# If the request is successful, the response is stored in the `response` variable.
# The `re.findall()` function is used to find all email addresses in the response text using a regular expression pattern. The found email addresses are added to the `new_emails` set.
# The `update()` method is used to add the new email addresses to the `emails` set.
# The response text is parsed using `BeautifulSoup` with the "lxml" parser.
# A loop is used to iterate over all anchor (`<a>`) tags in the parsed HTML.
# The `href` attribute of each anchor tag is checked. If it exists, it is stored in the `link` variable. Otherwise, an empty string is assigned to `link`.
# If the `link` starts with a slash (`/`), it is appended to the `base_url` to create an absolute URL. If it doesn't start with "http", it is appended to the `path` to create a relative URL.
# If the `link` is not already in the `urls` queue and not in the `scraped_urls` set, it is added to the `urls` queue.
# After the `while` loop finishes or is interrupted by a keyboard interrupt (`KeyboardInterrupt` exception), a message is printed to indicate that the script is closing.
# Finally, the script prints all the email addresses found in the `emails` set.
