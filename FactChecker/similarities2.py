import requests
from bs4 import BeautifulSoup
import pandas as pd
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer, util
import nltk
nltk.download('punkt')

model = SentenceTransformer("BAAI/bge-m3")

def sorted_df(df, query):
  articles = ' '.join(list(df['articles']))
  news_articles = ' '.join(list(df['news_articles']))
  full_articles = articles + news_articles
  sentences = sent_tokenize(full_articles)
  sentence_embeddings = model.encode(sentences, convert_to_tensor=True)
  query_embedding = model.encode([query], convert_to_tensor=True)[0]
  similarities = util.pytorch_cos_sim(query_embedding, sentence_embeddings)[0]
  similarities = [i.item() for i in similarities]
  new_df = pd.DataFrame({'sentences':sentences,'similarities':similarities})
  #new_df['similarities'] = pd.to_numeric(new_df['similarities'])
  new_df = new_df.sort_values(by='similarities', ascending=False)
  return new_df