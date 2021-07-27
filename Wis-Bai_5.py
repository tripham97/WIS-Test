#Bai_5: Định nghĩa hàm có thể chấp nhận input là số nguyên và in "Đây là một số chẵn" nếu nó chẵn
# và in "Đây là một số lẻ" nếu là số lẻ.

def value(n):
    if n%2 == 0:
        print(n, "Đây là một số chẵn")
    else:
        print(n, "Đây là một số lẻ" )
value(int(input("#:")))