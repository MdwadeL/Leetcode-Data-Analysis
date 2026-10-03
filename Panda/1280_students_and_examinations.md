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

# Solution:
    import numpy as np
    
    exam_attedance_count = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams=('student_id', 'count')).reset_index()
| student_id | subject_name | attended_exams |
| ---------- | ------------ | -------------- |
| 1          | Math         | 3              |
| 1          | Physics      | 2              |
| 1          | Programming  | 1              |
| 2          | Math         | 1              |
| 2          | Programming  | 1              |
| 13         | Math         | 1              |
| 13         | Physics      | 1              |
| 13         | Programming  | 1              |

<br>

    scheduled = students.merge(subjects, how='cross')
| student_id | student_name | subject_name |
| ---------- | ------------ | ------------ |
| 1          | Alice        | Math         |
| 1          | Alice        | Physics      |
| 1          | Alice        | Programming  |
| 2          | Bob          | Math         |
| 2          | Bob          | Physics      |
| 2          | Bob          | Programming  |
| 13         | John         | Math         |
| 13         | John         | Physics      |
| 13         | John         | Programming  |
| 6          | Alex         | Math         |
| 6          | Alex         | Physics      |
| 6          | Alex         | Programming  |

    taken_test = scheduled.merge(exam_attedance_count, on=['student_id', 'subject_name'], how='left').sort_values(by=['student_id', 'subject_name'])

produces:
| student_id | student_name | subject_name | attended_exams |
| ---------- | ------------ | ------------ | -------------- |
| 1          | Alice        | Math         | 3              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 1              |
| 2          | Bob          | Physics      | null           |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | null           |
| 6          | Alex         | Physics      | null           |
| 6          | Alex         | Programming  | null           |
| 13         | John         | Math         | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Programming  | 1              |

    taken_test['attended_exams'] = taken_test['attended_exams'].replace(np.nan, 0)
    
returns:
| student_id | student_name | subject_name | attended_exams |
| ---------- | ------------ | ------------ | -------------- |
| 1          | Alice        | Math         | 3              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 1              |
| 2          | Bob          | Physics      | 0              |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | 0              |
| 6          | Alex         | Physics      | 0              |
| 6          | Alex         | Programming  | 0              |
| 13         | John         | Math         | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Programming  | 1              |
