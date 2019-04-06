primeNums = []
alpha = []
for num in range(3, 104):
    if all(num % i != 0 for i in range(2, num)):
        primeNums.append(num)
for i in range(26):
    alpha.append(chr(65 + i))



cryptoMessage = input()
print(cryptoMessage)
for i in range(len(cryptoMessage)):
    if cryptoMessage[i] == primeNums[i]:
        print(alpha[i])