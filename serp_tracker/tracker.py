from send_email import send_email
from data import api_key, load_keywords
import requests

SERP_API = api_key()

KEYWORDS = load_keywords()

IDENTIFIER = "motadata.com"


def main():
    for key in KEYWORDS:
        tracker(key.strip())


def tracker(keyword):
    params = {
        'access_key': SERP_API,
        'query': keyword,
        "num": 100
    }

    api_response = requests.get(
        'http://api.serpstack.com/search', params=params).json()

    for obj in api_response['organic_results']:

        try:
            position = obj['position']
            url = obj['url']
            if IDENTIFIER not in url:
                raise Exception
        except:
            continue
        else:
            send_email(keyword, position, url)
            break


if __name__ == "__main__":
    main()
