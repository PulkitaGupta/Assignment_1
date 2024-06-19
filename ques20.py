list1 = list(map(int, input("Enter a list of numbers separated by comma: ").split(',')))
sum = 0
for i in list1:
    sum += i
print("The sum of the elements of list is: ", sum)
