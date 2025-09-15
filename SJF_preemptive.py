# Preemptive Shortest Job First (SRTF) Scheduling

n = int(input("Enter number of processes: "))

processes = []
for i in range(n):
    pid = f'P{i+1}'
    at = int(input(f"Enter Arrival Time ({pid}): "))
    bt = int(input(f"Enter Burst Time ({pid}): "))
    processes.append({'PID': pid, 'AT': at, 'BT': bt, 'RT': bt})  # RT = Remaining Time

time = 0
completed = []
while len(completed) < n:
    # Find processes that have arrived and are not finished
    ready = [p for p in processes if p['AT'] <= time and p['RT'] > 0]

    if not ready:
        time += 1
        continue

    # Select the process with shortest remaining time
    current = min(ready, key=lambda x: x['RT'])

    # Run it for 1 unit of time
    current['RT'] -= 1
    time += 1

    # If finished, record completion, TAT, WT
    if current['RT'] == 0:
        current['CT'] = time
        current['TAT'] = current['CT'] - current['AT']
        current['WT'] = current['TAT'] - current['BT']
        completed.append(current)

# Print results
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
total_wt = total_tat = 0
for p in processes:
    print(f"{p['PID']}\t{p['AT']}\t{p['BT']}\t{p['CT']}\t{p['TAT']}\t{p['WT']}")
    total_wt += p['WT']
    total_tat += p['TAT']

print(f"\nAverage Waiting Time: {(total_wt/n):.2f}")
print(f"Average Turnaround Time: {(total_tat/n):.2f}")
