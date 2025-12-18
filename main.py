import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
import threading

all_links = []
downloaded = []
broken = []
active_links = {}
net_issue_start = None
site_issue_start = None

def has_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.RequestException:
        return False

def site_available(url=None):
    if not url:
        url = "https://web-api.varzesh3.com/v1.0/news/most-visited?includeSports[0]=Football&includeSports[1]=Futsal&includeSports[2]=BeachSoccer"
    try:
        requests.get(url, timeout=5)
        return True
    except requests.RequestException:
        return False

def fetch_links():
    response = requests.get(
        'https://web-api.varzesh3.com/v1.0/news/most-visited?includeSports[0]=Football&includeSports[1]=Futsal&includeSports[2]=BeachSoccer'
    )
    for item in response.json():
        link = item["link"]
        if link not in all_links and link not in downloaded and link not in broken:
            all_links.append(link)

    with open("links.txt", "w", encoding="utf-8") as file:
        file.writelines(f"{lnk}\n" for lnk in all_links)

def download_image(url):
    active_links[url] = 0
    print(url)
    soup = BeautifulSoup(requests.get(url).content, "lxml")
    dom = etree.HTML(str(soup))
    img_list = dom.xpath('/html/body/div/div[1]/div/div/div[2]/div[2]/div[2]/div/img/@src')
    print(img_list)

    if not img_list:
        active_links[url] += 1
        for _ in range(5):
            if active_links[url] != 5:
                img_list = dom.xpath('/html/body/div/div[1]/div/div/div[2]/div[3]/div[2]/div/img/@src')
                if img_list:
                    img = img_list[0]
                    name = img.strip().split("/")[-1].split(".")[0]
                    print(name)
                    del active_links[url]
                    downloaded.append(url)
                    return
                else:
                    active_links[url] += 1
            else:
                broken.append(url)
                with open("broken_links.txt", "w", encoding="utf-8") as f:
                    f.writelines(f"{lnk}\n" for lnk in broken)
                print("Link is broken")
    else:
        img = img_list[0]
        name = img.strip().split("/")[-1].split(".")[0]
        print(name)
        del active_links[url]
        downloaded.append(url)
        print(downloaded)
        with open(f"images/{name}.jpg", "wb") as f_img:
            f_img.write(requests.get(img).content)
        with open("image.txt", "a", encoding="utf-8") as f_txt:
            f_txt.write(f"{img}\n")
        with open("downloaded_links.txt", "w", encoding="utf-8") as f_dl:
            f_dl.writelines(f"{lnk}\n" for lnk in downloaded)


start_time = time.time()
download_timer = 0
last_fetch_time = time.time()
fetch_timer = 0
thread_counter = 0
download_counter = 0
link_index = 0

with open("links.txt", "w", encoding="utf-8") as f:
    f.writelines(f"{lnk}\n" for lnk in all_links)

while True:
    if not has_internet():
        if net_issue_start is None:
            net_issue_start = time.time()
            print("Internet lost — waiting...")
        elif time.time() - net_issue_start < 120:
            time.sleep(5)
            continue
        else:
            print("Still no internet — retrying...")
            net_issue_start = time.time()
            continue
    else:
        if net_issue_start is not None:
            print("Internet restored, resuming...")
            net_issue_start = None

    if not site_available():
        if site_issue_start is None:
            site_issue_start = time.time()
            print("Website unreachable — waiting...")
        elif time.time() - site_issue_start < 300:
            print("Website still unreachable — retrying soon.")
            time.sleep(5)
            continue
        else:
            print("Website unreachable — restarting wait timer.")
            site_issue_start = time.time()
            continue
    else:
        if site_issue_start is not None:
            print("Website reachable again, resuming...")
            site_issue_start = None

    now = time.time()
    elapsed_fetch = now - last_fetch_time
    elapsed_download = now - start_time
    last_fetch_time = now
    start_time = now
    fetch_timer += elapsed_fetch
    download_timer += elapsed_download

    if download_timer > 120:
        fetch_threads = [t for t in threading.enumerate() if t.name.startswith("get-links")]
        if len(fetch_threads) < 3:
            t_fetch = threading.Thread(target=fetch_links, name=f"get-links{thread_counter}")
            t_fetch.start()
            download_timer = 0
            thread_counter += 1

            if all_links and fetch_timer > 30:
                dl_threads = [t for t in threading.enumerate() if t.name.startswith("download-image")]
                if len(dl_threads) < 5 and link_index < len(all_links):
                    t_dl = threading.Thread(target=download_image, args=(all_links[link_index],), name=f"download-image{download_counter}")
                    t_dl.start()
                    fetch_timer = 0
                    download_counter += 1
                    link_index += 1
