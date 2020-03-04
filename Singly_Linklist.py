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

    def insert_begin(self,data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    def insert_end(self,data):
        NewNode = Node(data)
        if self.head:
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = NewNode
        else:
            self.head=NewNode

    def insert_at_index(self,index,data):
        NewNode = Node(data)
        temp = self.head
        count = 0
        while(temp):
            count = count+1
            temp = temp.next
        if(index>count+1 or index<0):
            print("Can not be inserted")

        if(index==0):
            NewNode.next = self.head
            self.head = NewNode
        else:
            temp = self.head
            temp2 = self.head
            for i in range(0,index-1):
                temp = temp.next
                temp2 = temp.next
            temp.next = NewNode
            NewNode.next=temp2

    def delete(self, data):
        temp = self.head
        prev = temp

        if temp:
            if temp.data == data:
                self.head = temp.next
                temp = None
        if temp==None:
            print("Linklist is empty")
        else:
            while(temp):
                if temp.data == data:
                    break
                prev=temp
                temp = temp.next

            prev.next = temp.next
            temp=None

    def dispay_list(self):
        temp = self.head
        while(temp):
            print(temp.data),
            temp = temp.next

if __name__ == "__main__":
    print("################### Implementation of Singly Linklist ########################")
    print("Operations ========>")
    linklist_class_obj = linklist()
    print("1 for creating linklist")
    print("2 for Inserting value at begin")
    print("3 for Inserting value at end")
    print("4 for Inserting value at given index")
    print("5 for deleting value")
    print("8 for displaying")
    print("9 for exit")
    while(True):
        print("Please enter operation's value")
        operation_val = input()
        if operation_val==1:
            size = input("Enter size of the linklist : ")
            for i in range(0,size):
                value = input("Enter value to be inserted : ")
                linklist_class_obj.create_list(value)

        elif operation_val == 2:
            value = input("Enter value to be inserted : ")
            linklist_class_obj.insert_begin(value)


        elif operation_val == 3:
            value = input("Enter value to be inserted : ")
            linklist_class_obj.insert_end(value)

        elif operation_val == 4:
            value = input("Enter value to be inserted: ")
            index = input("Enter index: ")
            linklist_class_obj.insert_at_index(index,value)
        elif operation_val == 5:
            value = input("Enter value to be deleted: ")
            linklist_class_obj.delete(value)

        elif operation_val == 8:
            linklist_class_obj.dispay_list()

        elif operation_val == 9:
            print("Exiting .......................")
            exit()
        else:
            print("Please enter valid operation's value")
            continue






