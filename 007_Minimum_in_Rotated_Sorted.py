'''
Given a sorted array of distinct elements arr[] of size n that is rotated at some unknown point, the task is to find the minimum element in it.

Input: arr[] = [5, 6, 1, 2, 3, 4]
Output: 1
Explanation: 1 is the minimum element present in the array.

Input: arr[] = [3, 1, 2]
Output: 1
Explanation: 1 is the minimum element present in the array.

Input: arr[] = [4, 2, 3]
Output: 2
Explanation: 2 is the only minimum element in the array.
'''

arr = [5, 6, 1, 2, 3, 4]

#use binary search
lo = 0
hi =len(arr)-1
while lo < hi:
    if arr[lo]<arr[hi]:
        print(arr[lo])
    mid = (lo+hi)//2

    if(arr[mid]>arr[hi]):
        lo =mid+1
    else:
        hi = mid

print(arr[lo])
