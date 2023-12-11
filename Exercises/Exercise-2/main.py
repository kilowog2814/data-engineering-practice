import requests
import pandas as pd
from bs4 import BeautifulSoup

URL_ENDPOINT = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021"


def main():
    r = requests.get(URL_ENDPOINT)
    soup = BeautifulSoup(r.text, "html.parser")

    for tr in soup.find_all("tr"):
        if "2022-02-07 14:03" in tr.text:
            for a in tr.find_all("a", href=True):
                r = requests.get(f"{URL_ENDPOINT}/{a['href']}")
                with open(a["href"], "wb") as f:
                    file_content = r.content
                    f.write(file_content)
                    # df = pd.read(file_content)


if __name__ == "__main__":
    main()
