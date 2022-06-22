#!/usr/bin/python

import requests
import re
import sys
import argparse

parser = argparse.ArgumentParser(prog='PyCrawler', usage='%(prog)s -d/--domain [DOMAIN]', description='Python tool to pull links from any targeted website')
parser.add_argument('--domain','-d',type=str,help='Domain you want to pull links from',action='store',required=True)
parser.add_argument('--external','-e',help='If enabled, pull external links referenced on the website, by default this is set to false',default='false', action='store',type=str,required=False)
parser.add_argument('--output','-o',help='Write output to a file', action='store',default='',required=False)
args = parser.parse_args()


def get_links(url=args.domain,external_links=args.external,output=args.output):
    links_list = set()
    try:
    
        links_request = requests.get(url).text

    except:
        print('Cannot connect with server, exiting....')
        sys.exit()
    if external_links.lower() == 'false':
        links_re = r'<a href="({}/[\w\d\-&/#@\.]*)".*?>'.format(url)
    else:
         links_re = r'<a href="(http[s]*?://[\w\d\-&/#@\.]*)".*?>'
    
    links_find = re.findall(links_re,links_request)

    if links_find == []:
        print('No links found, exiting...')
        sys.exit()

    else:
    
        for each in links_find:
            links_list.add(each)
            crawl_request = requests.get(each).text
            crawl_find = re.findall(links_re,crawl_request)
            for each in crawl_find:
                links_list.add(each)

        if args.output != '':
            for each in sorted(links_list):
                file = open(args.output,"a+")
                file.write(each + '\n')
                file.close()
            print('Successfully wrote {} lines to {}.'.format(len(links_list),args.output))

        else:
            for each in sorted(links_list): 
                print(each)
            print('{} links found.'.format(len(links_list)))


if __name__ == '__main__':
    get_links()

