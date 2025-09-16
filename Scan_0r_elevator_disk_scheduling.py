requests = list(map(int, input("Enter the disk requests: ").split()))
requests.sort()
print("Sorted requests:", requests)


head = int(input("Head value:"))


direction = input("Head movement direction : ")
while direction not in ["left", "right"]:
    direction = input("Invalid input! Enter 'left' or 'right': ")

total_mov = 0
sequence = []

while requests:
    if direction == "left":
        
        candidates = [r for r in requests if r <= head]
        if candidates:
            closest = max(candidates)  
        else:
            
            closest = min(requests)
    else:  
        candidates = [r for r in requests if r >= head]
        if candidates:
            closest = min(candidates)  
        else:
          
            closest = max(requests)

    total_mov += abs(head - closest)
    head = closest
    sequence.append(head)
    requests.remove(closest)

print("Seek Sequence:", sequence)
print("Total head movement:", total_mov)

