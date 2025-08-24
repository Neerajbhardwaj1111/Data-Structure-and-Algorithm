'''
Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
Output: 8
Explanation: Buy for price 1 and sell for price 9. 

Input: prices[] = {7, 6, 4, 3, 1} 
Output: 0
Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

Input: prices[] = {1, 3, 6, 9, 11} 
Output: 10
Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1]
'''

# price = [1, 3, 6, 9, 11]


# def max_profit(price):
#     profit =0
#     for i in range(len(price)):
#         for j in range(i+1,len(price)):
#             if(price[j]-price[i])>profit:
#                 profit= price[j]-price[i]
            
#     return profit

# profit=max_profit(price)
# print(f"{profit}")

arr = [7, 10, 1, 3, 6, 9, 2]
min_so =arr[0]
max_p =0

for i in range(1,len(arr)):
    min_so = min(min_so,arr[i])
    max_p = max(max_p,arr[i]-min_so)

print(max_p)

    
