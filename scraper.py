from requests_html import HTMLSession
import json
import time
import random

class Reviews:
    # asin = Amazon Standard Identification Number (sheesh alam ni copilot, product identifier for amazon)
    def __init__(self, url) -> None:
        # self.asin = asin
        self.url = url
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
        
    def pagination(self, page):
        r = self.session.get(self.url + str(page))
        timeout_interval = random.uniform(20, 22)
        r.html.render(timeout=timeout_interval)
        if not r.html.find('div[data-hook=review]'):
            return False
        else:
            return r.html.find('div[data-hook=review]')

    def parse(self, reviews):
        total = []
        for review in reviews:
            name = review.find('.a-profile-name', first=True).text
            title = review.find('a[data-hook=review-title]', first=True).text
            rating = review.find('i[data-hook=review-star-rating] span', first=True).text
            body = review.find('span[data-hook=review-body] span', first=True).text.replace('\n', '').strip()

            data = {
                'name': name,
                'title': title,
                'rating': rating,
                'body': body
            }
            total.append(data)
        return total

if __name__ == '__main__':
    scraper = Reviews('https://www.amazon.com/Redragon-S101-Keyboard-Ergonomic-Programmable/product-reviews/B00NLZUM36/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')
    results = []
    # x = 1
    # for x in range(1, 20):
    #     reviews = scraper.pagination(x)
    #     print('Page found: ', x)
    #     if reviews is not False:
    #         results.append(scraper.parse(reviews))
    #         # x += 1
    #     else:
    #         print(f'Traversed {x-1} pages')
    #         print('No more reviews')
    #         break
    #     interval = random.uniform(3, 5)
    #     time.sleep(interval)
    # # print(json.dumps(results))
    # results_count = len(results)
    # print('Total reviews: ', results_count)
    # with open('content.json', 'w') as f:
    #     json.dump(results, f, indent=4)
    reviews = scraper.pagination(2)
    print(scraper.parse(reviews))