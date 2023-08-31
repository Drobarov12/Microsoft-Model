from gnews import GNews
import pandas as pd
import re
import datetime
import urllib.parse

def convertDate(date: str):
  # return datetime.datetime object from string parameter
  parts = re.split('\W', date)
  return datetime.datetime(year = int(parts[0]), month = int(parts[1]), day = int(parts[2]))

def changeDate(news: GNews):
  # increments the daterange by 5 days in a given GNews object
  startDateObj = convertDate(news.start_date)
  endDateObj = convertDate(news.end_date)
  news.start_date = startDateObj + datetime.timedelta(days = 5)
  news.end_date = endDateObj + datetime.timedelta(days = 5)
  return news

def getQuery2(news: GNews, keyword: str, results):
  # scrape Google News using the get_news command in GNews
  global newResults
  newResults = []
  newResults = news.get_news(urllib.parse.quote(keyword))
  results += newResults
  return results

def saveResults(results):
  # save results argument in a csv on local Drive Location (currently hardcoded)
  #null check
  if results is not None:
    d = []
    for post in results:
      title = post['title']
      description = post['description']
      date = datetime.datetime.strptime(post['published date'][5:16], '%d %b %Y')
      d.append((date,title,description))
    #0 length check
    if len(d)>0:
      global df
      df = pd.DataFrame(d, columns=('Date','Title','Description'))
      df = df.sort_values(by = ['Date'], ascending=False)
      file_name = "/Users/user/Projects/196124/VNP/RawData/GoogleNews_" + name + "_" + startDate.date().isoformat() + "_" + finalDate.date().isoformat() + ".csv"
      # Store data to CSV
      df.to_csv(file_name, encoding='utf-8', index=False)
      print(len(df), " articles saved on ", file_name)


def config2(news: GNews):
  # config GNews object on en-US locality and specific starting date, used to resume scraping
  global startDate
  news.langauge = 'en'
  news.country = 'US'
  news.start_date = startDate = convertDate('2019-07-27')
  news.end_date = startDate + datetime.timedelta(days = 5)
  return news

def main():
  global news, results, name, finalDate
  news = GNews()
  name = 'Microsoft'
  news = config2(news)
  finalDate = datetime.datetime(2019 , 8, 1)

  kw = 'Microsoft'
  results = []
  name = kw.replace(' ','')
  # time.sleep(5)
  print('Started scraping for keyword: ' + kw)
  newsEndDateObj = convertDate(news.end_date) # 2019/3/2 at first
  while newsEndDateObj < finalDate:
    print('Currently at: ' + news.end_date + ' and ' + str(len(results)) + ' results.')
    results = getQuery2(news, kw, results)
    if(len(newResults)==0):
      finalDate = newsEndDateObjу
      saveResults(results)
      print('Data gathering stopped at: ' + news.end_date)
      return
    news = changeDate(news)
    newsEndDateObj = convertDate(news.end_date)
  saveResults(results)
  print('Scrape for ' + kw + ' has finished. Got ' + str(len(results)) + ' results.')



if __name__ =="__main__":
  main()

