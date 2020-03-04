############# Functions ############
class Stack:
    def push(self,my_stack,value):
        my_stack.insert(0,value)
        return my_stack

    def pop(self,my_stack):
        Stack_class_obj = Stack()
        poped_val = "0"
        if not Stack_class_obj.isEmpty(my_stack):
            poped_val = my_stack[0]
            my_stack.pop(0)
        return poped_val,my_stack

    def isEmpty(self,my_stack):
        if(len(my_stack)==0):
            return True
        else:
            return False

    def top(self,my_stack):
        Stack_class_obj = Stack()
        if not Stack_class_obj.isEmpty(my_stack):
            isEmptyFlag = True
            return isEmptyFlag,my_stack[0]
        else:
            isEmptyFlag=False
            return isEmptyFlag,""

if __name__ == "__main__":
    print("################### Implementation of Stack using Array ########################")
    print("Operations ========>")
    my_stack = []
    stack_class_obj = Stack()
    print("1 for Push")
    print("2 for Pop")
    print("3 for Top")
    print("4 for isEmpty")
    print("5 for Exit")
    while(True):
        print("Please enter operation's value")
        operation_val = input()
        if operation_val==1:
            value = input("Enter value to be pushed : ")
            stack_class_obj.push(my_stack,value)

        elif operation_val == 2:
            poped_val,my_stack = stack_class_obj.pop(my_stack)
            if poped_val=="0":
                print("Stack is Empty")
            else:
                print("Poped value is : ",poped_val)

        elif operation_val == 3:
            isEmptyFlag , top_val = stack_class_obj.top(my_stack)
            if isEmptyFlag==True:
                print("Top value of the stack is :", top_val)
            else:
                print("Stack is Empty !")

        elif operation_val == 4:
            if stack_class_obj.isEmpty(my_stack):
                print("Stack is Empty !")
            else:
                print("Stack is not Empty and size of stack is : ", len(my_stack))

        elif operation_val == 5:
            print("Exiting .......................")
            exit()
        else:
            print("Please enter valid operation's value")
            continue

        print("Stack is :", my_stack)




