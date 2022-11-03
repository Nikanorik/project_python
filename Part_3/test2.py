def first_non_consecutive(arr):
    for i in range(len(arr)):
        if i + 1< len(arr) and i+2 < len(arr):
            if arr[i + 1] - arr[i] == arr[i+2] - arr[i+1]:
                None
            else:
                print(arr[i+2])
                return arr[i + 2]



first_non_consecutive([1,2,3,4,6,7,8])

