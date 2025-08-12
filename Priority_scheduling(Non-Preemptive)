num_pro = int(input("Enter number of processes: "))
processes = []
AT = []  
BT = []  
PR = []


# Taking input for each process
for i in range(num_pro):
    processes.append(f"P{i+1}")
    at = int(input(f"Arrival time for {processes[i]}: "))
    bt = int(input(f"Burst time for {processes[i]}: "))
    pr = int(input(f"Priority for {processes[i]} : "))
    AT.append(at)
    BT.append(bt)
    PR.append(pr)


#initializing variables

comptime = [0]*num_pro
waitingtime = [0]*num_pro
TAtime = [0]*num_pro 
finished = [False]*num_pro

t = 0 
comp_count = 0 

# loop
while comp_count < num_pro:
 
    available = [i for i in range(num_pro) if AT[i] <= t and not finished[i]]
    
    if not available:
        t += 1
        continue
 #lowest PR value
 #lower value = higher priority
    idx = min(available, key=lambda x: PR[x])
    
    #np
    t += BT[idx]
    comptime[idx] = t
    finished[idx] = True
    comp_count += 1

#TAT and WT
for i in range(num_pro):
    TAtime[i] = comptime[i] - AT[i]
    waitingtime[i] = TAtime[i] - BT[i]

print("\nProcess\tAT\tBT\tPR\tCT\tTAT\tWT")
for i in range(num_pro):
    print(f"{processes[i]}\t{AT[i]}\t{BT[i]}\t{PR[i]}\t{comptime[i]}\t{TAtime[i]}\t{waitingtime[i]}")







