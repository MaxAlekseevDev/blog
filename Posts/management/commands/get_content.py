from _thread import start_new_thread
import xml.etree.ElementTree as ET

from django.core.management.base import BaseCommand

import requests


class Command(BaseCommand):
    help = 'Get content from sitemap.xml'

    def get_urls_from_xml(self):
        xml_file = ET.parse("/home/dev-max/portfolio/NewBlog/Posts/management/commands/sitemap.xml")
        root = xml_file.getroot()
        urls = []
        for child in root:
            urls.append(child[0].text)
        return urls

    def generator_url(self, urls):
        for url in urls:
            url.strip()
            yield url
    
    def get_content(self, url):

        with requests.Session() as session:
            site = session.get(url)
            print(site)

    def handle(self, *args, **options):
        urls = self.get_urls_from_xml()
        start_new_thread(self.get_content, self.generator_url(urls))