s = str(input())

def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")

f = palindrome(s)