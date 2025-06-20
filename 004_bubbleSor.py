def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
list1= [98,37,86,45,12,101,115]
bubble_sort(list1)
print("Sorted list is:", list1)