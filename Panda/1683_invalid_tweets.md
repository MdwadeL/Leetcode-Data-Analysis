# 1683 Invalid Tweets
tweets(tweet_id, content)

| tweet_id | content                           |
| -------- | --------------------------------- |
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

## Skills
- String length
- Filtering rows
- Text validation

# Solution:
    invalid_tweets = tweets[
        (tweets['content'].str.len() > 15)
    ]

    return invalid_tweets[['tweet_id']]

<br>

| tweet_id |
| -------- |
| 2        |
