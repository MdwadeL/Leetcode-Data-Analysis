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
    views = views[
        (views['author_id'] == views['viewer_id'])
    ].drop(columns=['view_date', 'article_id', 'viewer_id']).rename(columns=({"author_id" : "id"})).drop_duplicates().sort_values(by=['id'])

    return views
