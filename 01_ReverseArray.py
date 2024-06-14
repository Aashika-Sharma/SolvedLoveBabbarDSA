def reverse_array(arr):
  reversed_array = arr[::-1]

  print("Original Array: ", end = ' ')
  for i in arr:
    print(i, end = " ")

  print("\nReversed Array: " , end = ' ')
  for i in reversed_array:
    print(i, end = " ")

numbers = [1, 2, 3, 4, 5]
reverse_array(numbers)
