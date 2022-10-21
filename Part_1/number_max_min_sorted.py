def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0
    else:
        summer = sum(sorted(arr)[1:-1])
        print(summer)
        return summer

sum_array([3,45,4666,33,2323,2452,42])