# 570 Managers with at Least 5 Direct Reports

Manager(id, name, department, managerId)
- PK = {id}

| id  | name  | department | managerId |
| --- | ----- | ---------- | --------- |
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |

<br>

Write a solution to find managers with at least five direct reports.


## Skills
- Self join
- GROUP BY
- HAVING

# Solution:

    num_of_emps_managed = employee.groupby('managerId').agg(num_employees_managed=('managerId', 'count')).reset_index().rename(columns={'managerId' : 'id'})

| id  | num_employees_managed |
| --- | --------------------- |
| 101 | 5                     |

<br>

    employee = employee.merge(num_of_emps_managed, on='id', how='left')

| id  | name  | department | managerId | num_employees_managed |
| --- | ----- | ---------- | --------- | --------------------- |
| 101 | John  | A          | null      | 5                     |
| 102 | Dan   | A          | 101       | null                  |
| 103 | James | A          | 101       | null                  |
| 104 | Amy   | A          | 101       | null                  |
| 105 | Anne  | A          | 101       | null                  |
| 106 | Ron   | B          | 101       | null                  |

<br>

    return employee[(employee['num_employees_managed'] > 4)][['name']]

| name |
| ---- |
| John |

