# 1068 Product Sales Analysis I
Sales(sales_id, product_id, year, quantity_ price)
- PK = {sales_id, year}
- FK = {product_id} REFERENCES Product(product_id)

Product(product_id, product_name)
- PK = {product_id

### Sales:
| sale_id | product_id | year | quantity | price |
| ------- | ---------- | ---- | -------- | ----- |
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |

### Product:
| product_id | product_name |
| ---------- | ------------ |
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |

Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

## Skills
- INNER JOIN
- Matching keys
- Column selection

# Solution
    product_sales_table = product.merge(sales, on='product_id', how='inner')

the table produced will look similar to:
| sale_id | product_id | product_name | year | quantitiy | price |
| ------- | ---------- | ------------ | ---- | --------- | ----- |
| 1       | 100        | Nokia        | 2008 | null      | 5000  |
| 2       | 100        | Nokia        | 2009 | null      | 5000  |
| 7       | 200        | Apple        | 2011 | null      | 9000  |

    products_year_price = product_sales_table[['product_name', 'year', 'price']]
    return products_year_price
    
Produces:
| product_name | year | price |
| ------------ | ---- | ----- |
| Nokia        | 2008 | 5000  |
| Nokia        | 2009 | 5000  |
| Apple        | 2011 | 9000  |
