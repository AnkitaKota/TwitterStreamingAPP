 Streaming data pipeline for Twitter Tweet
I have used Tweepy python library to connect twitter streaming API by handling authentication, connection, creating and destroying the session, reading incoming messages, and filtering the data.
 Startup guide:
 1) We will need to have Python 3.8 installed on your machine
 2) Download tweePy library
 3) Create twitter elevated account access. Please have below twitter account Api access secrets handy.
    1) consumer_key
    2) consumer_secret
    3) api_key
    4) api_secret
 ![img_1.png](img_1.png)
Useful Reference:
 https://developer.twitter.com/en/support/twitter-api/developer-account
 4) I have used MongoDB free Cloud account to store the tweets data
References:
 https://www.knowi.com/blog/getting-started-with-mongodb-atlas-overview-and-tutorial/
 5) Have MongoDB Connection String handy including Secrets
 6) Please add your PC IP to Mongo DB whitelist IP section in case of an issue where MongoDB reject the connection when you try to conenct your local environment to Cloud MongoDb instance.
 7) I have used pymongo library used to connect to MangoDB. Please install pymongo
 8) Used pyMongo to create Database, Collection and index
 9) Download python NLTK library for tokenizing the twitter text

Current application Flow:

Python Application Start -> tweePY -> Connect to Twitter Api
                                   -> Search the Tweets with Justin Bieber
                                   -> Response will be filterd by using NLTK python library
                                   -> Connect to MongoDB using pyMongo
                                   -> Save the data to database collection
Data filtering steps:
1. Kept a track of Number of tweets: tweetCount
2. Filtering out duplicate tweet by initialising a list and checking if the tweet has already been consumed.
3. Since the previous step has been executed, Number of tweets and Number of unique tweets will remain same.
4. I'm also filtering out on the keyword '#music' or 'music'.

![img_2.png](img_2.png)
RUN configurations :
----------------------

POC to production ready
-----------------------
Here is the high level that can be used to build MVP deliverable

![img_3.png](img_3.png)

Production readiness checklist:
CICD: Automated build and deploy pipeline
1) Build a CI pipeline
   1) PR commit to Main branch trigger CI
   2) Build
   3) Unit Test
   4) Code coverage
   5) Security vulnerabilities
2) Build CD
   1) Build to Dev environment
   2) Run regression test suite
   3) Success move on to QA Env,Failure Rollback the application to previous version
   4) Notify the Deployment status to users

Test cycle:
1) User acceptance testing
2) Automated Regression test suite that will be triggered as part of CICD
3) Performance Test
4) Disaster recovery test
5) Choas test()

Scalability and Application performance:
1) Horizontal Scaling

Monitoring:
1) Monitoring Producer, consumer apps and infrastructure
2) Build Dashboards to monitor application performance and identify key metrics(Success,failure, error codes etcs)
3) Create alerts and integrate with workflow tools

Documentation:
1) Data-pipeline documentation
2) Product documentation
3) Support documentation









