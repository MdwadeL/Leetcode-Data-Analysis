# 1075 Project Employees I

Project(project_id, employee_id)
- PK = {project_id, employee_id}

| project_id | employee_id |
| ---------- | ----------- |
| 1          | 1           |
| 1          | 2           |
| 1          | 3           |
| 2          | 1           |
| 2          | 4           |

<br>

Employee(employee_id, name, experience_years)
- PK = {employee_id}
- FK = Employee(employee_id) references Project(employee_id)

| employee_id | name   | experience_years |
| ----------- | ------ | ---------------- |
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |

Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

## Skills
- INNER JOIN
- GROUP BY
- AVG
- Rounding

### Solution

    project = project.merge(employee, on='employee_id', how='left')

    average_experience_years = project.groupby('project_id').agg(average_years=('experience_years', 'mean')).round(2).reset_index()

    return average_experience_years

| project_id | average_years |
| ---------- | ------------- |
| 1          | 2             |
| 2          | 2.5           |
