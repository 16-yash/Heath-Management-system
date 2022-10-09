import json

import requests
import time


def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    while True:
     print("Which Type Of News You Want To Listen Or Read\n")
     speak("Which Type Of News You Want To Listen Or Read")
     choice = input("'B' - For Business Related\n'S' For Sports Realated\n'T' For Technology Related\n")
     i=1
     if choice == 'T':
       url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=b196bae05af54603b10991809a872879"
       print("LISTEN TODAY TOP 10 HEADLINES RELATED TO TECHNOLOGY")
       speak("LISTEN TODAY TOP 10 HEADLINES RELATED TO TECHNOLOGY")
       news = requests.get(url).text
       news_dict = json.loads(news)
       arts = news_dict["articles"]
       for article in arts:
          speak(f"News {i} ")
          print(f" News {i}",article['title'])
          speak(article['title'])
          i+=1
          if i == 11:
              break
     if choice == 'S':
       i=1
    
       url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=b196bae05af54603b10991809a872879"
       print("LISTEN TODAY TOP 10 HEADLINES RELATED TO SPORTS")
       speak("LISTEN TODAY TOP 10 HEADLINES RELATED TO SPORTS")
       news = requests.get(url).text
       news_dict = json.loads(news)
       arts = news_dict["articles"]
       for article in arts:
          speak(f"News {i} ")
          print(f" News {i}",article['title'])
          speak(article['title'])
          i+=1
          if i == 11:
              break
     if choice == 'B':
       i=1
    
       url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=b196bae05af54603b10991809a872879"
       print("LISTEN TODAY TOP 10 HEADLINES RELATED TO BUSINESS")
       speak("LISTEN TODAY TOP 10 HEADLINES RELATED TO BUSINESS")
       news = requests.get(url).text
       news_dict = json.loads(news)
       arts = news_dict["articles"]
       for article in arts:
          speak(f"News {i} ")
          print(f" News {i}",article['title'])
          speak(article['title'])
          i+=1
          if i == 11:
              break
print("News Ended Here\nStay Tune\nSee You Tomorrow")
speak("News Ended Here Stay Tune See You Tomorrow")
        

    







    
