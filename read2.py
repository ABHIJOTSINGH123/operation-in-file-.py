file_read=open('text.txt', 'r')
print("file in read mode-")
print(file_read.read())
file_read.close()

file_write=open('text.txt', 'w')
file_write.write("file in write mode")
file_write.write("hi! i am penguin .i am 1 year old")
file_write.close()

file_append=open('text.txt','a')
file_append.write("\n file is in appended mode...")
file_append.write("hi! i am a penguin.i am 1 year old")
file_append.close()