# 577 Employee Bonus
Employee(empId, name, supervisor, salary)
PK = {empId}

Bonus(empId, bonus)
PK = {empId}
FK = Bonus(empId) references Employee(empId)

Write a solution to report the name and bonus amount of each employee who satisfies either of the following:
- The employee has a bonus less than 1000.
- The employee did not get any bonus.
## Skills
- LEFT JOIN
- NULL handling
- Filtering

# Solution
    payout = employee.merge(bonus, on='empId', how='left')
    payout = payout[
        (payout['bonus'] < 1000) |
        (payout['bonus'].isnull())
    ][['name', 'bonus']]

    return payout
### runtime: 316 ms
### memory: 68.56 MB
