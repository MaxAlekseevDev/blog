from django.core.management.base import BaseCommand

import requests

class Command(BaseCommand):
    help = 'Get content from url'


    def add_arguments(self, url):
        url.add_argument('url', nargs='+', type=str)

    def handle(self, *args, **options):
        print(options['url'])