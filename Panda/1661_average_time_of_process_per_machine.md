# 1661 Average Time of Process per Machine
    Activity(machine_id, process_id, activity_type, timestamp)
        pk = {machine_id, process_id, activity_type}
        
        machine_id (int): ID of a machine
        process_id (int): ID of the process running on the machine
        activity_type (enum): start or end
        timestamp (float): the current time in seconds

For each process_id + activity_type(start) < process_id + activity_type(end)

Find the average time each machine takes to complete a process. Round the time to 3 decimals
    
## Skills
- Self join
- Timestamp differences
- GROUP BY
- Rounding

# Solution:
    processed = activity.merge(
        activity, on=('machine_id', 'process_id'), how='left',
        suffixes=('_start', '_end')
        )
    processed = processed[
        (processed['activity_type_start'] != processed['activity_type_end']) &
        (processed['activity_type_start'] > processed['activity_type_end'])
    ]

    processed['running_time'] = processed['timestamp_end'] - processed['timestamp_start']

    avg_processed = processed[['machine_id', 'running_time']].groupby('machine_id').agg(processing_time=('running_time', 'mean')).round(3).reset_index()

    return avg_processed
## runtime: 299
