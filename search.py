def findGap (arr, l, r):
    mid = l + (r - l) // 2

    # basecase
    if arr[l] < arr[mid] and arr[mid] < arr[r]:
        print(f"Sorted!!! {arr[l:r+1]}")
        return 0
    
    if arr[mid] < arr[mid-1] and arr[mid] < arr[mid+1]:
        print(f"{arr[:mid]} >>>{[arr[mid]]}<<< {arr[mid+1:]}")
        return mid

    if mid == 0 or mid == len(arr)-2:
        print(f"{arr[:mid+1]} >>>{arr[mid+1:]}<<<")
        return mid+1
    
    # recursion
    if arr[mid] < arr[l]:
        print(f">>>{arr[:mid+1]}<<< {arr[mid+1:]}")
        return findGap(arr, l, mid)

    elif arr[mid] > arr[r]:
        print(f"{arr[:mid+1]} >>>{arr[mid+1:]}<<<")
        return findGap(arr, mid, r)


def binarySearch (arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
  
        if arr[mid] == x:
            return mid
          
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)  
        else:
            return binarySearch(arr, mid + 1, r, x)
  
    else:
        # Element is not present in the array
        return -1
    

arr = [1, 3, 4, 5, 0]
x = 9

print("\n@@@ Finding Gap...")
result = findGap(arr, 0, len(arr)-1)
print(f"Index: {result}\n")

newArr = arr[result:] + arr[:result]
print("@@@ Sorted Array...")
print(newArr)
print("")

answer = binarySearch(newArr, 0, len(newArr)-1, x)
print("@@@ Original Array...")
print(f"{arr} >>>{x}<<<" )

if answer == -1:
    print(answer)
    exit()

answer += result
print(answer%(len(arr)))