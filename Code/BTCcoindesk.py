import scrapy


class BtccoindeskSpider(scrapy.Spider):
    name = "BTCcoindesk"
    allowed_domains = ["www.coindesk.com"]
    start_urls = ["https://www.coindesk.com/tag/bitcoin/1"]

    def parse(self, response):
        articles = response.css('div.article-cardstyles__AcTitle-sc-q1x8lc-1.PUjAZ.articleTextSection')

        for article in articles:
            yield{
                'title' : article.css('h6 a.card-title::text').get(),
                'sub_title' : article.css('.display-desktop-block.display-tablet-block.display-mobile-block .typography__StyledTypography-sc-owin6q-0.hLnyzj .content-text::text').get(),
                'date' : article.css('.timing-data .typography__StyledTypography-sc-owin6q-0.hcIsFR::text').get()
            }
   
        url_list = []

        for a in range(2, 593):
            next_url = 'https://www.coindesk.com/tag/bitcoin/' + str(a) 
            url_list.append(next_url)
        
        for item in url_list:
            yield response.follow(item, callback = self.parse)