import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver_win32/chromedriver.exe'}
    return Browser('chrome', **executable_path, headless= False)

def scrape():
    browser = init_browser()

    the_data = {}

    url_news = 'https://mars.nasa.gov/news/'
    browser.visit(url_news)

    html = browser.html
    soup_news = bs(html, 'html.parser')

    results = soup_news.find_all('div', class_="slide")

    news = []
    title = []

    for result in results:
        news_title = result.find('div', class_='content_title').text
        print(f'News Titles: ' + news_title)
        news_p = result.find('div', class_='rollover_description_inner').text
        print(f'News Text: ' + news_p)
        news.append(news_p)
        title.append(news_title)
        print('...')

        the_data['news title'] = news_title
        the_data['news text'] = news_p

    return the_data

def build_report(mars_report):
    final_report = ""
    for p in mars_report:
        final_report += " " + p.get_text()
        print(final_report)
    return final_report

if __name__ == '__main__':
    scrape()


    