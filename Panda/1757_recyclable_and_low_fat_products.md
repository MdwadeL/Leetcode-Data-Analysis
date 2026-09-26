# 1757 Recyclable and Low Fat Products

    product_id PK = {...}
    low_fats (catg) = {Y, N}
    recyclable (catg) = {Y, N}

    find products that are low fat AND recycable
    
## Skills:
- basic filtering
- dataframe manipulation

# Solution 1
    products = products[
        (products['low_fats'] == 'Y') &
        (products['recyclable'] == 'Y')
    ]

    products = products[['product_id']]

    return products
## runtime: 299ms


# Solution 2
    products = products[
        (products['low_fats'] == 'Y') &
        (products['recyclable'] == 'Y')
    ].drop(columns=['low_fats', 'recyclable'])

    return products
## runtime: 256


# Solution 3
    return products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')][['product_id']]
## runtime: 236
