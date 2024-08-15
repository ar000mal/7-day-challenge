def is_palindrome(string):
    string = ''.join(char.lower() for char in string if char.isalnum())
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True
string=input("Enter the input: ")
result=is_palindrome(string)
print(f"{result}")

