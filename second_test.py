from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode('utf-8')

title_pattern = "<title.*?>.*?</title.*?>"
match_result = re.search(title_pattern, html, re.IGNORECASE)
title_text = match_result.group()
title_text = re.sub("<.*?>", "", title_text)

print("Page title:", title_text)

for string in ["Name:", "Favorite Color:"]:
    start_index = html.find(string) + len(string)
    end_index = html[start_index:].find('<')
    end_index = start_index + end_index
    print(string, html[start_index:end_index])