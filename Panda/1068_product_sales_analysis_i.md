# 1068 Product Sales Analysis I
Sales()


## Skills
- INNER JOIN
- Matching keys
- Column selection

# Solution
    products_by_year_price = product.merge(sales, on='product_id', how='inner')

the table produced will look similar to:
| product_id | product_name | sale_id | year | quantity | price |
| ---------- | ------------ | ------- | ---- | -------- | ----- |
| 100        | Nokia        | 1       | 2008 | 10       | 5000  |
| 100        | Nokia        | 2       | 2009 | 12       | 5000  |
| 200        | Apple        | 7       | 2011 | 15       | 9000  |


### runtime: ms
### memory: MB
# Solution 1
    product = product.merge(sales, on='product_id', how='left')
    product = product[
        (product['product_name'].notnull()) &
        (product['year'].notnull())
    ][['product_name', 'year', 'price']]
    
    return product
### runtime: 385 ms
### memory: 70.22 MB


# Solution 2
    product = product.merge(sales, on='product_id', how='inner')[['product_name', 'year', 'price']]
    
    return product
### runtime: 343 ms
### memory: 70.80 MB
