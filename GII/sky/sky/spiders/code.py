import scrapy
class CodeSpider(scrapy.Spider):
    name = "code"
    allowed_domains = ["skyquestt.com"]

    def start_requests(self):
        urls = ['https://www.skyquestt.com/report/automotive-wiring-harness-market']

        for url in urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={
                    "zyte_api_automap": {
                        "browserHtml": True,
                    }
                }
            )
            
    def parse(self, response):
        page_html = response.text
        
        with open("full_page.html", "w", encoding='utf-8') as f:
            f.write(page_html)

        self.log("Full page HTML saved to 'full_page.html'.")
