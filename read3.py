file1=open('text.txt', 'r')
file2=open('codingal.txt', 'w')


for line in file1.readlines():
    if not(line.startswith('coding')):
        print(line)
        file2.write(line)

file2.close()
file1.close()