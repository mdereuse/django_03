import sys
import requests
from bs4 import BeautifulSoup


def main():
    roads = []
    args = sys.argv[1:]
    if not len(args) == 1:
        raise Exception("The program takes one parameter.")
    request_name = args[0].strip().replace(" ", "_")
    url = "https://en.wikipedia.org/wiki/" + request_name
    try:
        res = requests.get(url)
        res.raise_for_status()
    except Exception:
        if res.status_code == 404:
            print("It's a dead end !")
            sys.exit()
        else:
            print("An error occured during the request.")
            raise
    text = res.text
    soup = BeautifulSoup(text, "html.parser")
    redirection = soup.find("span", class_="mw-redirectedfrom")
    if redirection is not None:
        redirection_title = redirection.a.attrs["title"]
        print(redirection_title)
        roads.append(redirection_title)
    page_title = soup.find(id="firstHeading").text
    print(page_title)
    if page_title in roads:
        print("It's a loop.")
        sys.exit()
    elif page_title == "Philosophy":
        print("Win")
        sys.exit()
    roads.append(page_title)
    content = soup.find(id="mw-content-text")
    for a in content.select("p > a"):
#    for a in content.find_all("a"):
        href = a.attrs["href"]
        if href.startswith("/wiki/") and ":" not in href:
            print(href)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
