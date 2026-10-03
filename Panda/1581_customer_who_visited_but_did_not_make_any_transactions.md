# 1581 Customer Who Visited but Did Not Make Any Transactions

Visits(visit_id, customer_id)
- PK = visit_id

| visit_id | customer_id |
| -------- | ----------- |
| 1        | 23          |
| 2        | 9           |
| 4        | 30          |
| 5        | 54          |
| 6        | 96          |
| 7        | 54          |
| 8        | 54          |

<br>

Transaction(transaction_id, visit_id, amount)
- PK = {transaction_id}
- FK = {visit_id} references Visits(visit_id)

| transaction_id | visit_id | amount |
| -------------- | -------- | ------ |
| 2              | 5        | 310    |
| 3              | 5        | 300    |
| 9              | 5        | 200    |
| 12             | 1        | 910    |
| 13             | 2        | 970    |

<br>
Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

## Skills
- LEFT JOIN
- Missing matches
- Aggregation

# Solution
    visit_transactions_frame = visits.merge(transactions, how='left', on='visit_id')
    
| visit_id | customer_id | transaction_id | amount |
| -------- | ----------- | -------------- | ------ |
| 1        | 23          | 12             | 910    |
| 2        | 9           | 13             | 970    |
| 4        | 30          | null           | null   |
| 5        | 54          | 2              | 310    |
| 5        | 54          | 3              | 300    |
| 5        | 54          | 9              | 200    |
| 6        | 96          | null           | null   |
| 7        | 54          | null           | null   |
| 8        | 54          | null           | null   |

<br>

    no_transactions = visit_transactions_frame[visit_transactions_frame['transaction_id'].isnull()]

| visit_id | customer_id | transaction_id | amount |
| -------- | ----------- | -------------- | ------ |
| 4        | 30          | null           | null   |
| 6        | 96          | null           | null   |
| 7        | 54          | null           | null   |
| 8        | 54          | null           | null   |

<br>

    return no_transactions.groupby(['customer_id']).agg(count_no_trans=('visit_id', 'count')).reset_index()

| customer_id | count_no_trans |
| ----------- | -------------- |
| 30          | 1              |
| 54          | 2              |
| 96          | 1              |
