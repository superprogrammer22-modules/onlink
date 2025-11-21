# ONLINK: Operational Network Linkage Interface Navigator Kit

[![PyPI Version](https://img.shields.io/pypi/v/search.svg)](https://pypi.org/project/onlink/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**onlink** is a powerful Python utility module designed to simplify common networking, search, and web-scraping tasks. Following the "simplify one thing" philosophy, search abstracts away the complexity of managing HTTP requests, parsing responses, handling errors, and integrating search APIs, making external data retrieval clean and Pythonic.

---

## 🌟 Features

* **Simplified HTTP:** One-line functions for fetching webpage content.
* **Intelligent Search:** Seamless integration with DuckDuckGo Search (DDGS) for text and image results.
* **Clean Parsing:** Extracts clean, readable text from complex HTML pages.
* **Image Handling:** Loads and displays web images directly using OpenCV, perfect for quick visualization and testing.
* **Robust Input:** Automatically cleans and sanitizes URLs and handles common errors internally.

---

## 📥 Installation

**Install the package using pip:**

```bash
# Standard installation command
pip install onlink

```

---

## 🚀 Quick Start Example

Retrieve the top 3 search results for a query, then read the content of the first result, and finally display images from a secondary search.

```python

import onlink as net

# 1. Perform a Search
search_urls = net.Search('latest python utility modules', results=3)
print("--- Search Results ---")
for i, url in enumerate(search_urls):
    print(f"{i+1}. {url}")

# 2. Read Clean Text from the first result (requires a valid URL)
if search_urls:
    first_url = search_urls[0]
    print(f"\n--- Reading Text from: {first_url} ---")
    readable_text = net.Read(first_url)
    print(readable_text[:500] + "...") # Print first 500 characters of the wrapped text

# 3. Display Images (requires OpenCV windows to close to continue)
print("\n--- Displaying Images for 'Python Logo' ---")
image_urls = net.Image('Python Logo', results=2)
# The net.Show() function handles loading the URLs and displaying the OpenCV windows.
net.Show(image_urls, size='640x480') 

print("\nFinished example.")

```
