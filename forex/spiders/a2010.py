import time
import scrapy
from scrapy.utils.reactor import install_reactor 
install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
from scrapy import Selector
from scrapy_playwright.page import PageMethod
import logging
from datetime import datetime
from data import link_10

def get_headers(s, sep=': ', strip_cookie=True, strip_cl=True, strip_headers: list = []) -> dict():
    d = dict()
    for kv in s.split('\n'):
        kv = kv.strip()
        if kv and sep in kv:
            v=''
            k = kv.split(sep)[0]
            if len(kv.split(sep)) == 1:
                v = ''
            else:
                v = kv.split(sep)[1]
            if v == '\'\'':
                v =''
            # v = kv.split(sep)[1]
            if strip_cookie and k.lower() == 'cookie': continue
            if strip_cl and k.lower() == 'content-length': continue
            if k in strip_headers: continue
            d[k] = v
    return d

def should_abort_request(req):

    if req.resource_type == "image":
        logging.log(logging.INFO, f"Ignoring Image {req.url}")
        return True
    if req.method.lower() == 'post':
        logging.log(logging.INFO, f"Ignoring {req.method} {req.url} ")
        return True

    return False




class A2010Spider(scrapy.Spider):
    name = "2010"
    custom_settings = {
        
#         'DOWNLOAD_DELAY': 1 , # 2 seconds of delay 

        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "headless": True,
#            "proxy": {
#                "server": "socks5://127.0.0.1:9050"

#            },

#            "proxy": {
#                "server": "https://proxy.scrapeops.io/:5353" ,
#                "username": "scrapeops.headless_browser_mode=true",
#                "password": "e4ea08af-ef35-4354-885d-e75b34979a52",
#            },

        },
        

        'FEEDS': {
#            f'links-{datetime.now()}.csv': 
             '2010.csv':
            {
                'format': 'csv'
            }},
        'PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT': '100000',
        'PLAYWRIGHT_ABORT_REQUEST': should_abort_request ,

    }


    def start_requests(self):
             h = get_headers('''
             ''')
             for link in link_10() :
                yield scrapy.Request(
           url = f'{link}',
#           headers=h,
           dont_filter=True,
            callback=self.parse,
                meta=dict(
                playwright = True,
                playwright_include_page = True ,
                playwright_page_methods = [
                         ],
                errback =self.errback ,
                headers=h,
            ))
            

    async def parse(self, response):
                
        page = response.meta["playwright_page"]


        date = response.xpath('//*[@id="flexBox_flex_calendar_mainCal"]/form/div[1]/ul/li[2]/h2/a/span/text()').extract()
        numer_of_rows = response.css('.calendar__row--grey')
        n = 2*(len(numer_of_rows))+2
        print(date)
        print(len(numer_of_rows))
        for i in range (3,n,2):
            
            t = response.xpath(f'//*[@id="flexBox_flex_calendar_mainCal"]/table/tbody/tr[{i}]/td[2]/div/text()').get()
            Currency = response.xpath(f'//*[@id="flexBox_flex_calendar_mainCal"]/table/tbody/tr[{i}]/td[4]/text()').get()
            Impact = response.xpath(f'//*[@id="flexBox_flex_calendar_mainCal"]/table/tbody/tr[{i}]/td[5]/span/@title').get()
            
            Description = response.xpath(f'//*[@id="flexBox_flex_calendar_mainCal"]/table/tbody/tr[{i}]/td[6]/div/span/text()').get()
            Actual = response.xpath(f'//*[@id="flexBox_flex_calendar_mainCal"]/table/tbody/tr[{i}]/td[8]/text()').get()
           
            Forecast = response.xpath(f'//*[@id="flexBox_flex_calendar_mainCal"]/table/tbody/tr[{i}]/td[9]/span/text()').get()
            P1 = response.xpath(f'//*[@id="flexBox_flex_calendar_mainCal"]/table/tbody/tr[{i}]/td[10]/span/span/text()').extract()
            p2 = response.xpath(f'//*[@id="flexBox_flex_calendar_mainCal"]/table/tbody/tr[{i}]/td[10]/span/text()').get()
            pp1 = ''.join(P1)
            pp2 = "".join(p2.split())
            Previous = pp1+pp2   



            yield {
                'Date' : date ,
                'Time' :t,
                'Currency' : Currency, 
                'Impact' : Impact,
                'Description' : Description ,
                'Actual' : Actual, 
                'Forecast' : Forecast,
                'Previous' : Previous ,


            }

              
        await page.close()





        
    async def errback(self,failure) :
        page = failure.request.meta["playwright_page"]
        await page.close()