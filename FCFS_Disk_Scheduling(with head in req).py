def fcfs_ds(reqs, head):
  total_seek_opt = 0
  sequence = [head] #to store movment seq #ds= disk scheduling

  for req in reqs:

    mov = abs(req - head)
    total_seek_opt += mov
    head = req
    sequence.append(head)
  return total_seek_opt, sequence


#user input

if __name__ == "__main__":

  n = int(input("Enter the number of requests sequence: "))
  reqs=[]
  print("Enter the disk requests: ")

  for i in range(n):
    req = int(input(f"Request{i+1}:"))
    reqs.append(req)

  head = int(input("Enter head value : "))


             #Fcfs

  total_mov , seq = fcfs_ds(reqs,head)


  
  print("Total Seek Operations: ",total_mov)
