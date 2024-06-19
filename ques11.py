def fibonacci(num):
    sequence = [0,1]
    for i in range(2,num):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence


n = int(input("Enter a number: "))
print(fibonacci(n))

