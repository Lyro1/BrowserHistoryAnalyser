import browserhistory as bh
import requests



def check_url(current, total, url):
    r = requests.post("https://urlhaus-api.abuse.ch/v1/" + url)
    print(str(current) + '/' + str(total))

    if r.status_code == 404:
        return current + 1, None
    else:
        return current + 1, r.json()


if __name__ == '__main__':
    history = bh.get_browserhistory()
    total = 0
    for browser in history:
        total += len(history[browser])
    current = 1
    foundDanger = 0

    if total <= 0:
        print("No entry found.")

    for browser in history:
        for entry in history[browser]:
            current, json = check_url(current, total, entry[0])
            if json:
                foundDanger += 1
                print(json)

    print("Results: " + str(foundDanger) + " dangerous URLs found.")