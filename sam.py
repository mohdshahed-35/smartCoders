class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Deleted:", self.top.data)
            self.top = self.top.next

    def display(self):
        temp = self.top
        if temp is None:
            print("Stack is empty")
        else:
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

s = Stack()

while True:
    print("1.Push 2.Pop 3.Display 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        data = int(input("Enter element: "))
        s.push(data)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")