def min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
    return min_val, max_val

def display(arr):
  for i in arr:
    print(i, end=" ")
  
numbers = [3,5,34,2,4,6,43,456,45]

display(numbers)
min_num, max_num = min_max(numbers)
print("\nMinimum number:", min_num)
print("Maximum number:", max_num)
