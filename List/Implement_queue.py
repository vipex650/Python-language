queue = []

def enqueue(item):
    queue.append(item)
    print(f"Enqueued {item} to queue")

def dequeue():
    if not queue:
        print("Queue is empty, cannot dequeue")
    else:
        removed_item = queue.pop(0)
        print(f"Dequeued {removed_item} from queue")

def display():
    if not queue:
        print("Queue is empty")
    else:
        print("Queue elements:", queue)

enqueue(10)  
enqueue(20)     
enqueue(30)
display() 
dequeue()    
display()  