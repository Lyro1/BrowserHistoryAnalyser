import browserhistory as bh
import requests


def check_url(url):
    print("Testing " + url + "...")
    r = requests.post("https://urlhaus-api.abuse.ch/v1/" + url)
    if r.status_code == 404:
        return None
    else:
        print(r.json())
        return r.json()


if __name__ == '__main__':
    history = bh.get_browserhistory()
    for browser in history:
        for entry in history[browser]:
            check_url(entry[0])
    else:
        print("No browsers available")

