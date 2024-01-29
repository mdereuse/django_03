import sys
import requests
import json
import dewiki


def main():
    url = "https://en.wikipedia.org/w/api.php"
    args = sys.argv[1:]
    if len(args) != 1:
        raise Exception("The program takes one argument.")
    name_request = args[0].strip().replace(" ", "_")
    params = {
        "action": "parse",
        "page": name_request,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }
    try:
        res = requests.get(url=url, params=params)
        res.raise_for_status()
    except Exception:
        print("An error has occured during the request to the API.")
        raise
    try:
        res_json = json.loads(res.text)
    except Exception:
        print("An error has occured during the json decoding.")
        raise
    if "error" in res_json.keys():
        raise Exception(
            res_json["error"]["info"]
        )
    res_txt = dewiki.from_string(res_json["parse"]["wikitext"]["*"])
    filename = name_request + ".wiki"
    try:
        with open(filename, "w") as f:
            f.write(res_txt)
    except Exception:
        print("An error has occured during the file writing.")
        raise


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
