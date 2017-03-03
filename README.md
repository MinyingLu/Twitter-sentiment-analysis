This is a class project of Minying Lu and Chelsea Waida on Twitter Sentiment Analysis

[Final Report](https://github.com/minggLu/Twitter-sentiment-analysis/blob/master/FinalReport.pdf)
[Final Poster](https://github.com/minggLu/Twitter-sentiment-analysis/blob/master/Poster.pdf)`

### 4/1 Happy April Fools day :p

**Minying**
- get /follower/list of the 20ish users (3 and -4), find the users that are following the popular users and also in our dataframe(5000) and compare the polarity scores
  - if we can't find the following relationships we can search the whole dataset
  - maybe geo

**Chelsea**
- popularity is defined by # of retweets + favorites
- for each tweet, get urls: T/F from eneities
- for each tweet, get list of mentioned users (id? name?)
- history gram for things:
  - urls vs popularity & polarity
  - mentioned vs popularity & polarity

### 4/8: mid-project report

Tasks:
1. Better sentiment analysis: `nltk.sentiment` module
2. Regression
- x: # of retweets of user, # of likes of user, # number of followers, # of mentions of user, desirable polarity score of tweet(s) of the user
- y: popularity of the user
3. Clustering: define similarity between users, and relationship between their similarity and polarity score
- define similarity base on list(s) that the specified user is a member of or subscribes to `GET /lists/memberships` and `GET /lists/list`  
  - feature extraction/vectorization
- cluster users base on their similarity, find corelation between the clusters and polarity score
- Stretch goal: keyword extraction of tweets to find a more specific opinion of a user's tweet and cluster them base on their opinion
  - for example people might be focusing on: the society being more supportive, or women should not be afraid to stand out and speak about their experience, or the law should be more strict on this kind of matter, etc

