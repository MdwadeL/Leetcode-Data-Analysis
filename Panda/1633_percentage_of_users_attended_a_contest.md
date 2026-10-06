# 1633 Percentage of Users Attended a Contest

Users(user_id, user_name)
- PK = {user_id}

| user_id | user_name |
| ------- | --------- |
| 6       | Alice     |
| 2       | Bob       |
| 7       | Alex      |

<br>

Register(contest_id, user_id)
- PK = {contest_id, user_id}
- FK = Register(user_id) references Users(user_id)

| contest_id | user_id |
| ---------- | ------- |
| 215        | 6       |
| 209        | 2       |
| 208        | 2       |
| 210        | 6       |
| 208        | 6       |
| 209        | 7       |
| 209        | 6       |
| 215        | 7       |
| 208        | 7       |
| 210        | 2       |
| 207        | 2       |
| 210        | 7       |

Write a solution to find the percentage of the users registered in each contest rounded to two decimals.

Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order

## Skills
- COUNT DISTINCT
- Percentage calculation
- Sorting results

# Solution
    registery = register.groupby('contest_id').agg(count_of_registered=('user_id', 'count')).reset_index()

    total_users = users['user_id'].nunique()

    registery['percentage'] = ((registery['count_of_registered'] / total_users) * 100).round(2)

    registery = registery.sort_values(by=['percentage', 'contest_id'],ascending=[False, True])

    return registery[['contest_id', 'percentage']]

| contest_id | percentage |
| ---------- | ---------- |
| 208        | 100        |
| 209        | 100        |
| 210        | 100        |
| 215        | 66.67      |
| 207        | 33.33      |
