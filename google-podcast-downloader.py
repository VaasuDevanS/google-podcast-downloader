#!/usr/bin/env python3
"""
Created: Aug 25, 2022
Last Modified: Sep 01, 2023
Description: Script to download entire Podcast Library for the given url
Github: https://github.com/VaasuDevanS/google-podcast-downloader
"""

import argparse
from pathlib import Path
import re
from bs4 import BeautifulSoup
import requests
import os
from tqdm import tqdm

def main(url: str, out_dir: Path) -> None:
    # Create directory if it doesn't exist
    out_dir.mkdir(parents=True, exist_ok=True)
    # Read the url and create soup object
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # Get all the divs corresponding to each podcast episode
    divs = soup.find_all("div", attrs={'class': 'oD3fme'})
    # Iterate through each div (episode)
    for ix, div in tqdm(enumerate(divs[::-1]), total=len(divs)):
        # Get the date published
        date = div.find("div", attrs={'class': 'OTz6ee'}).text
        # Get the name of the episode
        name = div.find("div", attrs={'class': 'e3ZUqe'}).text
        name = re.sub('[/:*?"<>|]+', '', name)
        file_name = f'EP {ix:03d} - {name} ({date}).mp3'
        episode_path = out_dir / file_name
        # If the episode is already downloaded, skip it.
        if os.path.exists(episode_path):
            pass
        # Get the URL
        url = div.find("div", attrs={"jsname": "fvi9Ef"}).get("jsdata")
        url = url.split(";")[1]
        # Download the episode
        podcast = requests.get(url)
        with open(rf"{episode_path}", "wb") as out:
            out.write(podcast.content)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Google Podcast Downloader',
        description='Script to download entire Podcast Library',
    )
    parser.add_argument('--url', help='URL of the podcast')
    parser.add_argument('--out-dir', help='Folder to download')
    args = parser.parse_args()
    main(url=args.url, out_dir=Path(args.out_dir))
