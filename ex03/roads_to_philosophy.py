import sys
import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
    except Exception:
        if res.status_code == 404:
            print("It leads to a dead end !")
            sys.exit()
        else:
            print("An error occured during a request.")
            raise
    else:
        return res.text


def search_redirection(soup, roads):
    redirection = soup.find("span", class_="mw-redirectedfrom")
    if redirection is not None:
        redirection_title = redirection.a.attrs["title"]
        print(redirection_title)
        roads.append(redirection_title)


def find_title(soup, roads):
    page_title = soup.find(id="firstHeading").text
    print(page_title)
    if page_title in roads:
        print("It leads to an infinite loop !")
        sys.exit()
    elif page_title == "Philosophy":
        print("{nb_roads} roads from {fst_road} to philosophy !".format(
            nb_roads=len(roads) + 1, fst_road=roads[0]
        ))
        sys.exit()
    roads.append(page_title)


def find_next_article(soup):
    content = soup.find(id="mw-content-text")
    for a in content.select("p > a"):
        href = a.attrs["href"]
        if href.startswith("/wiki/") and ":" not in href:
            url = "https://en.wikipedia.org" + href
            try:
                res = requests.get(url)
                res.raise_for_status()
            except Exception:
                if res.status_code == 404:
                    continue
                else:
                    print("An error occured during a request.")
                    raise
            else:
                return url
    return None


def loop(url, roads, first_try=False):
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    if first_try:
        search_redirection(soup, roads)
    find_title(soup, roads)
    next_url = find_next_article(soup)
    if next_url is not None:
        loop(next_url, roads)
    print("It leads to a dead end !")
    sys.exit()


def main():
    roads = []
    args = sys.argv[1:]
    if not len(args) == 1:
        raise Exception("The program takes one parameter.")
    request_name = args[0].strip().replace(" ", "_")
    url = "https://en.wikipedia.org/wiki/" + request_name
    loop(url, roads, True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
