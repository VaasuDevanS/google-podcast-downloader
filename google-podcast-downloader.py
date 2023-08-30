#!/usr/bin/env python3
"""
Developer: Vaasudevan Srinivasan
Created on: Aug 25, 2022
Description: Script to download entire Podcast Library for the given url
Email: vaasuceg.96@gmail.com
Github: https://github.com/VaasuDevanS/google-podcast-downloader
Pull Request by: Hirschy Kirkwood
Date Submitted: 08/29/23
"""

from bs4 import BeautifulSoup
import re
import requests
from tqdm import tqdm
import os
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    print("URL:", url)
    out_dir = sys.argv[2]
    print("Out Dir:", out_dir)
elif len(sys.argv) == 2:
    out_dir = r""  # fill in the directory to put your files into.
else:
    url = r""  # Fill in your URL here if you don't want to pass cli args.
    out_dir = r""  # fill in the directory to put your files into.


class NotEnoughParams(Exception):
    def __init__(self, message):
        self.message = message


def check_input(out_dir, url):
    if "~" in out_dir:
        out_dir = os.path.expanduser(out_dir)

    if not os.path.exists(out_dir):
        try:
            os.makedirs(out_dir)
        except Exception as e:
            raise ValueError(f"Invalid path: {out_dir}")
    return out_dir


if __name__ == "__main__":
    if not out_dir or not url:
        raise NotEnoughParams("Please provide both a URL and an output directory.")
    out_dir = check_input(out_dir, url)

    # Read the url and create soup object
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # Get all the divs corresponding to each podcast episode
    divs = soup.find_all("div", attrs={"class": "oD3fme"})

    # Iterate through each div (episode)
    for ix, div in tqdm(enumerate(divs[::-1]), total=len(divs)):
        # Get the date published
        date = div.find("div", attrs={"class": "OTz6ee"}).text
        # Get the name of the episode
        name = div.find("div", attrs={"class": "e3ZUqe"}).text
        name = re.sub('[\/:*?"<>|]+', "", name)
        file_name = f"EP {ix:03d} - {name} ({date}).mp3"

        episode_path = os.path.join(out_dir, file_name)
        if os.path.exists(episode_path):
            pass  # This file already exists...
        # Fetch each episode and write the file
        podcast = requests.get(url)

        # Get the URL
        url = div.find("div", attrs={"jsname": "fvi9Ef"}).get("jsdata")
        url = url.split(";")[1]

        # Construct the File name

        with open(rf"{episode_path}", "wb") as out:
            out.write(podcast.content)
