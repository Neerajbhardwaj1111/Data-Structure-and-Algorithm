'''
Given an integer array arr[], find the subarray (containing at least one element) which has the maximum possible sum, and return that sum.
Note: A subarray is a continuous part of an array.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray [-2] has the largest sum -2.

Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.
'''

arr =[2, 3, -8, 7, -1, 2, 3]

currsum = 0
max_sum = arr[0]

for i in range(len(arr)):
    currsum = max(currsum+arr[i],arr[i])
    max_sum = max(currsum,max_sum)

print(max_sum)

# max_sum = sum(arr)

# for i in range(len(arr)):
#     currsum = 0
#     for j in range(i,len(arr)):
#         currsum = currsum+arr[j]

#         max_sum = max(max_sum,currsum)

# print(max_sum)

