# 1378 Replace Employee ID With The Unique Identifier
Employees:
        id PK= {...}
        name = {...}

    EmployeeUNI:
        id PK = {...}
        unique_id PK = {...}

    Show the [unique_id] of each [id] in employee, if none exist then show null
## Skills
- LEFT JOIN
- Matching keys
- Missing values

# Solution 1
    return employees.merge(employee_uni, on='id', how='left').drop(columns='id')
### runtime: 346 ms
### memory: 67.39 MB

# Solution 2
    employees = employees.merge(employee_uni, on='id', how='left')
    return employees[['unique_id', 'name']]
### runtime: 306
### memory: 67.93 MB
