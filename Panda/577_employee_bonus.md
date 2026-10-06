# 577 Employee Bonus
Employee(empId, name, supervisor, salary)
- PK = {empId}

| empId | name   | supervisor | salary |
| ----- | ------ | ---------- | ------ |
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |

<br>

Bonus(empId, bonus)
- PK = {empId}
- FK = Bonus(empId) references Employee(empId)

| empId | bonus |
| ----- | ----- |
| 2     | 500   |
| 4     | 2000  |

<br>

Write a solution to report the name and bonus amount of each employee who satisfies either of the following:
- The employee has a bonus less than 1000.
- The employee did not get any bonus.
<br>

## Skills
- LEFT JOIN
- NULL handling
- Filtering

# Solution

    employee = employee.merge(bonus, on='empId', how='left')
    
| empId | name   | supervisor | salary | bonus |
| ----- | ------ | ---------- | ------ | ----- |
| 3     | Brad   | null       | 4000   | null  |
| 1     | John   | 3          | 1000   | null  |
| 2     | Dan    | 3          | 2000   | 500   |
| 4     | Thomas | 3          | 4000   | 2000  |

<br>
    employee['bonus'] = employee['bonus'].fillna(0)

| empId | name   | supervisor | salary | bonus |
| ----- | ------ | ---------- | ------ | ----- |
| 3     | Brad   | null       | 4000   | 0     |
| 1     | John   | 3          | 1000   | 0     |
| 2     | Dan    | 3          | 2000   | 500   |
| 4     | Thomas | 3          | 4000   | 2000  |

<br>

    employee['payout'] =employee['salary'] + employee['bonus']

| empId | name   | supervisor | salary | bonus | payout |
| ----- | ------ | ---------- | ------ | ----- | ------ |
| 3     | Brad   | null       | 4000   | 0     | 4000   |
| 1     | John   | 3          | 1000   | 0     | 1000   |
| 2     | Dan    | 3          | 2000   | 500   | 2500   |
| 4     | Thomas | 3          | 4000   | 2000  | 6000   |

<br>

    return employee[(employee['bonus']<1000)][['name', 'bonus']]
    
| name | bonus |
| ---- | ----- |
| Brad | 0     |
| John | 0     |
| Dan  | 500   |
