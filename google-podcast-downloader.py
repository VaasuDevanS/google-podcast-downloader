"""
Developer: Vaasudevan Srinivasan
Created on: Aug 25, 2022
Description: Script to download entire Podcast Library for the given url
Email: vaasuceg.96@gmail.com
Github: https://github.com/VaasuDevanS/google-podcast-downloader
"""

from bs4 import BeautifulSoup
import re
import requests
from tqdm import tqdm


# Specify the URL and the path where the episodes should be downloaded
url = r''
out_dir = r''


# Read the url and create soup object
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


# Get all the divs corresponding to each podcast episode
divs = soup.find_all('div', attrs={'class': 'oD3fme'})


# Iterate through each div (episode)
for ix, div in tqdm(enumerate(divs[::-1]), total=len(divs)):

    # Get the date published
    date = div.find('div', attrs={'class': 'OTz6ee'}).text

    # Get the name of the episode and remove invalid characters (Windows)
    name = div.find('div', attrs={'class': 'e3ZUqe'}).text
    name = re.sub('[\/:*?"<>|]+', '', name)
    
    # Get the URL
    url = div.find('div', attrs={'jsname': 'fvi9Ef'}).get('jsdata')
    url = url.split(';')[1]
    
    # Construct the File name
    file_name = f'EP {ix:03d} - {name} ({date})'
    
    # Fetch each episode and write the file
    podcast = requests.get(url)
    with open(rf'{out_dir}\{file_name}.mp3', 'wb') as out:
        out.write(podcast.content)    
