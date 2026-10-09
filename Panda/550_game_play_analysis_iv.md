# 550 Game Play Analysis IV

Activity(player_id, device_id, event_date, games_played)
- PK = {player_id, event_date}

| player_id | device_id | event_date | games_played |
| --------- | --------- | ---------- | ------------ |
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |

<br>

Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to determine the number of players who logged in on the day immediately following their initial login, and divide it by the number of total players.

## Skills
- First login per player
- Date arithmetic
- Retention rate

# Solution
    first_logins = activity.groupby('player_id')['event_date'].min().reset_index()
    first_logins['after_first_log_date'] = first_logins['event_date'] + pd.Timedelta(days=1)

    freq_logs = activity.merge(first_logins, how='left', left_on=['player_id', 'event_date'], right_on=['player_id', 'after_first_log_date'])

    freq_logs = freq_logs[(freq_logs['after_first_log_date'].notnull())][['player_id']].count()

    total_logs = activity['player_id'].drop_duplicates().count()
    
    retention_rate = (freq_logs / total_logs).round(2)

| fraction |
| -------- |
| 0.33     |
    frequency = pd.DataFrame({
        'fraction' : retention_rate
    })

    return frequency
