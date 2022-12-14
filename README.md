# Google Podcast Downloader

## Instructions
1. Clone this Repository
2. The script depends on `requests`, `beautifulsoup`, `tqdm` and `re`. See `requirements.txt` to create a new conda environment or you can install these packages directly using `pip install requests beautifulsoup4 tqdm` in your desired environment
3. Set the `url` to the podcast and `out_dir` within the script ([lines 16-17](https://github.com/VaasuDevanS/google-podcast-downloader/blob/c09068092d8807a61fe860ad290517303ceead3e/google-podcast-downloader.py#L16-L17))
4. Run the script using `python google-podcast-downloader.py`
5. [Optional] You can change the file name template in [line 44](https://github.com/VaasuDevanS/google-podcast-downloader/blob/c09068092d8807a61fe860ad290517303ceead3e/google-podcast-downloader.py#L44). The default template is `Ep 000 - <Podcast-Name> (<Date-Published>)`


## Tested Podcasts

I personally used the script to download the below podcasts for offline listening.

<a href="https://podcasts.google.com/feed/aHR0cHM6Ly93d3cub21ueWNvbnRlbnQuY29tL2QvcGxheWxpc3QvZDc1ZDJmZjQtYTRkZC00YTE5LWJjYjEtYWQzNTAxM2RmYzgzLzMzYTllNzBmLTU1YjEtNGY3OS04NmE5LWFkMzUwMTNlOTY3Mi80YWQwYThiYy1mNWRkLTRjNjMtYjZhZi1hZDM1MDEzZTk2ODAvcG9kY2FzdC5yc3M"><img src="https://user-images.githubusercontent.com/24793046/190875668-eebc55cc-e6d5-4a2f-b1b2-7856e78877a6.png" width=250 height=250></a> <br>
<a href="https://podcasts.google.com/feed/aHR0cHM6Ly90YWxrcHl0aG9uLmZtL2VwaXNvZGVzL3Jzcw"><img src="https://user-images.githubusercontent.com/24793046/188334448-f50171b9-8501-426e-83f7-553feb376369.png" width=250 height=250></a> 
<a href="https://podcasts.google.com/feed/aHR0cHM6Ly9tYXBzY2FwaW5nLnBvZGJlYW4uY29tL2ZlZWQueG1s"><img src="https://user-images.githubusercontent.com/24793046/188515031-1c71a2a1-331d-4dec-aafb-34f53f1aa47d.png" width=250 height=250></a><br>
<a href="https://podcasts.google.com/feed/aHR0cHM6Ly9yZWFscHl0aG9uLmNvbS9wb2RjYXN0cy9ycHAvZmVlZA=="><img src="https://user-images.githubusercontent.com/24793046/188514673-8eaa6c57-338a-46fe-8ae8-160718bb4900.png" width=250 height=250></a>
<a href="https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5tZWdhcGhvbmUuZm0vTExMNTQ0OTY4NTMxNA"><img src="https://user-images.githubusercontent.com/24793046/186712377-ee4ef1c3-29b6-4536-8141-5b347c39af03.png" width=250 height=250></a>


## Contributions
If you like this work, give a ???  
All Contributions and Pull Requests are Welcome
