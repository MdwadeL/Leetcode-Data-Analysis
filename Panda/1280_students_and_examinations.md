# 1280 Students and Examinations

## Skills
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
