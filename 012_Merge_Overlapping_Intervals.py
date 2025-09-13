'''
Given an array of time intervals where arr[i] = [starti, endi], our task is to merge all the overlapping intervals into one and output the result which should have only mutually exclusive intervals.

Examples:

Input: arr[] = [[1, 3], [2, 4], [6, 8], [9, 10]]
Output: [[1, 4], [6, 8], [9, 10]]
Explanation: In the given intervals, we have only two overlapping intervals [1, 3] and [2, 4]. Therefore, we will merge these two and return [[1, 4]], [6, 8], [9, 10]].

Input: arr[] = [[7, 8], [1, 5], [2, 4], [4, 6]]
Output: [[1, 6], [7, 8]]
Explanation: We will merge the overlapping intervals [[1, 5], [2, 4], [4, 6]] into a single interval [1, 6].
'''

'''
Algo
make two arrays 
sort them 
traverse in both 
until find gap in start and end

'''
arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
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
res = []

while i < n:
    temp_start = start[i]

    # move i until no overlap
    while i < n - 1 and start[i+1] <= end[i]:
        i += 1

    temp_end = end[i]
    res.append([temp_start, temp_end])
    i += 1

print(res)
