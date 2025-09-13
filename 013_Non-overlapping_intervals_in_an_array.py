'''
Non-overlapping intervals in an array
Given a 2d array arr[][] of time intervals, where each interval is of the form [start, end]. The task is to determine all intervals from the given array that do not overlap with any other interval in the set. If no such interval exists, return an empty list.

Examples: 

Input: arr[] = [[1, 3], [2, 4], [3, 5], [7, 9]] 
Output: [[5, 7]] 
Explanation: The only interval which doesn’t overlaps with the other intervals is [5, 7].

Input: arr[][] = [[1, 3], [2, 6], [8, 10], [15, 18]] 
Output: [[6, 8], [10, 15]]
Explanation: There are two intervals which don’t overlap with other intervals are [6, 8], [10, 15].

Input: arr[][] = [[1, 3], [9, 12], [2, 4], [6, 8]] 
Output: [[4, 6], [8, 9]] 
Explanation: There are two intervals which don’t overlap with other intervals are [4, 6], [8, 9].
'''
'''
Algorithm:
merge intervals by previous code
find gaps 
'''
arr = [[1, 3], [9, 12], [2, 4], [6, 8]]   
start = []
end = []

for ele in arr:
    start.append(ele[0])
    end.append(ele[1]) 

start.sort()
end.sort()

n = len(arr)
i = 0
j = 0
mid_res = []
res = []

while i < n:
    temp_start = start[i]

    # move i until no overlap
    while i < n - 1 and start[i+1] <= end[i]:
        i += 1

    temp_end = end[i]
    mid_res.append([temp_start, temp_end])
    i += 1

#mid_res=[[1, 5], [7, 9]]

for i in range(len(mid_res)-1):
    res.append([mid_res[i][1],mid_res[i+1][0]])

print(res)
    
