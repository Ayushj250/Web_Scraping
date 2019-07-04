# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 23:40:51 2019

@author: Ayush Jain
"""

# IMDB scraping for top 50 movies in 2018(couldn't find the 1000 movies details)

from bs4 import BeautifulSoup
from requests import get
import pandas as pd
url='https://www.imdb.com/search/title/?release_date=2018&sort=num_votes,desc&page=1'
response=get(url)
html=BeautifulSoup(response.text,'html.parser')
movie_containers=html.find_all('div',class_='lister-item mode-advanced')
names=[]
ratings=[]
casts=[]
for container in movie_containers:
    #The name of the movie
    name=container.h3.a.text
    names.append(name)
    #The rating
    rating=float(container.strong.text)
    ratings.append(rating)
    #The Casts
    c=container.find_all('p')
    a=c[2].find_all('a')
    cast=""
    for s in a:
        cast=cast+s.text+", "
    casts.append(cast[:-1])
data=pd.DataFrame({'Movie':names,
                   'Ratings':ratings,
                   'Cast':casts})
print(data)
'''for i in range(len(names)):
    print("**********************"+str(i)+"**********************")
    print("Name- ", names[i])
    print("Rating- ", ratings[i])
    print("Cast and Director:")
    print(casts[i])'''