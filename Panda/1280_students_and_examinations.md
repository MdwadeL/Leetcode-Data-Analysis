# 1280 Students and Examinations
Students(student_id, student_name)
- PK = {student_id}

Subjects(subject_name)
- PK = {subject_name}
  
Examinations(student_id, subject_name)
- FK = {student_id} references Students(student_id)
- FK = {subject_name} references Subjects(subject_name)

| student_id | student_name |
| ---------- | ------------ |
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |

| subject_name |
| ------------ |
| Math         |
| Physics      |
| Programming  |

| student_id | subject_name |
| ---------- | ------------ |
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
| 13         | Math         |
| 13         | Programming  |
| 13         | Physics      |
| 2          | Math         |
| 1          | Math         |

### Skills
- CROSS JOIN
- LEFT JOIN
- COUNT
- GROUP BY

# Solution 1:
    import numpy as np

    exam_count = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams=('student_id', 'count')).reset_index()

    scheduled = students.merge(subjects, how='cross')

    taken_test = scheduled.merge(exam_count, on=['student_id', 'subject_name'], how='left').sort_values(by=['student_id', 'subject_name'])
    
    taken_test['attended_exams'] = taken_test['attended_exams'].replace(np.nan, 0)

    return taken_test
### runtime: 365 ms
### memory: 69.19 MB
