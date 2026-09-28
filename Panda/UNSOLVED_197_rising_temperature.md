# 197 Rising Temperature
Weather (id, recordDate, temperature)
pk = {id}

Find the day whose temperature is higher than yesterday

## Skills
- Self join
- Date comparison
- Previous day matching

# Solution:
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
