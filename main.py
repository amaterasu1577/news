from client import News
from enum import Enum

class Code(Enum):
    BOLD = '\033[1m'
    DEF = '\033[0m'

def main():
    news = News()
    choix = input('Country headlines [' + str(Code.BOLD) + 'default' + str(Code.DEF) +\
         '] or Search [hit ' + str(Code.BOLD) + 's' + str(Code.DEF) + ']?\n> ')
    if str(choix).lower() == 's':
        search = input(f'What are you looking {Code.BOLD}for{Code.DEF}?')
    else:
        country = input("What country are you interested in?\n> ")
        headlines = news.country_headlines(country)
    for headline in headlines:
        print(f"- {headline}")

if __name__ == '__main__':
    main()
