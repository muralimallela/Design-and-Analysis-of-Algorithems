# Swapping
def swap(arr, i, j):
    print(f"\n{arr[i]} and {arr[j]} are swapped.")
    arr[i], arr[j] = arr[j], arr[i]
    

# Performing Partitioning   
def partition(arr, low, high):
    print("\n","."*70,"\n")
    print("Performing partition on list = ",*arr[low:high+1],f" with low = {low} and high = {high}")
    pivot = arr[low]
    left = low + 1 
    right = high
    done = False
    while not done:
        print(f"\nPivot = {pivot}")
        print(f"\nleft = {left} and right=  {right}")
        while left <= right and arr[left] <= pivot:
            print()
            print(f"{arr[left]} <= {pivot}   \n Increasing the left i.e., {left+1}")
            left = left + 1
        print(f"\nStopping the left at {left} because arr[left] is not <= pivot ")
        while arr[right] >= pivot and right >= left:
            print()
            print(f"{arr[right]} >= {pivot}   \n Decreasing the right i.e., {right-1}")
            right = right -1
        print(f"\nStopping the right at {right} because arr[right] not >= pivot")
            
        print(f"\nleft = {left} and right=  {right}")
        if right <= left:
            done= True
        else:
            print()
            print(f"left < right i.e., {left} <= {right}   \n Swapping arr[right] and arr[left] i.e., {arr[right]} and {arr[left]}")
            print("\nBefore swapping list : " , *arr[low:high+1])
            swap(arr, left, right)
            print("\nAfter swapping list : ", *arr[low:high+1])
    print()
    print(f"left >= right i.e., {left} >= {right}   \n Swapping  pivot and arr[right] i.e., {pivot} and {arr[right]}")
    print("\nBefore swapping list : " , *arr[low:high+1])
    swap(arr, low, right)
    print("\nAfter swapping list : ", *arr[low:high+1])
    print("\n","."*70)
    return right

# Performing Quick sort
def quick_sort(arr, low, high):
    if low < high:
        print("\n","*"*70,"\n")
        print("Performing quick sort on list = ",*arr[low:high+1],f" with low = {low} and high = {high}")
        print("\nFinding the pivot  of list = ",*arr[low:high+1],f" with low = {low},and high = {high}")
        pivot = partition(arr, low, high)
        print()
        print(f"The pivot is {arr[pivot]} at position {pivot} in the list ", *arr)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)
    

print("\n","-"*70,"\n")

# Taking the list from the user
size = int(input("Enter the size of the list: "))
my_list = []
for i in range(size):
    my_list.append(int(input(f"Enter the element at position {i}: ")))

print("\n","-"*70,"\n")   
print("Original List:", *my_list)

quick_sort(my_list, 0, len(my_list)-1)

print("\n","-"*70,"\n")

print("Finally, \nSorted List:", *my_list)

print("\n","*"*70,"\n\t\t\tMURALI KRISHNA MALLELA\n","*"*70)
