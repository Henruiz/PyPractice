
class Tweets:

    def __init__(self, tweet, date):
        self.tweet = tweet
        self.date = date


tweet1 = Tweets("hello", 2012)
tweet2 = Tweets("hey", 2014)
tweet3 = Tweets("hi", 2016)

t = [tweet1, tweet2, tweet3]

for x in t:
    print(x.tweet)


