import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict

TOP_MOVIES_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

content = requests.get(url=TOP_MOVIES_URL)
content.raise_for_status()

soup = BeautifulSoup(content.text, "html.parser")
title_tags = soup.find_all(name='h3', class_='title')

titles = OrderedDict()
titles = {int(re.split('\W', title_tag.text)[0]): re.split('[0-9][):]', title_tag.text)[1] for title_tag in title_tags}
with open("movies.txt", "w") as fp:
    while len(titles):
        title = titles.popitem()
        fp.write(f"{title[0]} {title[1].strip()}\n")
