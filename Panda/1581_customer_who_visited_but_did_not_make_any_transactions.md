# 1581 Customer Who Visited but Did Not Make Any Transactions
Find the ID of users who visit without making any transactions. Include the number of times they made these types of visits

Visits
visit_id PK = {...}
customer_id = {...}

Transaction
transaction_id PK = {...}
visit_id = {...}
amount = {...}

## Skills
- LEFT JOIN
- Missing matches
- Aggregation

# Solution
    solution = visits.merge(
        transactions,
        on='visit_id',
        how='left'
    )

    solution = solution[
        solution['transaction_id'].isnull()
    ]

    solution = solution.groupby('customer_id').agg(count_no_trans=('visit_id', 'count')).reset_index()

    return solution
### runtime: 399 ms
### memory: 68.85 MB
