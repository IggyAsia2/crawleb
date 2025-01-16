# scrapy_quotes/scrapy_quotes/spiders/quotes.py
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['gantzvn.com']
    # start_urls = ['https://manhwa18.net/manga/runner-s-high/chap-01-1166']

    # def parse(self, response):
    #     img_url = response.xpath("//*[@id='chapter-content']").css("img").xpath("@data-src").getall()
    #     for url in img_url:
    #         yield {'url': url} 
        
    #     next_page_url = response.xpath("//*[@id='app']/main/div[2]/div[5]/a[4]").xpath("@href").extract_first()
    #     if next_page_url is not None:
    #         yield scrapy.Request(response.urljoin(next_page_url))
    
    start_urls = ['https://gantzvn.com/truyen/gigant/chap-17}/']

    def parse(self, response):
        count = 17
        img_url = response.css("div.reading-content").css("div > img").xpath("@data-src").getall()
        for url in img_url:
            yield {'url': url.strip()} 
        next_page_url = f'https://gantzvn.com/truyen/gigant/chap-{count}/'
        if next_page_url is not None:
            count = count + 1
            yield scrapy.Request(response.urljoin(next_page_url))