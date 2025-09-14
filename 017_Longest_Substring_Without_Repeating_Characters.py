'''
Longest Substring Without Repeating Characters

Given a string s having lowercase characters, find the length of the longest substring without repeating characters. 

Examples:

Input: s = "geeksforgeeks"
Output: 7 
Explanation: The longest substrings without repeating characters are "eksforg” and "ksforge", with lengths of 7.

Input: s = "aaa"
Output: 1
Explanation: The longest substring without repeating characters is "a"

Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring without repeating characters is "abcdef".
'''
#Algorithm
# take a max = 0
# temp = ""
# append to temp untill next ele in temp 
# update max 
# print(max)

#input
s = "abcdefabcbb"

max_length = 0
temp =""
for ele in s:
    if ele in temp:
        max_length = max(max_length,len(temp))
        temp=""
    else:
        temp = temp+ele

print(max_length)



