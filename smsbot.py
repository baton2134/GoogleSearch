import telebot
import config
import string
import csv
import sys
import os
import statistics
import time
from telebot import types
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def wel(message):

    bot.send_message(message.chat.id, "добро пожаловать, сделан @lamia222")
m=""






import time
from urllib.parse import quote_plus
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser:


    def __init__(self, path, initiate=True, implicit_wait_time = 10, explicit_wait_time = 2):
        self.path = path
        self.implicit_wait_time = implicit_wait_time    # http://www.aptuz.com/blog/selenium-implicit-vs-explicit-waits/
        self.explicit_wait_time = explicit_wait_time    # http://www.aptuz.com/blog/selenium-implicit-vs-explicit-waits/
        if initiate:
            self.start()
        return

    def start(self):
        self.driver = webdriver.Chrome(ChromeDriverManager())
        self.driver.implicitly_wait(self.implicit_wait_time)
        


    def end(self):
        self.driver.quit()
        return


    def go_to_url(self, url, wait_time = None):
        global k,i
        if wait_time is None:
            wait_time = self.explicit_wait_time
        self.driver.get(url)
        i=('[*] Fetching results from: {}'.format(url))

        time.sleep(wait_time)
        return

    def get_search_url(self, query, page_num=0, per_page=10, lang='ru'):
        query = quote_plus(query)
        url = 'https://www.google.hr/search?q={}&num={}&start={}&nl={}'.format(query, per_page, page_num*per_page, lang)
        return url

    def scrape(self):
        #xpath migth change in future
        links = self.driver.find_elements_by_xpath("//h3[@class='r']/a[@href]") # searches for all links insede h3 tags with class "r"
        results = []
        for link in links:
            d = {'url': link.get_attribute('href'),
                 'title': link.text}
            results.append(d)
        return results

    def search(self, query, page_num=0, per_page=10, lang='en', wait_time = None):
        if wait_time is None:
            wait_time = self.explicit_wait_time
        url = self.get_search_url(query, page_num, per_page, lang)
        self.go_to_url(url, wait_time)
        results = self.scrape()
        return results

@bot.message_handler(content_types=['text'])
def lalala(message):
    global m,i
    m = str(message.text)
    
    path = '/usr/bin/chromedriver'
    br = Browser(path)
    results = br.search(str(m))
    bot.send_message(message.chat.id, i)
    for r in results:
        print(r)
    br.end()

if __name__ == '__main__':
    bot.polling(none_stop=True)
    os.execv(__file__, sys.argv)


