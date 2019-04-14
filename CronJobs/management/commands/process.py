import os

import schedule
import time
from django.core.management import BaseCommand
from selenium.webdriver.chrome.options import Options

from crawler.managers.baseurl_manager import BaseUrlManager
from crawler.managers.images_manager import ImagesManager
from crawler.utils.base_url_status import BaseUrlStatus
from selenium.webdriver import Chrome


class Command(BaseCommand):
    help = 'Crawls the urls to the specific depth and stores the image urls'
    visited = {}

    def handle(self, *args, **options):
        self.start()
        schedule.every(2).minutes.do(self.start)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def process(self, url, depth, data):
        print("processing ", url, "at depth ",depth)

        if depth == 0 or not url:
            return

        if url in self.visited:
            return
        self.visited[url] = True

        options = Options()
        options.add_argument('headless')
        driver = Chrome(chrome_options=options)

        driver.get(url)

        domain = url.split("://")[1].split("/")[0]
        print("domain" , domain)
        links_xpath = "//a[@href]"
        images_xpath = "//img[@src]"
        links = driver.find_elements_by_xpath(links_xpath)
        images = driver.find_elements_by_xpath(images_xpath)

        for image in images:
            image_url = image.get_attribute('src')
            if image_url.startswith('http'):
                ImagesManager.add_url(image_url, data)


        for link in links:
            next_url = link.get_attribute('href')
            if domain in next_url and depth-1 >= 1:
                self.process(next_url, depth-1, data)




    def start(self):
        print('I run every 2 minutes.. keep watching..')
        try:
            data = BaseUrlManager.get_url_to_process()
            if not data:
                return
            self.process(data.base_url, data.depth, data)
            data.status = BaseUrlStatus.processed
            data.save()
        except Exception as e:
            print(str(e))