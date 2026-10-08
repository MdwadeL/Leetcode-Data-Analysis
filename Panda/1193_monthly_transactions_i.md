# 1193 Monthly Transactions I

Transactions(id, country, state, amount, trans_date)
- PK = {id}

| id  | country | state    | amount | trans_date |
| --- | ------- | -------- | ------ | ---------- |
| 121 | US      | approved | 1000   | 2018-12-18 |
| 122 | US      | declined | 2000   | 2018-12-19 |
| 123 | US      | approved | 2000   | 2019-01-01 |
| 124 | DE      | approved | 2000   | 2019-01-07 |

<br>

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

## Skills
- Date grouping
- Conditional aggregation
- GROUP BY

# Solution
    
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    transactions['country'] = transactions['country'].fillna('Unknown')

    month_country_stats = transactions.groupby(['month', 'country']).agg(trans_count=('trans_date', 'count'), approved_count=('state', lambda x: (x== 'approved').sum()), trans_total_amount=('amount', 'sum')).reset_index()

    approved_sum = transactions[(transactions['state']=='approved')].groupby(['month', 'country']).agg(approved_total_amount=('amount', 'sum')).reset_index()

    month_country_stats = month_country_stats.merge(approved_sum, how='left', on=('month', 'country'))
    month_country_stats['approved_total_amount'] = month_country_stats['approved_total_amount'].fillna(0)

    month_country_stats['country'] = month_country_stats['country'].replace('Unknown', pd.NA)
    return month_country_stats

| month   | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
| ------- | ------- | ----------- | -------------- | ------------------ | --------------------- |
| 2018-12 | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01 | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01 | DE      | 1           | 1              | 2000               | 2000                  |
