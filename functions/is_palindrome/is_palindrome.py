def is_palindrome(s):
    reversed_s = ""

    for character in s:
        reversed_s = character + reversed_s

    return s == reversed_s
print  (is_palindrome("level"))

