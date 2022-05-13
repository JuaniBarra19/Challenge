from scrapy.crawler import CrawlerProcess
import scrapy

class Spider(scrapy.Spider):
    name = 'dolar'
    start_urls = [
        'https://dolarhoy.com/'
    ]
    custom_settings = {
        'FEED_URI': 'dolar_hoy.csv',
        'FEED_FORMAT': 'csv',
        'FEED_EXPORT_ENCODING': 'utf-8'
        
    }

    def parse(self,response):
        links = response.xpath("//div[@class='tile is-parent is-7 is-vertical']//a/@href").getall()

        for link in links:
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        
        nombre = response.xpath('//div[@class="tile is-child title"]/text()').get()
        compra = response.xpath('//*[@id="sitio"]/section/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/text()').get() 
        venta = response.xpath('//*[@id="sitio"]/section/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/text()').get()  
        fecha = response.xpath('//div[@class="tile is-child"]/span/text()').get()
        
        yield {
            'title': nombre, 
            'Compra':compra, 
            'Venta':venta, 
            'Fecha':fecha,
            'url': link
        }

process = CrawlerProcess()
process.crawl(Spider)
process.start()
        