# 1757 Recyclable and Low Fat Products

products(product_id, low_fats, recyclable)
- PK = {product_id}
<br>

| product_id | low_fats | recyclable |
| ---------- | -------- | ---------- |
| 0          | Y        | N          |
| 1          | Y        | Y          |
| 2          | N        | Y          |
| 3          | Y        | Y          |
| 4          | N        | N          |

<br>

Write a solution to find the ids of products that are both low fat and recyclable.

    
## Skills:
- Filtering rows
- Multiple conditions
- Boolean AND

# Solution 

    lowfat_and_recyclable = products[
        (products['low_fats'] == 'Y') &
        (products['recyclable'] == 'Y')
    ]

    return lowfat_and_recyclable[['product_id']]

| product_id |
| ---------- |
| 1          |
| 3          |
