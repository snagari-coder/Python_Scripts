
# This script lists the most popular hacker news items from Hacker News website.
# requests --> allows use to grab/download html files from websites
# beautiful soup --> allows us to use html and grab/scrape different data
import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get(
    'https://news.ycombinator.com/news')  # Requests is like a web browser, we are browsing the website
# print(response.text) --> gives a string with all the text in the page
soup = BeautifulSoup(response.text, 'html.parser')  # converts the string into html format, readable and understandable
# print(soup.body.contents) # All the contents of the body in list form
# print(soup.find_all('a')) # All the div objects contained in the page in list form
# print(soup.title)
# print(soup.select('.score')) # css selector, selects concerned parts from html page
# print(soup.select('#score_27797853'))
# print(soup.select('.storylink')[0])
links = soup.select('.storylink')  # Each link has a storylink class
# votes = soup.select('.score')  # Each points/likes for the link has a score class, right click --> inspect
subtexts = soup.select('.subtext')  # Each link has a subtext

def sort_stories_by_votes(hacker_news_list):
    return sorted(hacker_news_list, key = lambda k:k['votes'], reverse=True)


def create_custom_hackerNews(links, subtexts):
    hackerNews = []
    for idx, item in enumerate(links):

        # title = links[idx].getText()
        title = item.getText()
        # href = links[idx].get('href', None)  # If there is a title without a href attribute
        href = item.get('href', None)
        vote = subtexts[idx].select('.score')
        # print(vote)
        # print(vote[0].getText())
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points > 99:
                hackerNews.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hackerNews)


pprint.pprint(create_custom_hackerNews(links, subtexts))
