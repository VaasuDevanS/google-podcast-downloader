# Google Podcast Downloader

## Instructions
1. Clone this Repository
2. The script depends on `requests`, `beautifulsoup`, `tqdm` and `re`. See `requirements.txt` to create a new conda environment or you can install these packages directly using `pip install requests beautifulsoup4 tqdm` in your desired environment
3. Set the `url` to the podcast and `out_dir` within the script ([lines 16-17](https://github.com/VaasuDevanS/google-podcast-downloader/blob/c09068092d8807a61fe860ad290517303ceead3e/google-podcast-downloader.py#L16-L17))
4. Run the script using `python google-podcast-downloader.py`
5. [Optional] You can change the file name template in [line 44](https://github.com/VaasuDevanS/google-podcast-downloader/blob/c09068092d8807a61fe860ad290517303ceead3e/google-podcast-downloader.py#L44). The default template is `Ep 000 - <Podcast-Name> (<Date-Published>)`


## Tested Podcasts

I personally used the script to download the below podcasts for offline listening.

<a href="https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5tZWdhcGhvbmUuZm0vTExMNTQ0OTY4NTMxNA"><img src="https://user-images.githubusercontent.com/24793046/186712377-ee4ef1c3-29b6-4536-8141-5b347c39af03.png" width=250 height=250></a>
<a href="https://podcasts.google.com/feed/aHR0cHM6Ly9yZWFscGVyc29uYWxmaW5hbmNlLmxpYnN5bi5jb20vcnNz"><img src="https://user-images.githubusercontent.com/24793046/186715257-fd960d3a-7180-4cd9-bd7d-0ca04d1f68f5.png" width=250 height=250></a>
<a href="https://podcasts.google.com/feed/aHR0cHM6Ly90YWxrcHl0aG9uLmZtL2VwaXNvZGVzL3Jzcw"><img src="https://user-images.githubusercontent.com/24793046/188334448-f50171b9-8501-426e-83f7-553feb376369.png" width=250 height=250></a>


## Contributions
If you like this work, give a ⭐  
All Contributions and Pull Requests are Welcome
