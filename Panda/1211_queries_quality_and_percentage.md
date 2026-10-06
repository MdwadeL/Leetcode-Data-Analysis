# 1211 Queries Quality and Percentage

Queries(query_name, result, position, rating)

| query_name | result           | position | rating |
| ---------- | ---------------- | -------- | ------ |
| Dog        | Golden Retriever | 1        | 5      |
| Dog        | German Shepherd  | 2        | 5      |
| Dog        | Mule             | 200      | 1      |
| Cat        | Shirazi          | 5        | 2      |
| Cat        | Siamese          | 3        | 3      |
| Cat        | Sphynx           | 7        | 4      |

<br>

We define query quality as:
- The average of the ratio between query rating and its position.

We also define poor query percentage as:
- The percentage of all queries with rating less than 3.

Write a solution to find each query_name, the quality and poor_query_percentage.
Both quality and poor_query_percentage should be rounded to 2 decimal places

## Skills
- GROUP BY
- Conditional aggregation
- Rounding

# Solution
    queries['quality'] = queries['rating'] / queries['position']
    queries['poor'] = (queries['rating'] < 3).astype(int)

    stats = queries.groupby('query_name').agg(
        quality=('quality', 'mean'),
        poor_query_percentage=('poor', 'mean')
    ).reset_index()

    stats['quality'] = (stats['quality'] + 1e-9).round(2)

    stats['poor_query_percentage'] = (
        stats['poor_query_percentage'] * 100 + 1e-9
    ).round(2)

    return stats

| query_name | quality | poor_query_percentage |
| ---------- | ------- | --------------------- |
| Dog        | 2.5     | 33.33                 |
| Cat        | 0.66    | 33.33                 |
