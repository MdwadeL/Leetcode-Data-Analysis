# 197 Rising Temperature

## Skills
- Self join
- Date comparison
- Previous day matching

# Solution 1:
weather['prev_temp'] = weather['temperature'].shift(1)
    weather = weather[
        (weather['temperature'] > weather['prev_temp'])
    ][['id']]
    return weather


# runtime
