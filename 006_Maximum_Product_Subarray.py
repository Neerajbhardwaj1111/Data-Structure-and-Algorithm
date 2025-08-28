'''
Given an array arr[] consisting of positive, negative, and zero values, find the maximum product that can be obtained from any contiguous subarray of arr[].

Examples:

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.

Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.

Input: arr[] = [2, 3, 4] 
Output: 24 
Explanation: For an array with all positive elements, the result is product of all elements.
'''
import os
os.system("cls")
arr = [-2, 6, -3, -10, 0, 2]

n = len(arr)

currMax = arr[0]
currMin = arr[0]
maxProd = arr[0]
for i in range(1, n):
    temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)
    currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)
    currMax = temp
    maxProd = max(maxProd, currMax)
    print(temp,currMin, currMax,maxProd)

print(maxProd)


# max_mul =arr[0]

# for i in range(len(arr)):
#     cur_mul = arr[i]
#     for j in range(i+1,len(arr)):
#         cur_mul =cur_mul*arr[j]
#         max_mul=max(max_mul,cur_mul)

# print(max_mul)
