#Bai_6: Nhập một số, in ra giai thừa của số đó.
# Lưu ý: Không sử dụng for trong bài tập này.
n = int(input("Enter the number: "))
def factor(n):
    if n == 0:
        return 1
    return n*factor(n-1)
print(n,"! = ",factor(n))
