fibonacci = [0, 1]
N = int(input("Please entering the count of Fibonacci numbers: "))
for i in range(1, N-1):
	fibonacci.append(fibonacci[i - 1] + fibonacci[i])

print(fibonacci)
input()