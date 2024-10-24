stack = []

def push(item):
    stack.append(item)
    print(f"Pushed {item} to stack")

def pop():
    if not stack:
        print("Stack is empty, cannot pop")
    else:
        removed_item = stack.pop()  # Removes and returns the last item
        print(f"Popped {removed_item} from stack")

def display():
    if not stack:
        print("Stack is empty")
    else:
        print("Stack elements:", stack)

push(10)
push(20)
push(30)
display()
pop()     
display()