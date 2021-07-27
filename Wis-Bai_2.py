# Bai_2 Viết chương trình hỏi người dùng cần tạo bao nhiêu số trong dãy Fibonacci và tạo chúng. 
#Chuỗi Fibonacci là một dãy số trong đó số tiếp theo trong dãy là tổng của hai số trước đó. Ví dụ của một chuỗi Fibonacci như sau: 1, 1, 2, 3, 5, 8, 13,…
n = int(input("# of element: "))
if n<3:
    print("It's not enough element to create Fibonacci string")
elif n>=3:
    n_1 = int(input("Enter 1st number: "))
    n_2 = int(input("Enter 2nd number: "))
    fib = [n_1, n_2]
    for i in range (2,n):
        print(i)
        fib.append(fib[i-1]+fib[i-2])
    print(fib)
else:
    print("We cannot create the Fibonacci string ")
