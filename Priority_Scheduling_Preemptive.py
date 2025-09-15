num_pro = int(input("Enter number of processes: "))

processes = []
AT = []  
BT = []  
PR = []

# Input for each process
for i in range(num_pro):
    processes.append(f"P{i+1}")
    at = int(input(f"Arrival time for {processes[i]}: "))
    bt = int(input(f"Burst time for {processes[i]}: "))
    pr = int(input(f"Priority for {processes[i]} : "))
    AT.append(at)
    BT.append(bt)
    PR.append(pr)

# Initialize variables
RT = BT.copy()            # Remaining Time for each process
comptime = [0]*num_pro    # Completion Time
finished = [False]*num_pro
TAtime = [0]*num_pro      # Turnaround Time
waitingtime = [0]*num_pro

t = 0
comp_count = 0

# Loop until all processes are completed
while comp_count < num_pro:
    # Find all processes that have arrived and are not finished
    available = [i for i in range(num_pro) if AT[i] <= t and RT[i] > 0]
    
    if not available:
        t += 1
        continue
    
    # Pick the process with highest priority (lowest PR value)
    idx = min(available, key=lambda x: PR[x])
    
    # Execute the process for 1 time unit
    RT[idx] -= 1
    t += 1
    
    # If process finishes
    if RT[idx] == 0:
        comptime[idx] = t
        finished[idx] = True
        comp_count += 1

# Calculate TAT and WT
for i in range(num_pro):
    TAtime[i] = comptime[i] - AT[i]
    waitingtime[i] = TAtime[i] - BT[i]

# Display results
print("\nProcess\tAT\tBT\tPR\tCT\tTAT\tWT")
for i in range(num_pro):
    print(f"{processes[i]}\t{AT[i]}\t{BT[i]}\t{PR[i]}\t{comptime[i]}\t{TAtime[i]}\t{waitingtime[i]}")
