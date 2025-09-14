'''
Maximum consecutive repeating character in string

Given a string s, the task is to find the maximum consecutive repeating character in the string.

Note: We do not need to consider the overall count, but the count of repeating that appears in one place.

Examples: 

Input: s = "geeekk"
Output: e
Explanation: character e comes 3 times consecutively which is maximum.

Input: s = "aaaabbcbbb"
Output: a
Explanation: character a comes 4 times consecutively which is maximum.
'''
'''
Start with the first character.

Keep a counter of how many times the current character repeats.

If the next character is the same → increment counter.

If the next character is different:

Compare with maximum so far.

Update max if needed.

Reset counter for new character.

After the loop, check one last time (in case the max sequence is at the end).

Return the character with maximum streak.
'''
s = "geeekk"

max_char = s[0]
max_count = 1
curr_char = s[0]
curr_count = 1

for i in range(1,len(s)):
    if s[i] == curr_char:
        curr_count+=1
    else:
        if curr_count>max_count:
            max_count = curr_count
            max_char =curr_char
        curr_char = s[i]
        curr_count = 1
if curr_count>max_count:
    max_count = curr_count
    max_char = curr_char

print(max_char)



