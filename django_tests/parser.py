from bs4 import BeautifulSoup
import requests

url = "https://scipost.org/atom/publications/comp-ai"  # URL to XML
file = "parsed_rss.html" # output will be saved in this file
output = open(file, "w", encoding="utf-8")
out_soup = BeautifulSoup("<html> <meta charset='UTF-8'> </html>", 'html.parser')
response = requests.get(url)

if response.status_code == 200:
    xml_data = response.text
    in_soup = BeautifulSoup(xml_data, "xml")
    items = in_soup.find_all('entry')
    for item in items:
        html_link = item.find('link')['href']
        html_title = item.find('title').string
        html_date = item.find('updated').string
        new_tag = out_soup.new_tag('div')
        block_title = out_soup.new_tag('h1', string=html_title)
        new_tag.append(block_title)
        new_tag.append('Date :' + html_date)
        block_link = out_soup.new_tag('a', href=html_link, target='_blank', string=' Click here to read')
        new_tag.append(block_link)
        new_tag.append(out_soup.new_tag('br'))
        new_tag.append(out_soup.new_tag('hr'))  # horizontal line at the end of each section
        out_soup.html.append(new_tag)
else:
    print(f"Sorry, there was an error: {response.status_code}")
    print("while loading from "+url)

output.write(out_soup.prettify())
output.close()
