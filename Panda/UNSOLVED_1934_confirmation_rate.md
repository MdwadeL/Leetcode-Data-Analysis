# 1934 Confirmation Rate

Signups(user_id, time_stamp)
- PK = {user_id}

| user_id | time_stamp          |
| ------- | ------------------- |
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |

<br>

Confirmations(user_id, time_stamp, action)
- PK = {user_id, time_stamp}
- FK Confirmations(user_id) references Signups(user_id)
- FK Confirmations(time_stamp) references Signups(time_stamp)

| user_id | time_stamp          | action    |
| ------- | ------------------- | --------- |
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2021-02-28 23:59:59 | timeout   |

<br>

The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

Write a solution to find the confirmation rate of each user.

### Skills
- LEFT JOIN
- Conditional aggregation
- Rounding

# Solution

    num_of_confirmed = confirmations[(confirmations['action']=='confirmed')].groupby('user_id').agg(count_of_confirmed=('action', 'count')).reset_index()

| user_id | count_of_confirmed |
| ------- | ------------------ |
| 2       | 1                  |
| 7       | 3                  |

<br>

    num_of_request = confirmations.groupby('user_id').agg(count_of_request=('action', 'count')).reset_index()

| user_id | count_of_request |
| ------- | ---------------- |
| 2       | 2                |
| 3       | 2                |
| 7       | 3                |

<br>

    signups = signups.merge(num_of_confirmed, on='user_id', how='left').merge(num_of_request, on='user_id', how='left')

| user_id | time_stamp          | count_of_confirmed | count_of_request |
| ------- | ------------------- | ------------------ | ---------------- |
| 3       | 2020-03-21 10:16:13 | null               | 2                |
| 7       | 2020-01-04 13:57:59 | 3                  | 3                |
| 2       | 2020-07-29 23:09:44 | 1                  | 2                |
| 6       | 2020-12-09 10:39:37 | null               | null             |

<br>

  def fill_zero(signups):
        columns = ['count_of_confirmed', 'count_of_request']

        for col in columns:
            signups[col] = signups[col].fillna(0)
        return signups
        
  fill_zero(signups)

| user_id | time_stamp          | count_of_confirmed | count_of_request |
| ------- | ------------------- | ------------------ | ---------------- |
| 3       | 2020-03-21 10:16:13 | 0                  | 2                |
| 7       | 2020-01-04 13:57:59 | 3                  | 3                |
| 2       | 2020-07-29 23:09:44 | 1                  | 2                |
| 6       | 2020-12-09 10:39:37 | 0                  | 0                |

<br>

    signups['confirmation_rate'] = signups['count_of_confirmed'] / signups['count_of_request']
    signups['confirmation_rate'] = signups['confirmation_rate'].fillna(0)

| user_id | time_stamp          | count_of_confirmed | count_of_request | confirmation_rate |
| ------- | ------------------- | ------------------ | ---------------- | ----------------- |
| 3       | 2020-03-21 10:16:13 | 0                  | 2                | 0                 |
| 7       | 2020-01-04 13:57:59 | 3                  | 3                | 1                 |
| 2       | 2020-07-29 23:09:44 | 1                  | 2                | 0.5               |
| 6       | 2020-12-09 10:39:37 | 0                  | 0                | 0                 |

<br>

    return signups[['user_id', 'confirmation_rate']]

| user_id | confirmation_rate |
| ------- | ----------------- |
| 6       | 0                 |
| 3       | 0                 |
| 7       | 1                 |
| 2       | 0.5               |

