import datetime
from tqdm.notebook import tqdm as tqdm_notebook
from random import uniform
import time
import GetOldTweets3 as got
from bs4 import BeautifulSoup
import pandas as pd
# !pip install bs4
# !pip install GetOldTweets3
# !pip install pandas
# pip install -r requirementes.txt
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta


days_range = []

start = datetime.datetime.strptime("2017-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-06-13", "%Y-%m-%d")
date_generated = [
    start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    days_range.append(date.strftime("%Y-%m-%d"))

print("=== 설정된 트윗 수집 기간은 {} 에서 {} 까지 입니다 ===".format(
    days_range[0], days_range[-1]))
print("=== 총 {}일 간의 데이터 수집 ===".format(len(days_range)))

# 특정 검색어가 포함된 트윗 검색하기 (quary search)
# 검색어 : 어벤져스, 스포


# 수집 기간 맞추기
start_date = days_range[0]
end_date = (datetime.datetime.strptime(days_range[-1], "%Y-%m-%d")
            + datetime.timedelta(days=1)).strftime("%Y-%m-%d")  # setUntil이 끝을 포함하지 않으므로, day + 1

# 트윗 수집 기준 정의
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#2018_여성작가 OR #2019_여성작가 OR #2020_여성작가')\
                                           .setUntil(end_date)\
                                           .setMaxTweets(-1)

# 수집 with GetOldTweet3
print("Collecting data start.. from {} to {}".format(
    days_range[0], days_range[-1]))
start_time = time.time()

tweet = got.manager.TweetManager.getTweets(tweetCriteria)

print("Collecting data end.. {0:0.2f} Minutes".format(
    (time.time() - start_time)/60))
print("=== Total num of tweets is {} ===".format(len(tweet)))

# 원하는 변수 골라서 저장하기


# initialize
tweet_list = []

for index in tqdm_notebook(tweet):
    # 메타데이터 목록
    username = index.username
    link = index.permalink
    content = index.text
    # print(content)
    tweet_date = index.date.strftime("%Y-%m-%d")
    tweet_time = index.date.strftime("%H:%M:%S")
    retweets = index.retweets
    favorites = index.favorites

    # 결과 합치기
    info_list = [tweet_date, tweet_time, username,
                 content, link, retweets, favorites]
    tweet_list.append(info_list)

    doc = {'date' : tweet_date, 'time' : tweet_time, 'user_name' : username, 'text' : content, 'link': link, 
         'RT' : retweets , 'favorites' : favorites}

    db.women_writer2.insert_one(doc)


# final_list = {"date" : date, "time" : time, "user_name" :username, "text" : text, "link": link, 
#                  "retweet_counts" : rt_counts, "favorite_counts" : faborite_counts} 
   
# db.reviews.insert_one(final_list)

    # 휴식
    # time.sleep(uniform(1,2))

twitter_df = pd.DataFrame(tweet_list,
                          columns=["date", "time", "user_name", "text", "link", "retweet_counts", "favorite_counts"])

# csv 파일 만들기
twitter_df.to_csv("sample_twitter_data_{}_to_{}.csv".format(
    days_range[0], days_range[-1]), encoding="utf-8", index=False)
print("=== {} tweets are successfully saved ===".format(len(tweet_list)))

# df_tweet = pd.read_csv('sample_twitter_data_{}_to_{}.csv'.format(days_range[0], days_range[-1]))
# #df_tweet.head(10) # 위에서 10개만 출력

# aa = pd.read_csv('sample_twitter_data_2019-12-01_to_2019-12-30.csv')
# print(aa.values)

# final_list = {"date" : date, "time" : time, "user_name" :username, "text" : text, "link": link, 
#                  "retweet_counts" : rt_counts, "favorite_counts" : faborite_counts} 
   
# db.reviews.insert_one(final_list)
