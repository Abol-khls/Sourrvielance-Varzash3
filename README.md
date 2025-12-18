# Sourrvielance



This little script quietly polls the Varzesh3 "most visited" news API and saves the article links it finds into `links.txt`.


**What this repo contains**

- `1.py`: the small Python script that fetches the API and writes links.

- `links.txt`: created by the script; contains one URL per line.



**What it does**

- Every 120 seconds the script requests the "most visited" endpoint from Varzesh3.

- Collected links are saved to `links.txt` in UTF‑8 format.



**Optional but recommended**

1. Make a virtual environment and activate it.

## Installation


# Varzesh3 News Image Scraper

A Python script that automatically fetches the most-visited news links from the Varzesh3 website, downloads their main images, and keeps track of working and broken links.

---

## Features

- **Fetches latest news links** from Varzesh3's public API and stores them in `all_links`.
- **Downloads main images** from each news article and tracks them in `downloaded`.
- **Saves all found links** to `links.txt`.
- **Saves all downloaded image URLs** to `image.txt`.
- **Tracks which links have been downloaded in `downloaded_links.txt`.**
- **Tracks broken links** in `broken` and writes them to `broken_links.txt`.
- **Handles network and site outages** gracefully, using `net_issue_start` and `site_issue_start` for retry logic.
- **Multi-threaded**: Downloads images and fetches links in parallel for efficiency, using `active_links` to manage concurrent tasks.

---

## How It Works

1. The script regularly checks for internet and site availability, using `net_issue_start` and `site_issue_start` to manage downtime.
2. Every 2 minutes, it fetches the latest news links from Varzesh3's API and stores them in the `all_links` list, writing to `links.txt`.
3. For each new link, it tries to download the main image from the article page. Successfully downloaded images are tracked in `downloaded` and written to `downloaded_links.txt`.
4. Downloaded images are saved locally in the `images/` folder, and their URLs are logged in `image.txt`.
5. Broken or unreachable links are tracked in the `broken` list and written to `broken_links.txt` for review.
6. The script is robust against network and site outages, automatically retrying as needed.
7. Multi-threading is used to speed up both link fetching and image downloading, with `active_links` managing concurrent downloads.

---

## File Overview

- `1.py` — Main Python script for scraping and downloading images.
- `links.txt` — List of all news article links found (one per line).
- `image.txt` — URLs of images successfully downloaded.
- `downloaded_links.txt` — Links that have been successfully downloaded.
- `broken_links.txt` — Links that could not be processed or had no image.
- `images/` — Folder containing all downloaded images.

---

## Requirements

