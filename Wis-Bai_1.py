# Bai_1: Yêu cầu người dùng cung cấp một chuỗi và cho biết đó có phải một palindrome không (palindrome là một chuỗi có thể được viết xuôi hay viết ngược vẫn chỉ cho ra chính nó).
string = input("Input your string: ")
if string == string[::-1]:
    print("This is palindrome string")
else:
    print("This is not palindrome string")
