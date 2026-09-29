# 570 Managers with at Least 5 Direct Reports

## Skills
- Self join
- GROUP BY
- HAVING

# Solution 1:
    managed_num = employee.groupby('managerId').agg(managing_total=('managerId', 'count')).reset_index()

    managerial = employee.merge(managed_num, left_on='id', right_on='managerId', how='left').drop(columns='managerId_y')

    return managerial[(managerial['managing_total']>=5)][['name']]
### runtime: 312 ms
### memory: 68.90 MB

# Solution 2:
    managed_num = employee.groupby('managerId').agg(managing_total=('managerId', 'count')).reset_index()

    employee = employee.merge(managed_num, how='inner', left_on='id', right_on='managerId')

    return employee[employee['managing_total']>=5][['name']]
### runtime: 330 ms
### memory: 69.67 MB
