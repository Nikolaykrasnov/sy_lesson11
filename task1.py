def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

n = int(input("Введите число: "))
start = factorial(n)
facts = []
for i in range(start, 0, -1):
    facts.append(factorial(i))
print(facts)
