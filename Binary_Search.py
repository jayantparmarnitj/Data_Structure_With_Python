############# Functions ############
def binary_search(arr,val,first, last):
    if last>=first:
        mid = (first+last)/2
        if(arr[mid]==val):
            return True,mid

        if(arr[mid]>val):
            binary_search(arr, val, first, mid-1)
        else:
            binary_search(arr, val, mid+1, last)
    else:
        return False,""
if __name__ == "__main__":
    print("################### Implementation of Binary Search ########################")
    size = input("Enter size of aray :")
    list = []
    for i in range(0,size):
        list.append(input())
    val = input("Enter value to be searched :")
    mid = size/2
    flag,index = binary_search(list,val,0,size-1)
    if flag:
        print("Value present in the array at index :",index)
    else:
        print("Not Found!")








