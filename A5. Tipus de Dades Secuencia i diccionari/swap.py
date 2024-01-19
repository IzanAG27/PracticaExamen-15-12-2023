num = input("").split()
primerNum = num[0]
ultimoNum = num[-1]
num[0] = ultimoNum
num[-1] = primerNum
print(num)