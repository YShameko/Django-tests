from bs4 import BeautifulSoup
import requests
from lxml.html.defs import link_attrs

url = "https://life.pravda.com.ua/rss/"  # URL to XML
file = "parsed_rss.html" # output will be saved in this file
output = open(file, "w", encoding="utf-8")
out_soup = BeautifulSoup("<html> <meta charset='UTF-8'> </html>", 'html.parser')
response = requests.get(url)

if response.status_code == 200:
    xml_data = response.text
    in_soup = BeautifulSoup(xml_data, "xml")
    items = in_soup.find_all('item')
    for item in items:
        html_link = item.find('link').string
        html_title = item.find('title').string
        html_date = item.find('pubDate').string
        html_photo = item.find('media:content')['url']
        photo_link = html_photo[:html_photo.find('?')]
        new_tag = out_soup.new_tag('section')
        block_title = out_soup.new_tag('a', href=html_link, string=html_title)
        new_tag.append(block_title)
        new_tag.append(out_soup.new_tag('br'))
        new_tag.append('Date: ' + html_date)
        new_tag.append(out_soup.new_tag('br'))
        image_tag = out_soup.new_tag('img', src=photo_link)
        new_tag.append(image_tag)
        new_tag.append(out_soup.new_tag('hr')) # horizontal line at the end of each section
        out_soup.html.append(new_tag)
else:
    print(f"There was an error: {response.status_code}")
    print("while loading from "+url)

output.write(out_soup.prettify())
output.close()