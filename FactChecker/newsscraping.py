import pandas as pd
import numpy as np
from requests_html import HTMLSession
import time
from googlesearch import search_news
from googlesearch import search
from newsplease import NewsPlease

#from nltk.tokenize import sent_tokenize
#import nltk
#nltk.download('punkt')


def parse_elements(url):
    session = HTMLSession()
    text = ''
    try:
      r = session.get(url)
      for element in ('h1', 'p', 'span', 'li'):
        try:
            elements = r.html.find(element)
            elements = ' '.join([element.text for element in elements])
            text = text + ' ' + elements
        except Exception:
            continue
      #elements = list(map(lambda x: x.text, elements))
      return text
    except Exception:
      try:
          article = NewsPlease.from_url(url)
          title = article.title
          description = article.description
          main_text = article.maintext
          text = text + title + ' ' + description + ' ' + main_text
          return text
      except Exception:
        return np.nan




def news_scraper(query):
    news_result = search_news(query=query, num=5, stop=5)
    result = search(query=query, num=5, stop=5)
    news_result = list(news_result)
    result = list(result)
    while len(news_result) < len(result):
        news_result.append(np.nan)
    while len(result) < len(news_result):
        result.append(np.nan)
    results_df = pd.DataFrame({'results': result, 'news_results': news_result})
    results_df['articles'] = results_df['results'].apply(lambda x: parse_elements(x))
    results_df['news_articles'] = results_df['news_results'].apply(lambda x: parse_elements(x))
    return(results_df)
