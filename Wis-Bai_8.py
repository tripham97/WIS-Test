#Bai8: Viết một chương trình để chuyển đổi số nguyên N sang hệ cơ số B (2 <= B <= 32) bất kỳ.

n = int(input("Enter your interger: "))


def change(n):
  print("2: " + bin(n)[2:])
  print("32: " + hex(n))
  print("10 " + oct(n))


change(n)