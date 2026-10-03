# 1378 Replace Employee ID With The Unique Identifier
Employees(id, name)
- PK = {id}

| id | name     |
| -- | -------- |
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |

EmployeeUNI(id, unique_id)
- PK = {id, unique_id}

| id | unique_id |
| -- | --------- |
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |

Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

### Skills
- LEFT JOIN
- Matching keys
- Missing values

# Solution
    employees = employees.set_index('id').join(employee_uni.set_index('id'), lsuffix = '_left', rsuffix='_right', how='left')

    return employees

| name     | unique_id |
| -------- | --------- |
| Alice    | null      |
| Bob      | null      |
| Meir     | 2         |
| Winston  | 3         |
| Jonathan | 1         |
