import requests
import zipfile
import os
import aiohttp
import asyncio
import time

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
]


async def processing_zip_file(download_url, session):
    async with session.get(download_url) as response:
        file_name = download_url.split("/")[-1]

        full_path = f"Exercises/Exercise-1/download/{file_name}"

        with open(full_path, "wb") as f:
            file_content = await response.read()

            f.write(file_content)

        zip_file = zipfile.ZipFile(full_path, "r")
        zip_file.extractall(f"Exercises/Exercise-1/download")
        zip_file.close()

        os.remove(full_path)


async def main_extra_credits(download_url):
    coros = []
    async with aiohttp.ClientSession() as session:
        for id_c in download_url:
            coros.append(processing_zip_file(id_c, session))

        await asyncio.gather(*coros)


def main_single_thread():
    for download_url in download_uris:
        response = requests.get(download_url)

        file_name = download_url.split("/")[-1]

        full_path = f"Exercises/Exercise-1/download/{file_name}"

        with open(full_path, "wb") as f:
            f.write(response.content)

        zip_file = zipfile.ZipFile(full_path, "r")
        zip_file.extractall(f"Exercises/Exercise-1/download")
        zip_file.close()

        os.remove(full_path)


if __name__ == "__main__":
    started = time.time()
    # main_single_thread()

    event_loop = asyncio.get_event_loop()

    event_loop.run_until_complete(main_extra_credits(download_uris))

    ended = time.time()

    print(f"Processo multithead:{ended - started}")
