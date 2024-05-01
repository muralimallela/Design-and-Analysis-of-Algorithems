import streamlit as st
# Write custom CSS
custom_css = """
<style>
/* Decrease padding for mobile view */
@media (max-width: 680px) {
    #quick-sort{
        padding: 0px;
    }
}
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Swapping
def swap(arr, i, j):
    st.write(f"\n{arr[i]} and {arr[j]} are swapped.")
    arr[i], arr[j] = arr[j], arr[i]

# Performing Partitioning   
def partition(arr, low, high):
    st.write("\n","."*70,"\n")
    st.write("Performing partition on list")
    st.write(*arr[low:high+1],f"\n\nwith low = {low} and high = {high}")
    pivot = arr[low]
    left = low + 1 
    right = high
    done = False
    while not done:
        st.write("\n","~"*30,f"\nPivot = {pivot}"f"\n\nleft = {left} and right=  {right}")
        #st.write("\n","~"*30,f"\nleft = {left} and right=  {right}")
        while left <= right and arr[left] <= pivot:
            st.write()
            st.write(f"{arr[left]} <= {pivot}   \n Increasing the left i.e., {left+1}")
            left = left + 1
        st.write(f"\nStopping the left at {left} because arr[left] is not <= pivot ")
        while arr[right] >= pivot and right >= left:
            st.write()
            st.write(f"{arr[right]} >= {pivot}   \n Decreasing the right i.e., {right-1}")
            right = right -1
        st.write(f"\nStopping the right at {right} because arr[right] not >= pivot")
        st.write(f"\nleft = {left} and right=  {right}")
        if right <= left:
            done= True
        else:
            st.write()
            st.write(f"left < right i.e., {left} <= {right}   \n Swapping arr[right] and arr[left] i.e., {arr[right]} and {arr[left]}")
            st.write("\nBefore swapping list : \n\n" , *arr[low:high+1])
            swap(arr, left, right)
            st.write("After swapping list :")
            st.write(*arr[low:high+1])
    st.write()
    st.write(f"left >= right i.e., {left} >= {right}   \n Swapping  pivot and arr[right] i.e., {pivot} and {arr[right]}")
    st.write("\nBefore swapping list : \n\n" , *arr[low:high+1])
    swap(arr, low, right)
    st.write("\nAfter swapping list : ")
    st.write(*arr[low:high+1])
    st.write("\n","."*70)
    return right

# Performing Quick sort
def quick_sort(arr, low, high):
    if low < high:
        st.write("-"*70,"\n")
        st.write("""
                 ##### Performing quick sort on list  
                 """)
        st.write(*arr[low:high+1])
        st.write(f" \n \nwith low = {low} and high = {high}")
        st.write("\nFinding the pivot  of list \n\n",*arr[low:high+1],f"\n\n with low = {low} , and high = {high}")
        pivot = partition(arr, low, high)
        st.write()
        st.write(f"The pivot is {arr[pivot]} at position {pivot} in the list \n\n", *arr)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)

if __name__ == "__main__":
    st.title("Quick Sort")
    st.write("")
    # Taking the list from the user
    size = st.number_input("Enter the size of the list: ", step=1,value = 0)
    my_list = []
    for i in range(size):
        my_list.append(st.number_input(f"Enter the element at position {i}: ",value = 0))

    st.write("\n","-"*70,"\n")   
    st.write("Original List:\n","\n",*my_list)

    quick_sort(my_list, 0, len(my_list)-1)

    st.write("\n","-"*70,"\n")
    st.write("Finally,"," \nSorted List:")
    st.write(*my_list)
    st.write("\n","*"*70,"\n\t\t\t","\n"*20,"\n\t\t\t"," MURALI KRISHNA MALLELA\n","*"*70)
 
