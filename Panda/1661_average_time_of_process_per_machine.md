# 1661 Average Time of Process per Machine
Activity(machine_id, process_id, activity_type, timestamp)
- PK = {machine_id, process_id, activity_type}

| machine_id | process_id | activity_type | timestamp |
| ---------- | ---------- | ------------- | --------- |
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.52      |
| 0          | 1          | start         | 3.14      |
| 0          | 1          | end           | 4.12      |
| 1          | 0          | start         | 0.55      |
| 1          | 0          | end           | 1.55      |
| 1          | 1          | start         | 0.43      |
| 1          | 1          | end           | 1.42      |
| 2          | 0          | start         | 4.1       |
| 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.5       |
| 2          | 1          | end           | 5         |

<br>

There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.

The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.
    
## Skills
- Self join
- Timestamp differences
- GROUP BY
- Rounding

# Solution:
    activity_full = activity.merge(activity, how='inner', on=['machine_id', 'process_id'], suffixes=('_start', '_end'))

    activity_full = activity_full[
        (activity_full['activity_type_start'] != activity_full['activity_type_end']) &
        (activity_full['activity_type_start'] > activity_full['activity_type_end'])
    ]

| machine_id | process_id | activity_type_start | timestamp_start | activity_type_end | timestamp_end |
| ---------- | ---------- | ------------------- | --------------- | ----------------- | ------------- |
| 0          | 0          | start               | 0.712           | end               | 1.52          |
| 0          | 1          | start               | 3.14            | end               | 4.12          |
| 1          | 0          | start               | 0.55            | end               | 1.55          |
| 1          | 1          | start               | 0.43            | end               | 1.42          |
| 2          | 0          | start               | 4.1             | end               | 4.512         |
| 2          | 1          | start               | 2.5             | end               | 5             |

<br>

    activity_full['time_elapsed'] = (activity_full['timestamp_end'] - activity_full['timestamp_start'])

| machine_id | process_id | activity_type_start | timestamp_start | activity_type_end | timestamp_end | time_elapsed |
| ---------- | ---------- | ------------------- | --------------- | ----------------- | ------------- | ------------ |
| 0          | 0          | start               | 0.712           | end               | 1.52          | 0.808        |
| 0          | 1          | start               | 3.14            | end               | 4.12          | 0.98         |
| 1          | 0          | start               | 0.55            | end               | 1.55          | 1            |
| 1          | 1          | start               | 0.43            | end               | 1.42          | 0.99         |
| 2          | 0          | start               | 4.1             | end               | 4.512         | 0.412        |
| 2          | 1          | start               | 2.5             | end               | 5             | 2.5          |

<br>

    avg_machine_time = activity_full.groupby('machine_id').agg(processing_time=('time_elapsed', 'mean')).round(3).reset_index()

| machine_id | processing_time |
| ---------- | --------------- |
| 0          | 0.894           |
| 1          | 0.995           |
| 2          | 1.456           |
