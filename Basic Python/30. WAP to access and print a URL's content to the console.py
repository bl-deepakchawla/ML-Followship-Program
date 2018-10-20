import urllib.request


def get_url_content(url):
    response = urllib.request.urlopen(url)
    return response.read()


url = "https://www.google.com"
results = get_url_content(url)
print("Content of requested url as follows: ", results)
