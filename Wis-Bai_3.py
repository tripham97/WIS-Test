# Bai_3
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
