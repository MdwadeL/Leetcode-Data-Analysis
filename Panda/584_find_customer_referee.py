"""
584 Find Customer Referee.py
    # id PK = {...id of customer}
    # name = {...name of customer}
    # referee_id = {...id of who referrence customer}

    # inf products that are low fat AND recycable
    
Skills:
- boolean filtering
- null handling

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:

"""

# Solution 1
    solution = customer[
        (customer['referee_id'] != 2) |
        (customer['referee_id']).isnull()
    ][['name']]

    return solution
# runtime: 243ms


# Solution 2
        return customer[ (customer['referee_id'] != 2) | (customer['referee_id']).isnull() ][['name']]
# runtime: 217ms
