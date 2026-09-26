# 1148 Article Views I
Find the authors who viewed their own books.

author_id and viewer_id come from the same independent values

## Skills
- Boolean Filtering/Indexing
- Column Selection
- Deduplication
- Sorting
- Renaming and Conversion

# Solution 1
    views = views[
        (views['author_id'] == views['viewer_id'])
    ].drop(columns=['view_date', 'article_id', 'viewer_id']).rename(columns=({"author_id" : "id"})).drop_duplicates().sort_values(by=['id'])

    return views
## runtime: 265 ms

# Solution 2
    drop_cols = ['view_date', 'article_id', 'viewer_id']
    
    views = views[
        (views['author_id'] == views['viewer_id'])
    ]
    
    views = views.drop(columns=drop_cols).drop_duplicates()
    views = views.rename(columns=({"author_id" : "id"}))
    views = views.sort_values(by=['id'])

    return views
## runtime: 261 ms
