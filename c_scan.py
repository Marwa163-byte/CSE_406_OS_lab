def disk_scheduling(arr, head, direction):
    seek_time = 0
    try:
        idx = arr.index(head)
    except ValueError:
        print(f"Head position {head} not found in requests array!")
        return -1
    
    if direction == "left":
        for i in range(idx-1, -1, -1):
            seek_time += abs(head - arr[i])
            head = arr[i]
        
        for i in range(len(arr)-1, idx, -1):
            seek_time += abs(head - arr[i])
            head = arr[i]
    
    elif direction == "right":
        for i in range(idx+1, len(arr)):
            seek_time += abs(head - arr[i])
            head = arr[i]
        
        for i in range(0, idx):
            seek_time += abs(head - arr[i])
            head = arr[i]
  
    else:
        print("Invalid direction! Use 'left' or 'right'")
        return -1
    
    return seek_time


# Take user inputs
requests = list(map(int, input("Enter the disk requests : ").split()))
requests.sort()  


initial_head = int(input("Enter the initial head position: "))

direction = input("Enter head movement direction (left/right): ")
while direction not in ["left", "right"]:
    direction = input("Invalid input! Enter 'left' or 'right': ")
result = disk_scheduling(requests, initial_head, direction)
if result != -1:
    print(f"Total seek time: {result}")
