# 584 Find Customer Referee
Customer(id, name, referee_id)
- PK = {id}

| id | name | referee_id |
| -- | ---- | ---------- |
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |

<br>

Find the names of the customer that are either:
- referred by any customer with id != 2.
- not referred by any customer.
    
## Skills:
- Filtering rows
- NULL handling
- Boolean OR

# Solution 

    return customer[ (customer['referee_id'] != 2) | (customer['referee_id']).isnull() ][['name']]

| name |
| ---- |
| Will |
| Jane |
| Bill |
| Zack |
