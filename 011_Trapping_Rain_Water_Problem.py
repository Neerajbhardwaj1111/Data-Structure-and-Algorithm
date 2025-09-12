'''
Given an array arr[] of size n consisting of non-negative integers, where each element represents the height of a bar in an elevation map and the width of each bar is 1, determine the total amount of water that can be trapped between the bars after it rains.

Input: arr[] = [3, 0, 1, 0, 4, 0, 2]
Output: 10
Explanation: The expected rainwater to be trapped is shown in the above image.

Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: We trap 0 + 3 + 1 + 3 + 0 = 7 units.

Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides
'''

'''
Algo
water trapped = min(max_left[i],max_right[i])-height[i]

'''

arr = [1, 2, 3, 4]
max_left =[0] * len(arr)
max_right= [0] * len(arr)
water_trapped = 0

max_left[0]= arr[0]
for i in range(1,len(arr)):
    max_left[i] = max(max_left[i-1],arr[i])
    

curr_max_right = arr[len(arr)-1]
for i in range(len(arr)-1,-1,-1):
    curr_max_right = max(curr_max_right,arr[i])
    max_right[i] = curr_max_right

for i in range(len(arr)):
    water_trapped += min(max_left[i],max_right[i])-arr[i]

print(water_trapped)
