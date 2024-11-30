def reverse_string(str):
    str1 = str[-1: :-1]
    return str1
string = str(input("Enter string: "))
print(reverse_string(string))