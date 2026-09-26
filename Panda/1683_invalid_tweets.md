# 1683 Invalid Tweets

tweet_id PK = {...}
content = {values consist of: ABC123, '!', ' '}

An invalid tweet is when [content] holds a value with more than 15 characters

## Skills
- String length
- Filtering rows
- Text validation

# Solution 1
    tweets = tweets[
        (tweets['content'].str.len() > 15)
    ][['tweet_id']]

    return tweets
# runtime: 276ms
