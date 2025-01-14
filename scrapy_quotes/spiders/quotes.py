# scrapy_quotes/scrapy_quotes/spiders/quotes.py
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['manhwa18.net']
    start_urls = ['https://manhwa18.net/manga/runner-s-high/chap-01-1166']

    def parse(self, response):
        yield {
            'src': response.xpath("//*[@id='chapter-content']").css("img").xpath("@data-src").getall(),
        }
        next_page_url = response.xpath("//*[@id='app']/main/div[2]/div[5]/a[4]").xpath("@href").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(next_page_url)