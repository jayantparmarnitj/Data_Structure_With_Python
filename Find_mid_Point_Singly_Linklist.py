############# Functions ############
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = None

    def create_list(self,data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    def find_mid(self):
        temp = self.head
        prev = temp
        while(temp and temp.next):
            prev = prev.next
            temp = temp.next.next
        print("Middle point of the Linklist is : ",prev.data)

    def dispay_list(self):
        temp = self.head
        while(temp):
            print(temp.data),
            temp = temp.next

if __name__ == "__main__":
    print("################### Find Mid Point in Singly Linklist ########################")
    print("Operations ========>")
    linklist_class_obj = linklist()
    print("1 for creating linklist")
    print("2 for Find Mid Point")
    print("3 for Displaying")
    print("4 for exit")
    while(True):
        operation_val = int(input("Please enter operation's value : "))
        if operation_val==1:
            size = int(input("Enter size of the linklist : "))
            for i in range(0,size):
                value = input("Enter value to be inserted : ")
                linklist_class_obj.create_list(value)

        elif operation_val == 2:
            linklist_class_obj.find_mid()

        elif operation_val == 3:
            linklist_class_obj.dispay_list()

        elif operation_val == 4:
            print("Exiting .......................")
            exit()
        else:
            print("Please enter valid operation's value")
            continue






