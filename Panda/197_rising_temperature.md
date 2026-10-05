# 197 Rising Temperature
Weather (id, recordDate, temperature)
- pk = {id}

| id | recordDate | temperature |
| -- | ---------- | ----------- |
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |

<br>

Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

## Skills
- Self join
- Date comparison
- Previous day matching


# Solution

    weather['yesterdayDate'] = weather['recordDate'] - pd.Timedelta(days=1)

| id | recordDate | temperature | yesterdayDate |
| -- | ---------- | ----------- | ------------- |
| 1  | 2015-01-01 | 10          | 2014-12-31    |
| 2  | 2015-01-02 | 25          | 2015-01-01    |
| 3  | 2015-01-03 | 20          | 2015-01-02    |
| 4  | 2015-01-04 | 30          | 2015-01-03    |

<br>

    weather = weather.merge(weather, how='left', left_on='yesterdayDate', right_on='recordDate', suffixes=('_tdy', '_yest')).drop(columns=['recordDate_yest', 'yesterdayDate_yest'])

| id_tdy | recordDate_tdy | temperature_tdy | yesterdayDate_tdy | id_yest | temperature_yest |
| ------ | -------------- | --------------- | ----------------- | ------- | ---------------- |
| 1      | 2015-01-01     | 10              | 2014-12-31        | null    | null             |
| 2      | 2015-01-02     | 25              | 2015-01-01        | 1       | 10               |
| 3      | 2015-01-03     | 20              | 2015-01-02        | 2       | 25               |
| 4      | 2015-01-04     | 30              | 2015-01-03        | 3       | 20               |




