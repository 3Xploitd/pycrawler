
import requests
import re
import sys


if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    print('SyntaxError: Usage ./pycrawler.py <http(s)://domain.com>')
    sys.exit()
def get_links(url):
    links_list = set()
    links_request = requests.get(url).text
    links_find = re.findall(r'<a href="([https://|http://|\/]+?[\w\d\-&/#@\.]*)".*?>',links_request)
    for each in links_find:
        links_list.add(each)
        crawl_request = requests.get(each).text
        crawl_find = re.findall(r'<a href="([https://|http://|\/]+?[\w\d\-&/#@\.]*)".*?>',crawl_request)
        for each in crawl_find:
            links_list.add(each)
    for each in links_list:
        print(each)
    print(len(links_list))

if __name__ == '__main__':
    get_links(url)
            
