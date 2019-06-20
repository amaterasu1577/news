import requests

# State?
# Behavior?
# => - country_headlines
# => - keyword_headlines
# Client API
class News:
    def country_headlines(self, country):
        payload = {'country': country, 'apiKey': '367f28d82c3b42e2bb224b79b0ef480e'}
        r = requests.get('https://newsapi.org/v2/top-headlines', params=payload)

        articles = []
        # print(r.json()) #?
        for item in r.json()['articles']:
            articles.append(item['title'])
        return articles