- Python 3.7 or higher
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [lxml](https://pypi.org/project/lxml/)
## Table of Contents

- [Sourrvielance](#sourrvielance)
  - [Installation](#installation)
- [Varzesh3 News Image Scraper](#varzesh3-news-image-scraper)
  - [Features](#features)
  - [How It Works](#how-it-works)
  - [File Overview](#file-overview)
  - [Requirements](#requirements)
  - [Table of Contents](#table-of-contents)
  - [Motivation \& Background](#motivation--background)
    - [Script Architecture](#script-architecture)
    - [API Information](#api-information)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Create and Activate a Virtual Environment](#2-create-and-activate-a-virtual-environment)
    - [3. Install Required Packages](#3-install-required-packages)
    - [4. Create the `images` Folder (if it doesn't exist)](#4-create-the-images-folder-if-it-doesnt-exist)
    - [5. Run the Script](#5-run-the-script)
    - [6. Check the Output Files](#6-check-the-output-files)
  - [Customization](#customization)
  - [FAQ](#faq)
  - [Contributing](#contributing)
  - [Troubleshooting](#troubleshooting)
  - [Contact](#contact)
  - [Notes](#notes)
  - [License](#license)

---

## Motivation & Background

Varzesh3 is one of the most popular sports news websites in Iran, providing up-to-date news, images, and articles. This project was created to automate the process of collecting the latest news article links and their main images for research, archiving, or personal use. It is especially useful for:

- Building datasets for machine learning or NLP projects
- Monitoring trending sports news
- Archiving news and images for offline analysis

**Note:** This project is not affiliated with Varzesh3 and is intended for educational and personal use only.

---

2. **(Recommended) Create and activate a virtual environment:**
    ```sh
    python -m venv .venv
    .venv\Scripts\activate
    ```
1. The script regularly checks for internet and site availability.
2. Every 2 minutes, it fetches the latest news links from Varzesh3's API.
3. For each new link, it tries to download the main image from the article page using XPath and BeautifulSoup.
4. Downloaded images are saved locally in the `images/` folder, and their URLs are logged in `image.txt`.
5. Broken or unreachable links are recorded in `broken_links.txt` for review.
6. The script is robust against network and site outages, automatically retrying as needed.
7. Multi-threading is used to speed up both link fetching and image downloading.

### Script Architecture

- **Network & Site Check:** Ensures both internet and Varzesh3 API are reachable before proceeding.
- **Link Fetcher:** Periodically polls the API for new article links.
- **Image Downloader:** For each link, parses the page and downloads the main image if available.
- **Logging:** Maintains logs of all links, images, and broken links for transparency and debugging.

### API Information

- The script uses Varzesh3's public API for fetching the most-visited news articles.
- The API returns a JSON array of news items, each containing a `link` field.

---
4. **Create an `images` folder** (if it doesn't exist):
    ```sh
    mkdir images
### 1. Clone the Repository

Run the following command in your terminal (Windows, macOS, or Linux):

```sh
git clone https://github.com/Abol-khls/Sourrvielance-Varzash3.git
cd Get-Links-Frome-Varzash3
```

### 2. Create and Activate a Virtual Environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Required Packages

**Install all dependencies using `requirements.txt`:**

If you do not have a `requirements.txt` file, generate it after installing the needed packages (e.g., `requests`, `beautifulsoup4`, `lxml`) with:

```sh
pip freeze > requirements.txt
```

Then, to install all dependencies at once:

**Windows:**

```powershell
pip install -r requirements.txt
```

**macOS/Linux:**

```bash
pip3 install -r requirements.txt
```

### 4. Create the `images` Folder (if it doesn't exist)

**Windows:**

```powershell
mkdir images
```

**macOS/Linux:**

```bash
mkdir -p images
```

### 5. Run the Script

**Windows:**

```powershell
python 1.py
```

**macOS/Linux:**

```bash
python3 1.py
```

### 6. Check the Output Files

- `links.txt`: All news article links found.
- `image.txt`: URLs of images downloaded.
- `downloaded_links.txt`: Links that have been successfully downloaded.
- `broken_links.txt`: Links that could not be processed.
- `images/`: Folder containing downloaded images.

---

## Customization

- **Change Fetch Interval:**
  - Edit the timing logic in `1.py` (variables like `fetch_timer`, `download_timer`) to adjust how often the script fetches new links or downloads images.
- **Add More Sports:**
  - Modify the API URL in the `site_available` or `fetch_links` function to include other sports or categories.
- **Change Image XPath:**
  - If Varzesh3 changes its site structure, update the XPath in `grab_image()` to match the new image location.
- **Output Folder:**
  - Change the `images/` folder path in the script if you want images saved elsewhere.

---
- Downloaded images will appear in the `images/` folder, named after their article ID.


- **Dependencies not found:**
    - Double-check that you installed all required packages: `requests`, `beautifulsoup4`, `lxml`.
- **Permission errors:**
    - Make sure you have write access to the project directory and the `images/` folder.
- **API changes:**
    - If the script stops working, check if Varzesh3 has changed their API or site structure. You may need to update the API URL or XPath in the script.

---

## FAQ

**Q: Can I use this script for commercial purposes?**
A: No. This script is for educational and personal use only. Please respect Varzesh3's terms of service.

**Q: How do I add support for more sports or categories?**
A: Edit the API URL in the script to include additional sports or parameters as needed.

**Q: The script is slow. Can I make it faster?**
A: You can increase the number of threads for image downloading, but be careful not to overload the site or your own system.

**Q: How do I run this on Linux or macOS?**
A: The script is cross-platform. Just adjust the virtual environment activation command and folder paths as needed.

---

## Contributing

Contributions, bug reports, and suggestions are welcome! To contribute:

1. Fork the repository
2. Create a new branch for your feature or fix
3. Submit a pull request with a clear description of your changes

---

## Troubleshooting


- This project is not affiliated with or endorsed by Varzesh3.
- Use responsibly and do not abuse the API or website.
- For research, archiving, or personal projects only.

---

## Contact

For questions, feedback, or collaboration, please contact:

- **GitHub:** [Abol-khls](https://github.com/Abol-khls)
- **Email:** (abolfazldehghanpoorr@gmail,com)
    - Make sure the `images/` folder exists and is writable.
    - Check your internet connection.
    - The Varzesh3 site structure may have changed; inspect the XPath in the script if needed.
- **Script crashes or hangs:**
    - Ensure all dependencies are installed.
    - Try running the script in a fresh virtual environment.
- **Too many broken links:**
    - The articles may not have images, or the site structure/API may have changed.

---

## Notes

- Use this script responsibly and respect Varzesh3's terms of service.
- The script is for educational and personal use only.
- Frequent requests may be blocked by the site; adjust the interval if needed.

---

## License

MIT License


