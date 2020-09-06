from urllib.request import urlopen

# Worth checking the robots.txt file of each website to check if they want to be scrapped
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')

# Get the title
title_index_start = html.find('<title>') + len('<title>')
title_index_end = html.find('</title>')
title_text = html[title_index_start:title_index_end]

print(title_text)