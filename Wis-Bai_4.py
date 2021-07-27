#Bai_4: Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. 
#Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.
#Ví dụ: đầu vào là: 0100,0011,1010,1001
#	Đầu ra sẽ là: 1010	

n_str = []
n_bin = []
n = 100
for i in range (0,100):
    n = int(input("#:"))
    n_str.append(n)
    print(n_str)
    if n%5 == 0:
        n_bin.append(n)
        print((n_bin),"This divided by 5")
    else:
        print(n,"This cannot divided by 5")
    print((n_bin), "This divided by 5")
else:
    print(n_str)
