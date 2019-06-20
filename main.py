from client import News

def main():
    news = News()
    country = input("What country are you interested in?\n> ")
    headlines = news.country_headlines(country)
    for headline in headlines:
        print(f"- {headline}")

if __name__ == '__main__':
    main()
