import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    m = tweets['content'].str.len() > 15
    return tweets.loc[m, ['tweet_id']]