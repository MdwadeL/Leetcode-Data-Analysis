# 1148 Article Views I
Views(article_id, author_id, viewer_id, view_date)

### Views
| article_id | author_id | viewer_id | view_date  |
|------------|-----------|-----------|------------|
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |

Find the authors who viewed their own books.

## Skills
- Boolean Filtering/Indexing
- Column Selection
- Deduplication
- Sorting
- Renaming and Conversion

# Solution
    author_view_themselves = views[
        (views['author_id'] == views['viewer_id'])
    ].drop_duplicates(['author_id', 'viewer_id']).sort_values(by='author_id').rename(columns={'author_id' : 'id'})

| article_id | id | viewer_id | view_date  |
| ---------- | -- | --------- | ---------- |
| 3          | 4  | 4         | 2019-07-21 |
| 2          | 7  | 7         | 2019-08-01 |

<br>
    return author_view_themselves[['id']]
<b>returns:</b>
| id |
| -- |
| 4  |
| 7  |
