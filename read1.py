file=open('text.txt', 'r')
print(file.read())
file.close()

file=open('text.txt', 'r')
print("\n read in parts\n")
print(file.read(45))
file.close()

file=open('text.txt', 'a')
file.write("hi! iam a penguin and iam 1 year old.")
file.close()