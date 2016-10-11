# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from rfa.items import RfaItem
from scrapy.linkextractors import LinkExtractor
import time


class TestSpider(CrawlSpider):
    name = "rfa"
    allowed_domains = ["www.rfa.org"]
    start_urls = [
    'http://www.rfa.org/khmer',
    ]

    def parse(self, response):
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        hxs = scrapy.Selector(response)
        item = RfaItem()
        top_stories = hxs.xpath('//div[@id="topstorywidetease"]')
        item['categoryId'] = '1'

        name = top_stories.xpath('h2[1]/a[1]/span[1]/text()')
        if not name:
            print('RFA => [' + now + '] No title')
        else:
            item['name'] = name.extract_first()

        url = top_stories.xpath('h2[1]/a[1]/@href')
        if not url:
            print('RFA => [' + now + '] No url')
        else:
            item['url'] = 'http://rfa.org/' + url.extract_first()

        description = top_stories.xpath('h2[1]/following-sibling::p[1]/text()')
        if not description:
            print('RFA => [' + now + '] No description')
        else:
            item['description'] = description.extract_first()

        imageUrl = top_stories.xpath('//div[@id="topstorywideimg"]/a[1]/img[1]/@src')
        if not imageUrl:
            print('RFA => [' + now + '] No imageUrl')
        else:
            item['imageUrl'] = imageUrl.extract_first()

        yield item

        ## COL A

        col_a = hxs.xpath('//div[@id="morenewsColA"]/div[@class="sectionteaser"]')

        for col in col_a:
            item = RfaItem()
            item['categoryId'] = '1'
            name = col.xpath('h2[1]/a[1]/span[1]/text()')
            if not name:
                print('RFA => [' + now + '] No title')
            else:
                item['name'] = name.extract_first()

            url = col.xpath('h2[1]/a[1]/@href')
            if not url:
                print('RFA => [' + now + '] No url')
            else:
                item['url'] = url.extract_first()

            description = col.xpath('h2[1]/following-sibling::text()')
            if not description:
                print('RFA => [' + now + '] No description')
            else:
                item['description'] = description.extract_first()

            imageUrl = col.xpath('div[@class="teaserimg"][1]/a[1]/img[1]/@src')
            if not imageUrl:
                print('RFA => [' + now + '] No imageUrl')
            else:
                item['imageUrl'] = imageUrl.extract_first()

            yield item

        # COL_B

        col_b = hxs.xpath('//div[@id="morenewsColB"]/div[@class="sectionteaser"]')

        for col in col_b:
            item = RfaItem()
            item['categoryId'] = '1'
            name = col.xpath('h2[1]/a[1]/span[1]/text()')
            if not name:
                print('RFA => [' + now + '] No title')
            else:
                item['name'] = name.extract_first()

            url = col.xpath('h2[1]/a[1]/@href')
            if not url:
                print('RFA => [' + now + '] No url')
            else:
                item['url'] = url.extract_first()

            description = col.xpath('h2[1]/following-sibling::text()')
            if not description:
                print('RFA => [' + now + '] No description')
            else:
                item['description'] = description.extract_first()

            imageUrl = col.xpath('div[@class="teaserimg"][1]/a[1]/img[1]/@src')
            if not imageUrl:
                print('RFA => [' + now + '] No imageUrl')
            else:
                item['imageUrl'] = imageUrl.extract_first()

            yield item



    def parse_detail(self, response):
        item = response.meta['item']
        hxs = scrapy.Selector(response)
        now = time.strftime('%Y-%m-%d %H:%M:%S')

        item_page = hxs.css('div.item-page')
        description = item_page.xpath('p[1]/text()')
        if not description:
            print('ThmeyThmey => [' + now + '] No description')
        else:
            item['description'] = item_page.xpath('p[1]/strong/text()').extract_first() + ' ' + description.extract_first()

        imageUrl = item_page.xpath('p[last()]/img/@src')
        if not imageUrl:
            print('ThmeyThmey => [' + now + '] No imageUrl')
        else:
            item['imageUrl'] = imageUrl.extract_first()


        yield item
