import requests
import io
import gzip

URL_PATHS = "https://data.commoncrawl.org"

WET_PATHS = "crawl-data/CC-MAIN-2022-05/wet.paths.gz"


def main():
    print("requisiçao principal")
    r = requests.get(f"{URL_PATHS}/{WET_PATHS}")

    with io.BytesIO(r.content) as file_buffer:
        print("abrindo o gzip")
        with gzip.open(file_buffer, "r") as zip_file:
            print("lendo dados do gzip")
            file_content = zip_file.read()

    print("formatando dados dos arquivos")
    wet_paths = file_content.splitlines()

    print("fazendo requisiçao para baixar primeiro arquivo")
    r = requests.get(f"{URL_PATHS}/{wet_paths[0]}")
    content_file = r.content.decode("utf-8").splitlines()
    print(content_file[0])


if __name__ == "__main__":
    main()
