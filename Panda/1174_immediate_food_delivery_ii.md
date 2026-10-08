# 1174 Immediate Food Delivery II

Delivery(delivery_id, customer_id, order_date, customer_pref_delivery_date)
- PK = {delivery_id}

| delivery_id | customer_id | order_date | customer_pref_delivery_date |
| ----------- | ----------- | ---------- | --------------------------- |
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |

## Skills
- First row per group
- Conditional aggregation
- Percentage calculation

# Solution
    delivery['timing_type'] = 'scheduled'
    delivery.loc[delivery['order_date'] == delivery['customer_pref_delivery_date'], 'timing_type'] = 'immediate'

    first_order = delivery.sort_values(by=['customer_id', 'order_date']).drop_duplicates('customer_id')

    immediate_count = (first_order['timing_type'] == 'immediate').sum()
    total_orders = (first_order['timing_type']).count()

    immediate_percentage = ((immediate_count / total_orders)*100).round(2)
    immediate_percentage =  pd.DataFrame({
        'immediate_percentage' : [immediate_percentage]
    })

    return immediate_percentage
