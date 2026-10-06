# 1251 Average Selling Price

Prices(product_id, start_date, end_date, price)
- PK = {product_id, start_date, end_date,}

| product_id | start_date | end_date   | price |
| ---------- | ---------- | ---------- | ----- |
| 1          | 2019-02-17 | 2019-02-28 | 5     |
| 1          | 2019-03-01 | 2019-03-22 | 20    |
| 2          | 2019-02-01 | 2019-02-20 | 15    |
| 2          | 2019-02-21 | 2019-03-31 | 30    |

<br>

UnitsSold(product_id, purchase_date, units)
- FK = UnitsSold(product_id) references Prices(product_id)

| product_id | purchase_date | units |
| ---------- | ------------- | ----- |
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |

<br>

Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places. If a product does not have any sold units, its average selling price is assumed to be 0.

## Skills
- Date range join
- Weighted average
- NULL handling

# Solution

    sales = prices.merge(units_sold, how='outer', on='product_id')
    
    sales = sales[
        (
            (sales['purchase_date'] <= sales['end_date']) &
            (sales['purchase_date'] >= sales['start_date'])
        ) |
        sales['purchase_date'].isnull()
    ]

    sales['units'] = sales['units'].fillna(0)

    sales['revenue'] = sales['price'] * sales['units']

    stats = sales.groupby('product_id').agg(
        total_units=('units', 'sum'),
        total_revenue=('revenue', 'sum')
    ).reset_index()

    stats['average_price'] = (stats['total_revenue'] / stats['total_units']).round(2)

    stats.loc[stats['total_units'] == 0, 'average_price'] = 0

    return stats[['product_id', 'average_price']]

| product_id | average_price |
| ---------- | ------------- |
| 1          | 6.96          |
| 2          | 16.96         |
