import scrapy
import csv
import datetime
from sentiment.mail import send_email


class SentimentSpider(scrapy.Spider):
    name = "sentiment"

    start_urls = [
        'https://www.aaii.com/sentimentsurvey/sent_results',
    ]

    def parse(self, response):
        data= response.xpath('((//table)[1]//tr//td//text())')
        list_data = [i.extract().strip() for i in data]
        list_data_final = [i for i in list_data if i]
        filename = 'sentiment_data.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(0,len(list_data_final),4):
                writer.writerow(list_data_final[i:i+4])
        send_email('sentiment_data.csv')
        self.log('Saved file %s' % filename)