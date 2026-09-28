# 197 Rising Temperature
Weather (id, recordDate, temperature)
pk = {id}

Find the day whose temperature is higher than yesterday

## Skills
- Self join
- Date comparison
- Previous day matching


# Solution 1:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    weather['prevDate'] = weather['recordDate'] - pd.offsets.Day(-1)

    full_weather = weather.merge(
        weather,  how='left', 
        left_on='recordDate', right_on='prevDate', 
        suffixes=('_today', '_yesterday')
    ).drop(columns=['prevDate_today', 'prevDate_yesterday'])

    full_weather = full_weather[
        (full_weather['temperature_today'] > full_weather['temperature_yesterday'])
    ][['id_today']].rename(columns={'id_today' : 'id'})

    return full_weather
## runtime: 294 ms


# Solution 2:
This solution reads cleaner then Solution 1 by grabbing the nextDate instead of the the prevDate
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    weather['nextDate'] = weather['recordDate'] + pd.offsets.Day(1)
    
    full_weather = weather.merge(
        weather,
        how='left',
        left_on='recordDate',
        right_on='nextDate',
        suffixes=('_today', '_yesterday')
    ).drop(columns=['nextDate_today', 'nextDate_yesterday'])
    
    full_weather = full_weather[
        full_weather['temperature_today'] > full_weather['temperature_yesterday']
    ][['id_today']].rename(columns={'id_today': 'id'})
    
    return full_weather
## Runtime: 290 ms


# Solution 3:
## Passes only 8/15 testcases
    weather['prev_temp'] = weather['temperature'].shift(1)
    weather = weather[
        (weather['temperature'] > weather['prev_temp'])][['id']]
    return weather

## Fails: 
| id | recordDate | temperature |
| -- | ---------- | ----------- |
| 1  | 2000-12-16 | 3           |
| 2  | 2000-12-15 | -1          |
