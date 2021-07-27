# Bai_3: Yêu cầu người dùng nhập một số và xác định xem đó có phải là số nguyên tố hay không.
n = int(input("Enter your prime number: "))
if n>1:
    for i in range(2, n):
        if (n % i) == 0:
            print("This is Composite Number")
        break
    else:
        print("This is Prime Number")
else:
    print("This is extra")
