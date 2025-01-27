#themoviedb.org ->  film ve dizi arsivi
#themoviedb nin sunduğu apiyi uygulamanızda kullanınız
#anahtar kelimeye göre arama
#en populer film listesi
#vizyondaki film listesi

import requests
import json
class themovieDB:
    def __init__(self):  #kurucu metot
        self.api_url="https://api.themoviedb.org/3"
        self.api_key="96a3a0f38a6d2b5d30b31c3de4060398"
    def getPopulars(self):    #populer filmleri çeken metot
        response= requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self, keyword): #film arama metodu
      response= requests.get(f"{self.api_url}/search/movie?api_key={self.api_key}&query={keyword}&language=en-US&page=1")
      return response.json()

movieApi = themovieDB()
while True:
     secim = input("1-popula movies\n2-Search movies\n3-Exit\nSecim:")
     if secim=="3":
         break
     else:
         if secim=="1":
             movies=movieApi.getPopulars()   #populer filmleri listele
             for movie in movies["results"]:
                 print(movie["title"])
         if secim =="2":
             keyword=input("keyword: ")   #anahtar kelime ile film arama
             movies = movieApi.getSearchResults(keyword)
             for movie in movies['results']:
                 print(movie['title'])  #filmin adı

