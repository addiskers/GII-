# toc_scraper/spiders/ccus_spider.py
import scrapy
from w3lib.html import remove_tags
import json

class DaSpider(scrapy.Spider):
    name = 'da'
    start_urls = ['https://www.marketsandmarkets.com/Market-Reports/industrial-sensor-market-108042398.html']

    def parse(self, response):
        # Select all relevant elements within the div
        content = response.css('div.tab-pane#tab_default_2').xpath('.//text()').getall()

        if content:
            # Clean and structure the content, removing HTML tags
            cleaned_content = [remove_tags(line).strip() for line in content]
            # Filter out empty lines and lines starting with 'figure' or 'table'
            structured_content = [line for line in cleaned_content if line and not line.lower().startswith(('figure', 'table'))]

            # Save the content to a JSON file
            with open('table_of_contents.json', 'w') as f:
                json.dump(structured_content, f, indent=4)
            self.log('Content saved to table_of_contents.json')

            # Print the content
            print("TABLE OF CONTENTS")
            for line in structured_content:
                print(line)
        else:
            self.log('Failed to retrieve content.')