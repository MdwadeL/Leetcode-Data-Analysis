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

    weather['nextDay'] = weather['recordDate'] + pd.Timedelta(days=1)

| id | recordDate | temperature | nextDay    |
| -- | ---------- | ----------- | ---------- |
| 1  | 2015-01-01 | 10          | 2015-01-02 |
| 2  | 2015-01-02 | 25          | 2015-01-03 |
| 3  | 2015-01-03 | 20          | 2015-01-04 |
| 4  | 2015-01-04 | 30          | 2015-01-05 |

<br>

    weather = weather.merge(weather, how='left', left_on='yesterdayDate', right_on='recordDate', suffixes=('', '_yest')).drop(columns=['yesterdayDate_yest'])

| id | recordDate | temperature | yesterdayDate | id_yest | recordDate_yest | temperature_yest |
| -- | ---------- | ----------- | ------------- | ------- | --------------- | ---------------- |
| 1  | 2015-01-01 | 10          | 2014-12-31    | null    | NaT             | null             |
| 2  | 2015-01-02 | 25          | 2015-01-01    | 1       | 2015-01-01      | 10               |
| 3  | 2015-01-03 | 20          | 2015-01-02    | 2       | 2015-01-02      | 25               |
| 4  | 2015-01-04 | 30          | 2015-01-03    | 3       | 2015-01-03      | 20               |

<br>

    hotter_today = weather[(weather['temperature'] > weather['temperature_yest'])]
    
| id | recordDate | temperature | yesterdayDate | id_yest | recordDate_yest | temperature_yest |
| -- | ---------- | ----------- | ------------- | ------- | --------------- | ---------------- |
| 2  | 2015-01-02 | 25          | 2015-01-01    | 1       | 2015-01-01      | 10               |
| 4  | 2015-01-04 | 30          | 2015-01-03    | 3       | 2015-01-03      | 20               |
