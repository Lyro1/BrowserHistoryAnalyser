import browserhistory as bh
import requests


def check_url(url):
    r = requests.post("https://urlhaus-api.abuse.ch/v1/" + url)
    print(r.json)


if __name__ == '__main__':
    history = bh.get_browserhistory()
    browsers = history.keys()
    if len(browsers) > 0:
        check_url(history[browsers[0]][0])
    else:
        print("No browsers available")

