# 620 Not Boring Movies
Cinema(id, movie, description, rating)
- PK = {id}

| id | movie      | description | rating |
| -- | ---------- | ----------- | ------ |
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |

<br>

Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".
Return the result table ordered by rating in descending order

## Skills
- Filtering rows
- Odd and even numbers
- Sorting results

### Solution

    odd_id_not_boring = cinema[((cinema['id'] % 2) == 1) & (cinema['description'] != 'boring')].sort_values(by='rating', ascending=False)

| id | movie      | description | rating |
| -- | ---------- | ----------- | ------ |
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |
