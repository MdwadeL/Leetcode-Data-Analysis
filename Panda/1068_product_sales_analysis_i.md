# 1068 Product Sales Analysis I

## Skills
- INNER JOIN
- Matching keys
- Column selection

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
