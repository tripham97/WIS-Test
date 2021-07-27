#Bai7: Tạo trò chơi “Cows and Bulls” với cách thức hoạt động như sau:
#1.	Tạo ngẫu nhiên một con số có 4 chữ số. Yêu cầu người chơi đoán con số đó.
#2.	Khi người chơi đoán đúng một chữ số nào đó ở đúng vị trí, họ sẽ có một “Cow”. Với mỗi chữ số sai, họ sẽ có một “Bull”.
#3.	Mỗi khi người dùng đưa ra phỏng đoán, hãy cho họ biết họ có bao nhiêu “Cows” và “Bulls”. Khi người dùng đoán đúng số, trò chơi kết thúc. Theo dõi số lần đoán mà người dùng thực hiện trong suốt trò chơi và họ biết khi kết thúc.
#Ví dụ: Giả sử, máy tính tạo ra một con số là 1038. Một tương tác sẽ diễn ra như sau:
#	Welcome to the Cows and Bulls Game!
# 	Enter a number:
#  	>>> 1234
#  	2 cows, 0 bulls
#  	>>> 1256
#  	1 cow, 1 bull
#  	...
import random
import time

def CowBull():
  n = random.randint(999,10000)
  n_1 = 0
  print(n)
  print("Welcome to the Cows and Bulls Game!")
  while int(n_1) != n:
    n_2 = 0
    n_1 = int(input("Enter a number: "))
    for i in range(0,4):
      if str(n_1)[i] == str(n)[i]:
        n_2 += 1
    print(str(n_2)+'Cows, '+str(int(4-n_2))+' Bulls')
CowBull()
