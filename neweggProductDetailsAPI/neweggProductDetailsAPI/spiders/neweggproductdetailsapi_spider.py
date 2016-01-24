import scrapy
import csv
import re
from neweggProductDetailsAPI.items import NeweggproductdetailsapiItem
class neweggproductdetailsapi_Spider(scrapy.Spider):
    name = "neweggpda"
    allowed_domains = ["newegg.com"]
    #start_urls=["http://www.newegg.com/Product/Product.aspx?Item=9SIA68F39E3613"]
    data=[line.strip() for line in open("/media/raghu/DATA/newegg mining/Product Lists.txt", "r")]
    for i in range(0,len(data)):
	data[i]=data[i][3:(len(data[i])-2)]
    start_urls=data

    def parse(self,response):
	item=NeweggproductdetailsapiItem()
	item['spec']=[]
	temp=response.xpath('/html/head/meta[5]/@content').extract()
        l=response.xpath('//*/div/div/div/a/@title').extract()
	m=[]
	item['brand']=l[0]
	item['rating']=response.xpath('//*[@id="synopsis"]/div[2]/div/div[4]/a/span[1]/@content').extract()
	r=0
	while(True):
		r=r+1		
		m=[]		
		t='//*/li['
		u=']/text()'
		try:
			k=response.xpath(t+str(r)+u).extract()
			for i in range(0,len(k)):
				k[i]=k[i].encode('ascii','ignore')
				k[i]=k[i].strip()
			m.append([q for q in k if q])
			k[0]=m[0][0]
			item['spec'].append(k[0])
		except IndexError:
			break
	
	#------------------------------------------------------------------------------
	#for g in range(1,r):
		#print(item['spec'+str(g)])
	
		
	yield item		

