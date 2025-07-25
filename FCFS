# Completion Time
# Turn Around Time
# Waiting Time
# Average TAT and Waiting Time

# Initializing

processes = []
arrival = []
burst = []
completion = []
turnAround = []
waiting = []

def getProcesses():

    num = int(input('Number of Processes: '))

    for i in range(num):

        processID = input(f'Process ID {i+1}: ')
        arrivalTime = int(input(f'Arrival Time {i+1}: '))
        burstTime = int(input(f'Burst Time {i+1}: '))

        processes.append(processID)
        arrival.append(arrivalTime)
        burst.append(burstTime)

def completionTime():

    new = burst[0]
    completion.append(new)

    for i in range(len(burst)-1):
        new = new + burst[i+1]
        completion.append(new)

def tat():

    for i in range(len(processes)):
        turnAround.append(completion[i] - arrival[i])

def waitingTime():

    for i in range(len(processes)):
        waiting.append(turnAround[i] - burst[i])

def average():

   
    avgWT = sum(waiting) / len(waiting)

    print('Average Waiting -', avgWT)
   

def display():

    completionTime()
    tat()
    waitingTime()

    print('Process | Arrival | Burst | Completion | TAT | Waiting')
    for i in range(len(processes)):
        print(f'   {processes[i]}   |    {arrival[i]}    |   {burst[i]}   |    {completion[i]}   |  {turnAround[i]}  |  {waiting[i]}  ')

    average()

getProcesses()
display()
