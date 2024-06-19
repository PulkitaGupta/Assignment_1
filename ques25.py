with open("ques25_1.txt",'r') as file1:
    content = file1.read()

with open("ques25_2.txt",'w') as file2:
    print(content, file=file2)

