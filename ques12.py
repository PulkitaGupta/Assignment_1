num = int(input("Enter a number: "))
sum = 0
while num > 0:
    n = int(num) % 10
    sum += n
    num = int(num/10)

print(sum)

