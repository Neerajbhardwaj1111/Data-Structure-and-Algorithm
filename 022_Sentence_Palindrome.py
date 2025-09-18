'''
Sentence Palindrome

Given a sentence s, determine whether it is a palindrome sentence or not. A palindrome sentence is a sequence of characters that reads the same forward and backward after:

Converting all uppercase letters to lowercase.
Removing all non-alphanumeric characters (i.e., ignore spaces, punctuation, and symbols).

Examples: 

Input: s = "Too hot to hoot."
Output: true
Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become "toohottohoot" which is a palindrome.

Input: s = "Abc 012..##  10cbA"
Output: true
Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become "abc01210cba" which is a palindrome.

Input: s = "ABC $. def01ASDF.."
Output: false
Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become "abcdef01asdf" which is not a palindrome.
'''
string = "ABC $. def01ASDF.."
processed_string = "".join(ch.lower() for ch in string if ch.isalpha())
print("true" if processed_string[::-1] == processed_string else "false" )
