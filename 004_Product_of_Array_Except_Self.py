'''
Goal :  O(n) Time and O(1) Space

Input: arr[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: 

For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.
Input: arr[] = [12, 0]
Output: [0, 12]
Explanation: 

For i = 0, res[i] = 0.
For i = 1, res[i] = 12.
'''

arr = [10, 3, 5, 6, 2]

# for i in range(len(arr)):
#     mul=1
#     for j in range(len(arr)):
#         if j==i:
#             continue
#         mul = mul*arr[j]
#     res.append(mul)

# print(res)

pre = [1]*len(arr)
suf = [1]*len(arr)
res =[1]*len(arr)

for i in range(1,len(arr)):
    pre[i] = pre[i-1]*arr[i-1]
for i in range((len(arr)-2),-1,-1):
    suf[i] = suf[i+1]*arr[i+1]

for i in range(len(arr)):
    res[i] = pre[i]*suf[i]

print(pre,suf)
print(res)


    
    
