import requests
import time


url = "http://toxiproxy:22222"

tries = 0
while tries <= 5 and tries != -1:
    tries += 1
    try:
        r = requests.get(url=url, timeout=1)
        print(r.json())
        print(r.elapsed.total_seconds())
    except requests.exceptions.Timeout as timeout:
        print("Request timeout after 1s")
        print("Trying again after 30s")
        time.sleep(30)
        tries += 1
    except requests.exceptions.ConnectionError as notfound:
        print("Target api is down")
        tries = -1

