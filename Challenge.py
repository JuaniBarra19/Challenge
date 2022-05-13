import scrapy  
import pandas as pd 
from scrapy.crawler import CrawlerProcess



XPATH_NAMES = "//div[@class='tile is-parent is-7 is-vertical']//a[@class='title']/text()"
XPATH_COMPRA = "//div[@class='tile is-parent is-7 is-vertical']//div[@class='compra']//div[@class='val']/text()" 
XPATH_VENTA = "//div[@class='tile is-parent is-7 is-vertical']//div[@class='venta']//div[@class='val']/text()"  
XPATH_FECHA = "//div[@class='tile update']/span/text()" 






class Spider(scrapy.Spider):

    name = 'dolar'
    start_urls = [
        "https://dolarhoy.com/"
    ] 


    
    def parse(self, response):
        
        nombres = response.xpath(XPATH_NAMES).getall()
        
        compra = response.xpath(XPATH_COMPRA).getall()
        venta = response.xpath(XPATH_VENTA).getall() 
        fecha = response.xpath(XPATH_FECHA).getall() 
        fecha_total = fecha*5
         
        
        df = pd.DataFrame(list(zip(nombres,compra,venta,fecha_total)),columns = ['Nombre','Compra',"Venta","Fecha"]) 
        print(df) 

        df.to_csv('dolar.csv', index=False)   

process = CrawlerProcess()
process.crawl(Spider)
process.start()
        


    
   

   
