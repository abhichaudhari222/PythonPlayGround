# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
 start = 0
 end = len(arr) - 1
 mid = 0

 while start <= end:

  mid = (end + start) // 2

  # If x is greater, ignore left half
  if arr[mid] < x:
   start = mid + 1

  # If x is smaller, ignore right half
  elif arr[mid] > x:
   end = mid - 1

  # means x is present at mid
  else:
   return mid

 # If we reach here, then the element was not present
 return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
 print("Element is present at index", str(result))
else:
 print("Element is not present in array")
