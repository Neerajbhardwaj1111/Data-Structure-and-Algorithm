'''
Container With Most Water
Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the vertical lines, find the maximum amount of water that can be contained between any two lines, together with the x-axis.

Examples :  

Input: arr[] = [1, 5, 4, 3]
Output: 6
Explanation: 5 and 3 are 2 distance apart. So the size of the base = 2. Height of container = min(5, 3) = 3. So total area = 3 * 2 = 6.

Input: arr[] = [3, 1, 2, 4, 5]
Output: 12
Explanation: 5 and 3 are 4 distance apart. So the size of the base = 4. Height of container = min(5, 3) = 3. So total area = 4 * 3 = 12.

Input: arr[] = [2, 1, 8, 6, 4, 6, 5, 5]
Output: 25
Explanation: 8 and 5 are 5 distance apart. So the size of the base = 5. Height of container = min(8, 5) = 5. So, total area = 5 * 5 = 25.
'''
#input
arr = [3, 1, 2, 4, 5]

#global Variable for storing maximum water hold till now
max_water_hold =0
'''
for each elemnet:
  chck for the min and and multiply by distant
  check with the max if greter update
'''
step =0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        distant = j-i
        min_ele = min(arr[i],arr[j])
        current_water_hold = distant*min_ele
        max_water_hold = max(max_water_hold,current_water_hold)
        step+=1




'''
Two Pointer Approach
put two pointer one at each end
and make them closer from the smaller hight end
and keep track of max water hold and current water hold
and reduce distant each time 
'''
step1=0
left = 0
right = len(arr)-1
while left<right:
    distant = right-left
    min_ele = min(arr[left],arr[right])
    current_water_hold = distant*min_ele
    max_water_hold = max(max_water_hold,current_water_hold)
    step1+=1
    if arr[left]<=arr[right]:
        left+=1
    else:
        right-=1

#Output
print(f"Steps by Naive / Brute Force : {step}\nSteps by Two Pointer : {step1}")
print(f"Result : {max_water_hold}")
