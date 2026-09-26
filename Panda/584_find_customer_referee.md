# 584 Find Customer Referee.py
    id PK = {...id of customer}
    name = {...name of customer}
    referee_id = {...id of who referrence customer}

    find the names of customers who were referenced by no one and customer's id that isn't 2
    
## Skills:
- Filtering rows
- NULL handling
- Boolean OR

# Solution 1
    solution = customer[
        (customer['referee_id'] != 2) |
        (customer['referee_id']).isnull()
    ][['name']]

    return solution
## runtime: 243ms


# Solution 2
        return customer[ (customer['referee_id'] != 2) | (customer['referee_id']).isnull() ][['name']]
## runtime: 217ms
