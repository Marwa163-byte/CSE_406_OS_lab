n=int(input("Enter no of processes:"))
processes=[]
for i in range(n):
  pid = f'p{i+1}'
  at=int(input(f"Enter arrival time for {pid}:"))
  bt=int(input(f"Enter burst time for {pid}:"))
  processes.append({'PID':pid,'AT':at,'BT':bt})
time = 0
completed=[]
while len(completed) < n:
    ready = [p for p in processes if p['AT'] <= time and 'CT' not in p]
    if not ready:
        time += 1
        continue
    current = min(ready, key=lambda x: x['BT'])
    time += current['BT']
    current['CT'] = time
    current['TAT'] = current['CT'] - current['AT']
    current['WT'] = current['TAT'] - current['BT']
    completed.append(current)
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
total_WT = total_tat = 0
for p in processes:
  print(f"{p['PID']}\t{p['AT']}\t{p['BT']}\t{p['CT']}\t{p['TAT']}\t{p['WT']}")
  total_WT+=p['WT']
  total_tat+=p['TAT']
print(f"Average Waiting Time: {total_WT/n}")
print(f"Average Turnaround Time: {total_tat/n}")

