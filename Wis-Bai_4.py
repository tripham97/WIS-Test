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
