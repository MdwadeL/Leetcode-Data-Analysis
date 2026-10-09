# 2356 Number of Unique Subjects Taught by Each Teacher

Teacher(teacher_id, subject_id, dept_id)
- PK = {teacher_id, dept_id}

| teacher_id | subject_id | dept_id |
| ---------- | ---------- | ------- |
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |

<br>

Write a solution to calculate the number of unique subjects each teacher teaches in the university.

## Skills
- GROUP BY
- COUNT DISTINCT

# Solution

    teacher_teaching_count = teacher.drop_duplicates(['teacher_id', 'subject_id']).groupby(['teacher_id']).agg(cnt=('subject_id', 'count')).reset_index()
    return teacher_teaching_count

| teacher_id | cnt |
| ---------- | --- |
| 1          | 2   |
| 2          | 4   |
