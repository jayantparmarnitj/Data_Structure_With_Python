############# Functions ############
class Node:
    def __init__(self,data):
        self.data = data
        self.next = Node

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    def dispay_stack(self):
        temp = self.head
        while(temp):
            print(temp.data),
            temp = temp.next

    def pop(self):
        temp = self.head
        if temp:
            self.head = temp.next
            temp=None
        else:
            print("Stack is empty")

    def isEmpty(self):
        if self.head:
            print("Stack is not empty")
        else:
            print("Stack is empty")

    def top(self):
        if self.head:
            print("Stack is not empty and top of the Stack is :", self.head.data)
        else:
            print("Stack is empty")

if __name__ == "__main__":
    print("################### Implementation of Stack using Link list ########################")
    print("<======== Operations ========>")
    stack_class_obj = Stack()
    print("1 for Push")
    print("2 for Pop")
    print("3 for Top")
    print("4 for isEmpty")
    print("5 for Displaying")
    print("6 for exit")

    while(True):
        operation_val = input("Please enter operation's value : ")
        if operation_val=="1":
            value = input("Enter value to be pushed : ")
            stack_class_obj.push(value)

        elif operation_val == "2":
            stack_class_obj.pop()


        elif operation_val == '3':
            stack_class_obj.top()

        elif operation_val == '4':
            stack_class_obj.isEmpty()

        elif operation_val == '5':
            stack_class_obj.dispay_stack()
            print()

        elif operation_val == '6':
            print("Exiting .......................")
            exit()
        else:
            print("Please enter valid operation's value")
            continue





