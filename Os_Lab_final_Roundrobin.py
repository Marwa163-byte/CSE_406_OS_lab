num_processes = int(input("Enter process no : "))
processes = []
AT = []
BT = []


for i in range(num_processes):
    processes.append(f"P{i+1}")
    at = int(input(f"Arrival time for process {processes[i]}: "))
    bt = int(input(f"Burst time for process {processes[i]}: "))
    AT.append(at)
    BT.append(bt)


time_quant = int(input("Enter time quant: "))


remain_bt = BT[:]
comptime = [0]*num_processes
waitingtime = [0]*num_processes
TAtime = [0]*num_processes

t=0
r_que = []
visited = [False]*num_processes

while True:
# Add arrived processes
    for i in range(num_processes):
        if AT[i] <= t and not visited[i]:
            r_que.append(i)
            visited[i] = True
#r que any execute
    if r_que:
        idx = r_que.pop(0)
#WHEN remain  btime more than quant time
        if remain_bt[idx] > time_quant:
            t += time_quant
            remain_bt[idx] -= time_quant
        else:
#when rem bt less or equal to quant time         
            t += remain_bt[idx]
            remain_bt[idx] = 0
            comptime[idx] = t
 #newly arrived
        for i in range(num_processes):
            if AT[i] <= t and not visited[i]:
                r_que.append(i)
                visited[i] = True

#process burst time left
        if remain_bt[idx] > 0:
            r_que.append(idx)
    else:
 
        t += 1

    if all(bt == 0 for bt in remain_bt):
        break
for i in range(num_processes):
    TAtime[i] = comptime[i] - AT[i]
    waitingtime[i] = TAtime[i] - BT[i]

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(num_processes):
  print(f"{processes[i]}\t{AT[i]}\t{BT[i]}\t{comptime[i]}\t{TAtime[i]}\t{waitingtime[i]}")
  
